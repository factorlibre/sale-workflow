# -*- coding: utf-8 -*-
# © 2016 FactorLibre - Ismael Calvo <ismael.calvo@factorlibre.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, exceptions, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def _prepare_payment_move_lines(self, move_name, journal, period,
                                    amount, date):
        debit_line, credit_line = \
            super(SaleOrder, self)._prepare_payment_move_lines(
                move_name, journal, period, amount, date)
        method = self.payment_method_id
        res_amount, surcharge = method.get_surcharge(amount, self)
        if surcharge > 0:
            surcharge_line = dict(debit_line)
            if not method.surcharge_account:
                raise exceptions.Warning(
                    "The surcharge account is not configured for the payment "
                    "method '{0}'".format(method.name))
            surcharge_line['account_id'] = method.surcharge_account.id
            surcharge_line['debit'] = surcharge
            debit_line['debit'] = res_amount
            return debit_line, credit_line, surcharge_line
        else:
            return debit_line, credit_line
