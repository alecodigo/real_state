# -*- coding: utf-8 -*-

{
    'name': "Real Estate",
    'version': '1.0',
    'author': "Alejandro Sánchez",
    'category': 'Category',
    'description': """
    Description text
    """,
    'depends': ['base'],
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_menus.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        # 'demo/demo_data.xml',
    ],
    'application': True,
    'license': 'LGPL-3'
}