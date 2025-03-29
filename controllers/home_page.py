from odoo import http
from odoo.http import request

class HomepageController(http.Controller):
    @http.route('/', type='http', auth="public", website=True)
    def custom_homepage(self, **kwargs):
        return request.render('user_registration.homepage_template', {})
