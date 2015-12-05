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
###########################################################################
#    Copyright (C) 2015 thinkasoft , C.A. (www.thinkasoft.com)
#    All Rights Reserved
# ############## Credits ######################################################
#    Developed by: thinkasoft , C.A.
#
#    Coded by:  Aular Hector Manuel (aular.hector3@gmail.com)
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
        consult = dict()
        result = list()
        sale_order_ids = list()
        pos = 1
        sale_order_obj = self.pool.get('sale.order')
        sale_order_line_obj = self.pool.get('sale.order.line')
        self.cr.execute("SELECT * from res_partner_res_partner_category_rel ")

        if data['form']['user_id']:
            cond = 'in'
            user_id = data['form']['user_id'][0]
        else:
            cond = 'not in'
            user_id = data['form']['user_id']

        cond2 = 'in' if data['form']['category_id'] else 'not in'
        partner_id = [x[1] for x in self.cr.fetchall() if x[0] in data['form']['category_id']]

        sale_order_condition = [
            ('user_id', cond, [user_id]),
            ('date_order', '>=', data['form']['date_from']),
            ('date_order', '<=', data['form']['date_to']),
            ('state', 'not in', ['draft', 'sent', 'cancel'])
        ]
        sale_order_ids = sale_order_obj.search(self.cr, self.uid, sale_order_condition)
        sale_order_condition = [
            ('partner_id', cond2, partner_id),
            ('id', 'in', sale_order_ids),
        ]
        sale_order_ids = sale_order_obj.search(self.cr, self.uid, sale_order_condition)
        for sale_order in sale_order_obj.browse(self.cr, self.uid, sale_order_ids, context=data['form']['used_context']):
            sale_dic = {
                'no': pos,
                'customer': sale_order.partner_id.name,
                'sale_order_id': sale_order.name,
                'total': sale_order.amount_total
            }
            pos += 1
            result.append(sale_dic)
            sale_order_ids.append(sale_order.id)
        consult['sale_order'] = result
        result = []
        pos = 1

        sale_order_condition = [
            ('order_id', 'in', sale_order_ids),
            ('state', 'not in', ['draft', 'sent', 'cancel'])
        ]

        sale_line_dic = dict(name=False)
        sale_order_ids = sale_order_line_obj.search(self.cr, self.uid, sale_order_condition, order='name')
        for sale_order_line in sale_order_line_obj.browse(self.cr, self.uid, sale_order_ids, context=data['form']['used_context']):

            if sale_order_line.name == sale_line_dic['name']:
                sale_line_dic['qty'] += sale_order_line.product_uom_qty
                sale_line_dic['total'] += sale_order_line.product_uom_qty * sale_order_line.price_unit
            else:
                sale_line_dic = {
                    'no': pos,
                    'name': sale_order_line.name,
                    'qty': sale_order_line.product_uom_qty,
                    'total': sale_order_line.product_uom_qty * sale_order_line.price_unit,
                }
                result.append(sale_line_dic)

            pos += 1
        consult['sale_order_line'] = result

        return consult


class ReportPartnerledger(osv.AbstractModel):
    _name = 'report.sale_margin_extended.report_slae_summury'
    _inherit = 'report.abstract_report'
    _template = 'sale_margin_extended.report_slae_summury'
    _wrapped_report_class = SaleMarginExtended
