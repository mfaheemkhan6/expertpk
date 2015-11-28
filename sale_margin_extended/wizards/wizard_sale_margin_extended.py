# -*- coding: utf-8 -*-

from openerp.osv import fields, osv


class WizardSaleMarginExtended(osv.osv_memory):

    _inherit = "account.common.account.report"
    _name = 'slae_summury.wizard'

    _columns = {
        'user_id': fields.many2one('res.users', 'Salesperson', readonly=False, required=True,),
    }
    _defaults = {
        'user_id': lambda self, cr, uid, context: uid,
    }

    def _print_report(self, cr, uid, ids, data, context=None):
        if context is None:
            context = {}
        data = self.pre_print_report(cr, uid, ids, data, context=context)
        data['form'].update(self.read(cr, uid, ids, ['date_from', 'date_to', 'user_id'])[0])
        return self.pool['report'].get_action(cr, uid, [], 'sale_margin_extended.report_slae_summury', data=data, context=context)
