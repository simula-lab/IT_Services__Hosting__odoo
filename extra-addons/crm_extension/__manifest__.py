{
    'name': 'crm_extension',
    'category': 'Sales',
    'version': '1.0.0',
    'description': "Odoo 16 Extension for CRM",
    'summary': 'Odoo 16 Extension for CRM ',
    'sequence': 1,
    'depends': ['crm'],
    'data': [
        'views/crm_details.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False
}
