# -*- coding: utf-8 -*-
{
    'name': "OpenHouse RealEstate",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Bjit",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'wizard/orderview.xml',
        'views/menu_action_final.xml',
        'views/properties_view_final.xml',
        'views/owner_view_final.xml',
        'views/customer_view_final.xml',

        'reports/report.xml',
        'reports/property_card.xml',
        'reports/order_details_wizard.xml',
        

        
    ],
    
    'installable': True,
    'auto_install': False,

}
