from odoo import models, api

class UserProfileUpdate(models.Model):
    _inherit = 'res.users'  # Extend res.users to use existing fields like name, skills, etc.
    
    _description = 'Updates user Profile'
    @api.model
    def action_save_profile(self):
        # Custom logic for saving/updating the user's profile
        for user in self:
            # Just call the write method to save the changes to the fields
            user.write({
                'skills': user.skills,
                'portfolio_url': user.portfolio_url,
                'certifications': user.certifications,
                'profile_visibility': user.profile_visibility,
                'profile_picture': user.profile_picture,
            })
        return True
