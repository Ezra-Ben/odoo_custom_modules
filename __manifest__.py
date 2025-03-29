# -*-coding UTF-8 -*-
{
'name': 'User Profile',
'version': '1.0',
'author': 'Mukisa Ben Ezra',
'category': 'Human Resource',
'summary': 'User Registration and Profile',
'description': """
 User Proseit
 ==============
 Registers users and authenticates user credentials 
 on login and provides access to user profile details
 allowing user to change and update user information.
 """,
'depends': ['base', 'website', 'auth_oauth', 'mail'],
'data': [
        'views/frontend/email_verification_templates.xml',
        'views/frontend/homepage.xml',
        'views/frontend/menu.xml',
        'views/frontend/profile_update_frontend_form.xml',
        'views/frontend/registration_thank_you.xml',
        'views/frontend/registration_frontend_view.xml',
        'views/frontend/user_profile_frontend_view.xml',
        'data/email_template.xml',
],
'application': True,
'installable': True,
'license': 'LGPL-3',
}