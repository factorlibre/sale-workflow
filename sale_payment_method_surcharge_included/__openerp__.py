# -*- coding: utf-8 -*-
# © 2016 FactorLibre - Ismael Calvo <ismael.calvo@factorlibre.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Sale Payment Method Surcharge Included",
    "summary": "Allows to take a percentage of the order amount as payment "
               "expenses.",
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
    ],
    "demo": [],
    "qweb": []
}
