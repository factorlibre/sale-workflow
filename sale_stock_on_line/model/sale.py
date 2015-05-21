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
from openerp import api, models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def update_stock_information(self):
        for line in self.order_line:
            line.write({
                'qty_available': line.product_id.qty_available,
                'virtual_available': line.product_id.virtual_available
            })


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    qty_available = fields.Float(string='Quantity On Hand',
                                 related='product_id.qty_available',
                                 store=True)
    virtual_available = fields.Float(string='Forecast Quantity',
                                     related='product_id.virtual_available',
                                     store=True)
