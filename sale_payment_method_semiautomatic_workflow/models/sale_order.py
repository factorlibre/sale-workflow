# -*- coding: utf-8 -*-
# © 2015 FactorLibre - Ismael Calvo <ismael.calvo@factorlibre.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    manual_payment_validation = fields.Boolean(
        'Manual Payment Validation',
        related='workflow_process_id.manual_payment_validation')

    @api.multi
    def confirm_payments(self):
        print "confirm_payments"
        self.automatic_payment()
