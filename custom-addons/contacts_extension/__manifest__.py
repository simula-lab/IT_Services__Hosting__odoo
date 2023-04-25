{
    'name': 'contact_extension',
    'category': 'Sales',
    'version': '1.0.0',
    'description': "Odoo 16 Extension for Extension",
    'summary': 'Odoo 16 Extension for Extension ',
    'sequence': 1,
    'depends': ['contacts'],
    'data': [
        'views/company_contact.xml',
        'security/ir.model.access.csv'
    ],
    'installable': True,
    'application': False,
    'auto_install': False
}
