# -*- coding: utf-8 -*-
# from odoo import http


# class LoginCustom(http.Controller):
#     @http.route('/login_custom/login_custom/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/login_custom/login_custom/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('login_custom.listing', {
#             'root': '/login_custom/login_custom',
#             'objects': http.request.env['login_custom.login_custom'].search([]),
#         })

#     @http.route('/login_custom/login_custom/objects/<model("login_custom.login_custom"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('login_custom.object', {
#             'object': obj
#         })
