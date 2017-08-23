# -*- coding: utf-8 -*-
# © 2016 FactorLibre - Ismael Calvo <ismael.calvo@factorlibre.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, exceptions, fields, models
from openerp.tools.float_utils import float_round


class PaymentMethod(models.Model):
    _inherit = "payment.method"

    surcharge_lines = fields.One2many(
        'payment.method.surcharge.line',
        'payment_method',
        string="Surcharge lines")
    surcharge_account = fields.Many2one('account.account', 'Account')

    def get_surcharge(self, amount, order):
        self.ensure_one()
        res_amount = amount
        country_id = order.partner_id.country_id
        country_id = country_id.id
        for line in self.surcharge_lines:
            # Check the country
            if line.country_apply_type == 'specific' and \
                    line.country.id != country_id:
                continue
            elif line.country_apply_type == 'except' and \
                    line.country.id == country_id:
                continue

            # Get the amount
            if line.surcharge_type == 'fixed':
                res_amount -= line.amount
            elif line.surcharge_type == 'percentage':
                subtract = res_amount * line.amount / 100
                if subtract < line.min_amount:
                    subtract = line.min_amount
                res_amount -= subtract
        res_amount = float_round(res_amount, 2)
        return res_amount, amount - res_amount


class PaymentMethodSurchargeLine(models.Model):
    _name = "payment.method.surcharge.line"
    _order = "sequence,id"

    payment_method = fields.Many2one('payment.method', 'Payment method')
    amount = fields.Float('Amount', required=True)
    surcharge_type = fields.Selection([
        ('percentage', '%'),
        ('fixed', 'fixed')
    ], 'Surcharge type', required=True)
    country_apply_type = fields.Selection([
        ('specific', 'only to'),
        ('except', 'to all except')
    ], 'Country apply type')
    country = fields.Many2one('res.country', 'Country')
    min_amount = fields.Float('Minimum amount')
    sequence = fields.Integer(
        'Sequence', default=1, help="Determine the display order")

    @api.model
    def create(self, vals):
        if 'amount' not in vals or vals['amount'] <= 0:
            raise exceptions.Warning(
                "The amount of surcharges must be greater than 0.0")
        return super(PaymentMethodSurchargeLine, self).create(vals)
