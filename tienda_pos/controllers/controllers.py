# -*- coding: utf-8 -*-
from odoo import http

# class TiendaPos(http.Controller):
#     @http.route('/tienda_pos/tienda_pos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tienda_pos/tienda_pos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tienda_pos.listing', {
#             'root': '/tienda_pos/tienda_pos',
#             'objects': http.request.env['tienda_pos.tienda_pos'].search([]),
#         })

#     @http.route('/tienda_pos/tienda_pos/objects/<model("tienda_pos.tienda_pos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tienda_pos.object', {
#             'object': obj
#         })