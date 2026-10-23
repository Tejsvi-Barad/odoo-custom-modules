
from odoo import models, fields


class StudentIDCard(models.Model):
    _name = 'student.course.idcard'
    _description = 'Student ID Card'

    name = fields.Char(
        string='Card Number',
        required=True
    )

    student_id = fields.Many2one(
        'student.course.student',
        string='Student',
        required=True
    )

    issue_date = fields.Date(
        string='Issue Date',
        default=fields.Date.today
    )

    expiry_date = fields.Date(
        string='Expiry Date'
    )

    _sql_constraints = [
        (
            'unique_student_idcard',
            'UNIQUE(student_id)',
            'A student can have only one ID card.'
        ),
        (
            'unique_card_number',
            'UNIQUE(name)',
            'Card number must be unique.'
        ),
    ]
