# -*- coding: utf-8 -*-
# Copyright 2016 FactorLibre - Ismael Calvo <ismael.calvo@factorlibre.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.osv import orm


class SaleOrder(orm.Model):
    _inherit = 'sale.order'

    def _add_payment(self, cr, uid, sale, journal, amount, date,
                     description=None, context=None):
        if context is None:
            context = {}
        pmjl_pool = self.pool.get('payment.method.journal.line')
        jour_line_ids = False
        if sale.magento_bind_ids:
            currency = sale.magento_bind_ids[0].magento_currency_id
            jour_line_ids = pmjl_pool.search(cr, uid, [
                ('method', '=', sale.payment_method_id.id),
                ('currency', '=', currency and currency.id)
            ], context=context)
        if not jour_line_ids:
            jour_line_ids = pmjl_pool.search(cr, uid, [
                ('method', '=', sale.payment_method_id.id),
                ('currency', '=', False)
            ], context=context)
        if jour_line_ids:
            jour_line = pmjl_pool.browse(cr, uid, jour_line_ids[0],
                                         context=context)
            journal = jour_line.journal
        return super(SaleOrder, self)._add_payment(
            cr, uid, sale, journal, amount, date, description=description,
            context=context)
