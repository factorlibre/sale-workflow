# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Hugo Santos
#    Author: Rafael Valle
#    Author: Zahra Velasco
#    Copyright 2015-2017 FactorLibre
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
{
    'name': 'Sale Order Add Variants',
    'summary': 'Add variants from template into sale order',
    'version': '11.0.0.1.0',
    'author': 'FactorLibre,Odoo Community Association (OCA)',
    'category': 'Sale',
    'license': 'AGPL-3',
    'website': 'http://factorlibre.com',
    'depends': [
        'sale',
        'product'
    ],
    'demo': [],
    'data': [
        'security/sale_order_add_variants_security.xml',
        'wizard/sale_add_variants_view.xml',
        'view/sale_view.xml',
    ],
    'installable': True
}