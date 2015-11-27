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
##############################################################################

from openerp import tools
from openerp import models, fields, api


class SaleMarginExtended(models.AbstractModel):

    _name = 'report.sale_margin_extended.report_slae_summury'

    def _get_sale_order_line(self, data):
        print False

    @api.multi
    def render_html(self, data=None):
        report_obj = self.env['report']
        report = report_obj._get_report_from_name('sale_margin_extended.report_slae_summury')
        report_sale_order_line = self._get_sale_order_line(data)
        docargs = {
            'doc_ids': self.ids,
            'doc_model': report.model,
            'docs': self,
            'get_sale_order_line': report_sale_order_line
        }
        return report_obj.render('sale_margin_extended.report_slae_summury', docargs)
