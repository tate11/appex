# -*- coding: utf-8 -*-
{
    'name': "tour_travel",

    'summary': """
       tour travel is tour travel management""",

    'description': """
        tour travel is tour travel management efficient
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',  'account', 'product', 'sale','crm','purchase','sale_crm'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/action.xml',
        'views/menu.xml',
        'views/view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}