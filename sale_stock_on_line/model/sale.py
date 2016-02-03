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
from openerp import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    qty_available = fields.Float(string='Quantity On Hand',
                                 compute='_get_available',
                                 store=False)
    virtual_available = fields.Float(string='Forecast Quantity',
                                     compute='_get_available',
                                     store=False)

    @api.depends('product_id', 'order_id.warehouse_id')
    def _get_available(self):
        for line in self:
            if not line.product_id:
                continue
            product = line.product_id
            ctx = dict(self.env.context)
            ctx['warehouse'] = line.order_id.warehouse_id.id
            line.qty_available = product.with_context(ctx).qty_available
            line.virtual_available =\
                product.with_context(ctx).virtual_available
