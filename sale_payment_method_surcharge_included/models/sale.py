# -*- coding: utf-8 -*-
# © 2016 FactorLibre - Ismael Calvo <ismael.calvo@factorlibre.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def _prepare_payment_move_lines(self, move_name, journal, period,
                                    amount, date):
        debit_line, credit_line = \
            super(SaleOrder, self)._prepare_payment_move_lines(
                move_name, journal, period, amount, date)
        method = self.payment_method_id
        if method.surcharge_included:
            charge_type = method.surcharge_type
            charge_amount = method.surcharge_amount
            surcharge_line = dict(credit_line)
            surcharge_line['account_id'] = method.surcharge_account.id
            if charge_type == 'fixed':
                credit_line['credit'] -= charge_amount
                surcharge_line['credit'] = charge_amount
            elif charge_type == 'percentage':
                credit_line['credit'] = amount * (100 - charge_amount) / 100
                surcharge_line['credit'] = amount * charge_amount / 100
            else:
                raise NotImplementedError
            credit_line['credit']
            return debit_line, credit_line, surcharge_line
        else:
            return debit_line, credit_line
