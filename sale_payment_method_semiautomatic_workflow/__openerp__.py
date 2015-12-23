# -*- coding: utf-8 -*-
# © 2015 FactorLibre - Ismael Calvo <ismael.calvo@factorlibre.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Sale Payment Method SemiAutomatic Workflow",
    "summary": "Allows to confirm the payment on a sale order",
    "version": "8.0.1.0.0",
    "category": "Accounting & Finance",
    "website": "https://factorlibre.com/",
    "author": "FactorLibre, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "external_dependencies": {},
    "depends": [
        "sale",
        "sale_payment_method",
        "sale_automatic_workflow"
    ],
    "data": [
        "data/sale_workflow_process_data.xml",
        "views/sale_order_view.xml",
        "views/sale_workflow_process_view.xml",
    ],
    "demo": [],
    "qweb": []
}
