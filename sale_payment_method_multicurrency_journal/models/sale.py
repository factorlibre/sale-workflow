# -*- coding: utf-8 -*-
# Copyright 2016 FactorLibre - Ismael Calvo <ismael.calvo@factorlibre.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def _add_payment(self, journal, amount, date, description=None):
        pmjl_pool = self.env['payment.method.journal.line']
        jour_line = False
        for sale in self:
            if sale.pricelist_id:
                currency = sale.pricelist_id.currency_id
                jour_line = pmjl_pool.search([
                    ('method', '=', sale.payment_method_id.id),
                    ('currency', '=', currency and currency.id)
                ], limit=1)
            if not jour_line:
                jour_line = pmjl_pool.search([
                    ('method', '=', sale.payment_method_id.id),
                    ('currency', '=', False)
                ], limit=1)
            if jour_line:
                journal = jour_line.journal
            return super(SaleOrder, self)._add_payment(
                journal, amount, date, description=description)
