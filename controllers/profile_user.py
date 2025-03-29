from odoo import http
from odoo.http import request
import base64

class UserProfile(http.Controller):

    @http.route('/my/profile', auth="user", website=True)
    def profile_dashboard(self, **kwargs):
        
        # Logic for the frontend user profile view
        user = request.env.user

        if not user or user.id == request.website.user_id.id:
            user = None  # Handle public user safely
        
        #Pass the user object to the template
        return request.render('user_registration.user_profile_frontend_readonly_form', {
            "user": user
        })
    
    @http.route('/admin/user/profile', auth="user", website=False)
    def profile_backend(self, **kwargs):
        # Logic for backend user profile view (admin)
        user = request.env.user
        return request.render('user_registration.view_user_profile_form', {
            "user": user
        })
    
    @http.route('/my/profile/update', type='http', auth="user",methods=["GET"], website=True)
    def update_profile_form(self, **kwargs):
        #Render the update profile form
        user = request.env.user
        return request.render('user_registration.user_profile_update_form',{
            "user": user       # user object automatically includes 'image_1920'
        })

    @http.route('/my/profile/update', type='http', auth="user", methods=["POST"], website=True)
    def update_profile(self, **post):
        # Logic for updating user profile for currently logged in users in the frontend(website)
        user = request.env.user
        # Check if the user has uploaded a new profile picture (Base64 data from form)
        image = request.httprequest.files.get('profile_picture') 
        
        if image:
           image_data = image.read()
           user.sudo().write({
            'image_1920':  base64.b64encode(image_data)
        })
        
        user.sudo().write({
            'name': post.get('name'),
            'email': post.get('email'),
            'skills': post.get('skills'),
            'portfolio_url': post.get('portfolio_url'),
            'certifications': post.get('certifications'),
            'profile_visibility': post.get('profile_visibility')
        })
        return request.redirect('/my/profile')
    
    @http.route('/admin/user/profile/update', type='http', auth="user", methods=["POST"], website=False)
    def update_profile_backend(self, **post):
        # Logic for updating user profile in the backend (admin)
        user = request.env.user
        user.sudo().write({
            'name': post.get('name'),
            'skills': post.get('skills'),
            'portfolio_url': post.get('portfolio_url'),
            'certifications': post.get('certifications')
        })
        return request.redirect('/admin/user/profile')
