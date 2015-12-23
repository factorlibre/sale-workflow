# -*- coding: utf-8 -*-
# © 2015 FactorLibre - Ismael Calvo <ismael.calvo@factorlibre.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class SaleWorkflowProcess(models.Model):
    _inherit = "sale.workflow.process"

    manual_payment_validation = fields.Boolean(
        'Manual Payment Confirm',
        default=False)
