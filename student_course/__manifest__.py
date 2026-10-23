
{
    'name': 'Student Course Management',
    'version': '1.0',
    'summary': 'Manage students, courses, enrollments and dashboard',
    'category': 'Education',
    'author': 'Tejsvi Barad',
    'license': 'LGPL-3',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/student_views.xml',
        'views/course_views.xml',
        'views/enrollment_views.xml',
        'views/dashboard_views.xml',
        'views/idcard_views.xml',
        'views/activity_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'student_course/static/src/js/dashboard.js',
            'student_course/static/src/xml/dashboard.xml',
            'student_course/static/src/css/dashboard.css',
        ],
    },
    'installable': True,
    'application': True,
}
