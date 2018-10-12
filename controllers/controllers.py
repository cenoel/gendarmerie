# -*- coding: utf-8 -*-
from odoo import http

# class OgGn(http.Controller):
#     @http.route('/og_gn/og_gn/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/og_gn/og_gn/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('og_gn.listing', {
#             'root': '/og_gn/og_gn',
#             'objects': http.request.env['og_gn.og_gn'].search([]),
#         })

#     @http.route('/og_gn/og_gn/objects/<model("og_gn.og_gn"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('og_gn.object', {
#             'object': obj
#         })