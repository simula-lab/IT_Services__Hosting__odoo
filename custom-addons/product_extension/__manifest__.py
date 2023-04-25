{
    'name': 'product_extension',
    'category': 'Productivity',
    'version': '1.0.0',
    'description': "Odoo 16 Extension for Products",
    'summary': 'Odoo 16 Extension for Products ',
    'sequence': 2,
    'depends': ['product'],
    'data': [
        'views/product_general_information.xml',
        'views/product_pages.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False
}
