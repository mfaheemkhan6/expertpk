# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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
#    Developed by: thinkasoft , C.A.
#    Coded by: Aular Hector Manuel (aular.hector3@gmail.com)
#
##############################################################################

{
    'name': "Margins in Sales Orders extended",

    'summary': """
        the margin field has been add to the tree view""",

    'description': """
        This module add a field (margin) on tree view in Sales Orders
    """,

    'author': "Expert IT Solutions",
    'website': "https://expertpk.com/",

    'category': 'Sales Management',
    'version': '1.0',
    'depends': [
                'base',
                'sale',
                'sale_margin',
    ],
    'data': [
        'data/sale_margin_extended.xml'
        'views/report_slae_summury.xml',
        'views/sale_margin_extended.xml',
        'report/report.xml',
        'wizards/wizard_sale_margin_extended.xml',
        # 'security/ir.model.access.csv',
        # 'sale_margin_extended_templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
