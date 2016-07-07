# -*- coding: utf-8 -*-
# Copyright 2016 FactorLibre - Ismael Calvo <ismael.calvo@factorlibre.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.osv import fields, orm


class PaymentMethod(orm.Model):
    _inherit = "payment.method"

    _columns = {
        'multicurrency_journals': fields.one2many(
            'payment.method.journal.line',
            'method',
            string="Multicurrency journals")
    }


class PaymentMethodJournalLine(orm.Model):
    _name = "payment.method.journal.line"

    _columns = {
        'method': fields.many2one('payment.method', 'Method'),
        'journal': fields.many2one(
            'account.journal',
            'Journal',
            required=True),
        'currency': fields.many2one(
            'res.currency',
            'Currency')
    }

    _sql_constraints = {
        ('currency_uniq', 'unique(method, currency)',
         'You can only set a journal for each currency.')
    }
