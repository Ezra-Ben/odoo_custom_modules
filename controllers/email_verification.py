from odoo import http
from odoo.http import request

class UserVerification(http.Controller):
    @http.route('/check-your-email', type='http', auth='public', website=True)
    def check_email_page(self, **kwargs):
        return request.render('user_registration.check_email_template')

    @http.route('/verify_email/<string:token>', auth='public', type='http', website=True)
    def verify_email(self, token):
        # Search for the user based on the token
        user = request.env['res.users'].sudo().search([('verification_token', '=', token)], limit=1)
        if user:
            # Successful email verification
            user.email_verified = True
            user.verification_token = False  # Optionally reset the token after verification
            return request.render('user_registration.email_verified_success') # Redirect to profile page
        else:
            return request.render('user_registration.email_verified_failed')  # Display failure page
