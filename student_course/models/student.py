
from odoo import models, fields


class Student(models.Model):
    _name = 'student.course.student'
    _description = 'Student'

    name = fields.Char(string='Student Name', required=True)
    student_id = fields.Char(string='Student ID', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    course = fields.Char(string='Course')
    enrollment_date = fields.Date(string='Enrollment Date')
    active = fields.Boolean(string='Active', default=True)

    # Many-to-Many Relationship
    activity_ids = fields.Many2many(
        'student.course.activity',
        'student_activity_rel',
        'student_id',
        'activity_id',
        string='Activities'
    )
