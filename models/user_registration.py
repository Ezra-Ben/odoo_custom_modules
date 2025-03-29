from odoo import models, fields, api, _
import secrets

class UserRegistration(models.Model):
    _inherit = 'res.users'  # Inherit from the default user model 
    _description = "Extended User Registration for additional profile fields"

    # Your custom fields here 
    skills = fields.Text(string="Skills")
    portfolio_url = fields.Char(string="Portfolio URL")
    certifications = fields.Text(string="Certifications")
    profile_visibility = fields.Selection([
        ('public', 'Public'),
        ('private', 'Private')
    ], string="Profile Visibility", default='private')

    #Use Odoo's built-in image field for profile pictures
    profile_picture = fields.Binary(string="Profile Picture", related="image_1920", readonly=False)
    

    #Email verification fields
    verification_token = fields.Char(string="Verification Token")
    email_verified = fields.Boolean(string="Email Verified", default=False)

    @api.model
    def generate_verification_token(self):
        return secrets.token_urlsafe(32)

    @api.model
    def create(self, vals):
        # Generate a verification token and pass it to the vals dictionary before calling create() 
        vals['verification_token'] = self.generate_verification_token()
        
         # Ensure groups_id exists in vals and is properly formatted
        if 'groups_id' in vals and isinstance(vals['groups_id'], list):
            vals['groups_id'] = [(6, 0, vals['groups_id'])]  # Format correctly

        # Create the user record
        user = super(UserRegistration, self).create(vals)
        
        # Send the verification email
        template =  self.env.ref('user_registration.email_verification_template')
        if template:
            template.send_mail(user.id, force_send=True)
            
        return user

   