# -*- coding: utf-8 -*-
{
    'name': "nia_profile",

    'summary': """
        NIA Profile""",

    'description': """
        NIA Profile
    """,

    'author': "wael alkhalifa",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','contacts','mail'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',

        'views/profile.xml',

    ],

 
}
