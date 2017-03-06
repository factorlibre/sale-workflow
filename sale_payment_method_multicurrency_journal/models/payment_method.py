# -*- coding: utf-8 -*-
# Copyright 2016 FactorLibre - Ismael Calvo <ismael.calvo@factorlibre.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class PaymentMethod(models.Model):
    _inherit = "payment.method"

    multicurrency_journals = fields.One2many(
        'payment.method.journal.line',
        'method',
        string="Multicurrency journals")


class PaymentMethodJournalLine(models.Model):
    _name = "payment.method.journal.line"

    method = fields.Many2one('payment.method', 'Method')
    journal = fields.Many2one(
        'account.journal',
        'Journal',
        required=True)
    currency = fields.Many2one(
        'res.currency',
        'Currency')

    _sql_constraints = {
        ('currency_uniq', 'unique(method, currency)',
         'You can only set a journal for each currency.')
    }
