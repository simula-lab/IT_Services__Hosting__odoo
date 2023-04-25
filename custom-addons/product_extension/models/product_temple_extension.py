from odoo import fields, api, models

selling_unit_selection = [('A', 'A'), ('B', 'B'), ('C', 'C')]

class ProductExtension(models.Model):
    _inherit = 'product.template'
    selling_unit = fields.Selection(selling_unit_selection)