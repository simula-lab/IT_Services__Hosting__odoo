{
    'name': 'project_extension',
    'category': 'Services',
    'version': '1.0.0',
    'description': "Odoo 16 Extension for Project",
    'summary': 'Odoo 16 Extension for Project ',
    'sequence': 1,
    'depends': ['project'],
    'data': [
        'views/project_extension.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False
}
