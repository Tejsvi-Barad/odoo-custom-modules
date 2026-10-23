from odoo import models, fields


class StudentActivity(models.Model):
    _name = 'student.course.activity'
    _description = 'Student Activity'

    name = fields.Char(string='Activity Name', required=True)
    description = fields.Text(string='Description')

    student_ids = fields.Many2many(
        'student.course.student',
        'student_activity_rel',
        'activity_id',
        'student_id',
        string='Students'
    )