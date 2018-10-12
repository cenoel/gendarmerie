# -*- coding: utf-8 -*-
{
    'name': "OG GN",
    'sequence': -10,
    'icon':'/og_gn/static/description/icon.png',
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'description': """
        Long description of module's purpose
    """,
    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        # 'security/ir.model.access.csv',
        'data/ir_sequence_data_view.xml',
        'data/styly_data_src_view.xml',
        'views/gn_affectation_views.xml',
        'views/gn_grades_views.xml',
        'views/gn_personnel_views.xml',
        'views/gn_type_centre_travail_views.xml',
        'views/gn_lieu_travail_views.xml',
        'views/gn_menu_principale_views.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
