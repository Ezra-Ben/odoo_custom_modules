from odoo import http
from odoo.http import request

class UserRegistration(http.Controller):

    @http.route('/user/register', type='http', auth='public', website=True)
    def register_form(self, **kwargs):
        groups = request.env['res.groups'].sudo().search([]) # You can modify this search if you need specific groups
        return request.render('user_registration.registration_form', {'groups':groups})

    @http.route('/user/register/submit', type='http', auth='public', website=True, methods=["POST"], csrf=True)
    def register_submit(self, **post):
        
         # Check if user already exists
        existing_user = request.env['res.users'].sudo().search([('login', '=', post.get('email'))])
        if existing_user:
            return request.redirect('/user/register?error=user_exists')

        # Get selected groups from the form
        selected_group_ids = post.get('groups_id')  # This might return a string or list

        # Convert to a list if it's a single value
        if isinstance(selected_group_ids, str):
           selected_group_ids = [int(selected_group_ids)]
        elif isinstance(selected_group_ids, list):
            selected_group_ids = [int(group_id) for group_id in selected_group_ids]

        
        #Create a new user record(relies on model's crerate method)
        vals = {
            'name' : post.get('name'),
            'login' : post.get('email'), # Used for authentication
            'password' : post.get('password'),
            'skills' : post.get('skills'),
            'portfolio_url' : post.get('portfolio'),
            'certifications' : post.get('certifications'),
            'groups_id': selected_group_ids  # Pass directly; the model will format it
        }   
        
        # Create the user
        user = request.env['res.users'].sudo().create(vals)
        
        if user:
            # Access the user's partner record (Odoo automatically creates a partner when the user is created)
            partner = user.partner_id  # This links to the partner associated with the user
            
            if partner:
                # Update the email field in the partner model
                partner.sudo().write({'email': post.get('email')})
                
        # Send verification email first (before allowing login)
        return request.redirect("/check-your-email")  # Redirect to an email confirmation page

    