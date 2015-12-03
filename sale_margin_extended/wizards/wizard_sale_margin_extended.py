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

import time
from openerp.osv import fields, osv
from openerp import api, exceptions
from datetime import datetime
from dateutil import relativedelta


class WizardSaleMarginExtended(osv.osv_memory):

    _inherit = "account.common.account.report"
    _name = 'slae_summury.wizard'

    _columns = {
        'user_id': fields.many2one('res.users', 'Salesperson', readonly=False,),
        'category_id': fields.many2many('res.partner.category', id1='partner_id',
         id2='category_id', string='Category' ,readonly=False),
    }
    _defaults = {
        'date_from': lambda *a: time.strftime('%Y-%m-01'),
        'date_to': lambda *a: str(datetime.now() + relativedelta.relativedelta(months=+1, day=1, days=-1))[:10],
    }

    @api.constrains('date_from', 'date_to')
    def _check_date(self):
        for record in self:
            if record.date_to < record.date_from:
                raise exceptions.ValidationError("Ended date must be equal o later than Started date")

    def _print_report(self, cr, uid, ids, data, context=None):
        if context is None:
            context = {}

        data = self.pre_print_report(cr, uid, ids, data, context=context)
        data['form'].update(self.read(cr, uid, ids, ['date_from', 'date_to', 'user_id','category_id'])[0])
        return self.pool['report'].get_action(cr, uid, [], 'sale_margin_extended.report_slae_summury', data=data, context=context)
