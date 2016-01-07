# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Hugo Santos
#    Copyright 2015 FactorLibre
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    qty_available = fields.Float(string='Quantity On Hand',
                                 compute='_get_available',
                                 store=False)
    virtual_available = fields.Float(string='Forecast Quantity',
                                     compute='_get_available',
                                     store=False)

    @api.multi
    def _get_available(self, field_names=None):
        product_pool = self.env['product.product']
        lines = self.browse(self.ids)

        res = {line.id: line.product_id.id for line in lines}
        products = product_pool.browse(res.values())

        ctx = dict(self.env.context)
        ctx['warehouse'] = self[0].order_id.warehouse_id.id
        products_attrs = products.with_context(ctx)._product_available()

        for line in lines:
            if res[line.id]:
                attrs = products_attrs[res[line.id]]
                line.qty_available = attrs['qty_available']
                line.virtual_available = attrs['virtual_available']
        return True
