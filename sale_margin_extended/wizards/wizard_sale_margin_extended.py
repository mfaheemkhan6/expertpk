# -*- coding: utf-8 -*-

from openerp import models, fields


class WizardSaleMarginExtended(models.TransientModel):

    _inherit = "account.common.account.report"
    _name = 'slae_summury.wizard'

    def _print_report(self, data):
        import pdb
        pdb.set_trace()
        import pdb
        pdb.set_trace()
        if context is None:
            context = {}
        data = self.pre_print_report(data, context=context)
        return self.pool['report'].get_action('sale_margin_extended.report_slae_summury', data=data, context=context)
