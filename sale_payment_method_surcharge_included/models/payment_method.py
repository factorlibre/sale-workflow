# -*- coding: utf-8 -*-
# © 2016 FactorLibre - Ismael Calvo <ismael.calvo@factorlibre.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class PaymentMethod(models.Model):
    _inherit = "payment.method"

    surcharge_included = fields.Boolean('Surcharge included')
    surcharge_amount = fields.Float('Amount')
    surcharge_type = fields.Selection([
        ('percentage', '%'),
        ('fixed', 'fixed')
    ])
    surcharge_account = fields.Many2one('account.account', 'Account')
