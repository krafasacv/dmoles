# -*- coding: utf-8 -*-
{
    'name': "tienda_pos",

    'summary': """
        Modifica vista y recibo del POS para la tienda""",

    'description': """
        Modifica la vista principal y el recibo de la tienda
    """,

    'author': "KRA-FA SA DE CV",
    'website': "http://www.krafa.com.mx",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','point_of_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'views/views.xml',
        #'views/templates.xml',
    ],
    'qweb': ['static/src/xml/tienda_pos.xml'],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}