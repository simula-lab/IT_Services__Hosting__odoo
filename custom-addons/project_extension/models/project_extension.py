from odoo import fields, api, models

class ProjectExtension(models.Model):
    _inherit = 'project.project'
    official_project_title = fields.Char(string='Official Project Title')
    contact_reference_number = fields.Char(string='Contract reference number')
    contract_link =  fields.Char(string='Contract link')
    project_contract_signed_date = fields.Date(string='Project Contract Signed Date')
    project_start_date = fields.Date(string='Project Start Date')
    project_expected_closure_date = fields.Date(string='Project Expected Closure Date')
    project_actual = fields.Date(string='Project Actual')