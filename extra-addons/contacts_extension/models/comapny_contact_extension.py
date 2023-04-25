from odoo import fields, api, models

class ComapnyContact(models.Model):
    _name ='company.contact'

    region = fields.Char(string='Region')
    rational = fields.Char(string='Rational')
    type = fields.Selection([('A', 'A'), ('B', 'B')], string='Type')
    opening_type = fields.Selection([('A', 'A'), ('B', 'B')], string='Opening type')
    next_opening = fields.Date(string='Next Opening')
    next_deadline = fields.Date(string='next Deadline')
    last_check = fields.Date(string='Last Check')
    about = fields.Text(string='About')
