from odoo import models, fields


class Customer(models.Model):
    _name = 'computer.customer'
    _description = 'Computer Service Customer'

    name = fields.Char(string='Customer Name', required=True)
    phone = fields.Char(string='Phone Number')
    email = fields.Char(string='Email')
    address = fields.Char(string='Address')