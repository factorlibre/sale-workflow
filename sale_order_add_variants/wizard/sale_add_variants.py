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

from openerp import api, models, fields, _


class SaleAddVariants(models.TransientModel):
    _name = 'sale.add.variants'

    product_tmpl_id = fields.Many2one('product.template', string="Template",
                                      required=True)
    variant_line_ids = fields.One2many('sale.add.variants.line', 'wizard_id',
                                       string="Variant Lines")

    @api.multi
    def clear_previous_selections(self):
        for line in self.variant_line_ids:
            line.unlink()

    @api.onchange('product_tmpl_id')
    def _onchange_product_tmpl_id(self):
        if self.product_tmpl_id:
            product_variants = self.env['product.product'].search([
                ('product_tmpl_id', '=', self.product_tmpl_id.id)
            ])
            variant_lines = []
            for variant in product_variants:
               variant_lines.append([0, 0, {
                    'product_id': variant.id,
                    'quantity': 0
                }])
            self.variant_line_ids = variant_lines

    @api.multi
    def add_to_order(self):
        context = self.env.context
        sale_order = self.env['sale.order'].browse(context.get('active_id'))
        for line in self.variant_line_ids:
            if not line.quantity:
                continue
            line_values = {
                'product_id': line.product_id.id,
                'product_uom_qty': line.quantity,
                'order_id': sale_order.id
            }
            sale_order.order_line.create(line_values)

    @api.multi
    def add_to_order_continue(self):
        self.add_to_order()
        self.clear_previous_selections()
        return self.open_new_window()

    @api.multi
    def open_new_window(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'sale.add.variants',
            'name': _('Add Variants'),
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new',
            'nodestroy': True,
            'context': self.env.context
        }


class SaleAddVariantsLine(models.TransientModel):
    _name = 'sale.add.variants.line'

    wizard_id = fields.Many2one('sale.add.variants')
    product_id = fields.Many2one('product.product', string="Variant",
                                 required=True, readonly=True)
    quantity = fields.Float(string="Quantity")