
from odoo import models, fields


class RepairRequest(models.Model):
    _name = 'computer.repair'
    _description = 'Computer Repair Request'

    name = fields.Char(string='Problem', required=True)

    repair_date = fields.Date(
        string='Repair Date',
        default=fields.Date.today
    )

    estimated_cost = fields.Float(string='Estimated Cost')

    status = fields.Selection(
        [
            ('received', 'Received'),
            ('progress', 'In Progress'),
            ('repaired', 'Repaired')
        ],
        string='Status',
        default='received'
    )

    device_id = fields.Many2one(
        'computer.device',
        string='Device',
        required=True
    )
