# -*- coding: utf-8 -*-
{
    'name': "gym",
    'summary': """Gestión del módulo Gym""",
    'description': """Gestion de clases, usuarios, material, etc""", 
    'author': "ENG - SPA", 
    'website': "http://www.upo.es", 
    'category': 'Uncategorized', 
    'version': '0.1', 
    'depends': ['base'], 
    'data': [ 
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml', 
        ], 
    'demo': [ 
    'demo/demo.xml', 
        ], 
    'application': True, 
} 