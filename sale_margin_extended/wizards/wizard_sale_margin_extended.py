# -*- coding: utf-8 -*-

from openerp.osv import fields, osv


class WizardSaleMarginExtended(osv.osv_memory):

    _inherit = "account.common.account.report"
    _name = 'slae_summury.wizard'

    def _print_report(self, cr, uid, ids, data, context=None):
        if context is None:
            context = {}
        data = self.pre_print_report(cr, uid, ids, data, context=context)
        data['form'].update(self.read(cr, uid, ids, ['date_from', 'date_to'])[0])
        return self.pool['report'].get_action(cr, uid, [], 'sale_margin_extended.report_slae_summury', data=data, context=context)
