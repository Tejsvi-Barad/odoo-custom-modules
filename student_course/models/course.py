
from odoo import models, fields


class Course(models.Model):
    _name = 'student.course.course'
    _description = 'Course Management'
    _rec_name = 'name'

    name = fields.Char(string='Course Name', required=True)
    course_code = fields.Char(string='Course ID', required=True)
    fees = fields.Float(string='Course Fees')
    duration = fields.Char(string='Duration')
    description = fields.Text(string='Description')
    active = fields.Boolean(string='Active', default=True)
