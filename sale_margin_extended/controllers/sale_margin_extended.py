# -*- coding: utf-8 -*-
from openerp import http

# class ../addons-haular/saleMarginExtended(http.Controller):
#     @http.route('/../addons-haular/sale_margin_extended/../addons-haular/sale_margin_extended/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/../addons-haular/sale_margin_extended/../addons-haular/sale_margin_extended/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('../addons-haular/sale_margin_extended.listing', {
#             'root': '/../addons-haular/sale_margin_extended/../addons-haular/sale_margin_extended',
#             'objects': http.request.env['../addons-haular/sale_margin_extended.../addons-haular/sale_margin_extended'].search([]),
#         })

#     @http.route('/../addons-haular/sale_margin_extended/../addons-haular/sale_margin_extended/objects/<model("../addons-haular/sale_margin_extended.../addons-haular/sale_margin_extended"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('../addons-haular/sale_margin_extended.object', {
#             'object': obj
#         })