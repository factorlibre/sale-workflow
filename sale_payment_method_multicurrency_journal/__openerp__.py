# -*- coding: utf-8 -*-
# Copyright 2016 FactorLibre - Ismael Calvo <ismael.calvo@factorlibre.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Sale Payment Method Multicurrency Journal",
    "summary": "Allows to assign a different journal by the order currency",
    "version": "8.0.1.0.0",
    "category": "",
    "website": "https://odoo-community.org/",
    "author": "FactorLibre, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        "sale_payment_method",
    ],
    "data": [
        "views/payment_method_view.xml",
        "security/ir.model.access.csv",
    ],
    "demo": [],
    "qweb": []
}
