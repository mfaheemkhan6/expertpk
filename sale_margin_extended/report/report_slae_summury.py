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

from openerp.osv import osv
from openerp.report import report_sxw


class SaleMarginExtended(report_sxw.rml_parse):

    _name = 'report.sale_margin_extended.report_slae_summury'

    def __init__(self, cr, uid, name, context=None):
        super(SaleMarginExtended, self).__init__(cr, uid, name, context=context)
        self.init_bal_sum = 0.0
        self.amount_currency = {}
        self.localcontext.update({
            'get_sale_order_line': self._get_sale_order_line,
        })

    def _get_sale_order_line(self, data):
        sale_order_obj = self.pool.get('sale.order')
        sale_order_line_obj = self.pool.get('sale.order.line')
        sale_order_ids = sale_order_obj.search(self.cr, self.uid, [('partner_id', '=', data['ids'])])
        import pdb
        pdb.set_trace()
        return False


class report_partnerledger(osv.AbstractModel):
    _name = 'report.sale_margin_extended.report_slae_summury'
    _inherit = 'report.abstract_report'
    _template = 'sale_margin_extended.report_slae_summury'
    _wrapped_report_class = SaleMarginExtended
