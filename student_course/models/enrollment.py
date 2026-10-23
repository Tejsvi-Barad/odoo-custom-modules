
from odoo import models, fields, api


class Enrollment(models.Model):
    _name = 'student.course.enrollment'
    _description = 'Student Enrollment'
    _rec_name = 'student_id'

    student_id = fields.Many2one(
        'student.course.student',
        string='Student',
        required=True
    )

    course_id = fields.Many2one(
        'student.course.course',
        string='Course',
        required=True
    )

    enrollment_date = fields.Date(
        string='Enrollment Date',
        default=fields.Date.today
    )

    fees = fields.Float(string='Fees', default=0.0)

    status = fields.Selection(
        [
            ('draft', 'Draft'),
            ('enrolled', 'Enrolled'),
            ('completed', 'Completed'),
            ('cancelled', 'Cancelled')
        ],
        string='Status',
        default='draft'
    )

    @api.onchange('course_id')
    def _onchange_course_id(self):
        if self.course_id:
            self.fees = self.course_id.fees
        else:
            self.fees = 0.0
