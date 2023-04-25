from odoo import fields, api, models

class IndividualContact(models.Model):
    _name ='individual.contact'

    region = fields.Char(string='Region')
