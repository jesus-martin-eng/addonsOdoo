# -*- coding: utf-8 -*-
# from odoo import http


# class MegaMarket(http.Controller):
#     @http.route('/mega_market/mega_market', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mega_market/mega_market/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mega_market.listing', {
#             'root': '/mega_market/mega_market',
#             'objects': http.request.env['mega_market.mega_market'].search([]),
#         })

#     @http.route('/mega_market/mega_market/objects/<model("mega_market.mega_market"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mega_market.object', {
#             'object': obj
#         })

