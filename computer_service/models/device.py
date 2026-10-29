from odoo import models, fields


class Device(models.Model):
    _name = 'computer.device'
    _description = 'Computer Device'

    name = fields.Char(string='Device Name', required=True)
    device_type = fields.Selection(
        [
            ('laptop', 'Laptop'),
            ('desktop', 'Desktop'),
            ('printer', 'Printer'),
            ('other', 'Other')
        ],
        string='Device Type',
        required=True
    )
    serial_number = fields.Char(string='Serial Number')

    customer_id = fields.Many2one(
        'computer.customer',
        string='Customer',
        required=True
    )
