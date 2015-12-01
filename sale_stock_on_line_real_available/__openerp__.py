# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Hugo Santos
#    Copyright 2015 FactorLibre
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
    'name': 'Sale Stock on line Real Available',
    'summary': 'Adds the real available (available - outgoing) on sale line',
    'version': '1.0',
    'author': "FactorLibre,Odoo Community Association (OCA)",
    'category': 'Sales Management',
    'license': 'AGPL-3',
    'images': [],
    'website': "http://factorlibre.com",
    'depends': [
        'product_stock_info',
        'sale_stock_on_line'
    ],
    'data': [
        'views/sale_view.xml'
    ],
    'installable': True,
    'auto_install': True,
}
