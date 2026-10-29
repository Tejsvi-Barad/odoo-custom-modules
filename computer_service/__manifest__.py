{
    'name': 'Computer Service Management',
    'version': '18.0.1.0.0',
    'summary': 'Manage computer repair work',
    'author': 'Tejsvi Barad',
    'category': 'Services',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/customer_views.xml',
        'views/device_views.xml',
        'views/repair_request_views.xml',
    ],
    'installable': True,
    'application': True,
}