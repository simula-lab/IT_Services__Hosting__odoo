{
    'name': 'website opportunities',
    'category': 'Website',
    'version': '1.0.0',
    'description': "Odoo 16 Website Opportunities",
    'summary': 'Odoo 16 Website Opportunities ',
    'sequence': 1,
    'depends': ['contacts'],
    'data': [
        'views/menu.xml',
        'views/website_opportunities.xml',
        'security/ir.model.access.csv'
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
