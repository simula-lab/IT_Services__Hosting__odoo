from odoo import fields, api, models


class WebsiteOpportunities(models.Model):
    _name = 'website.opportunities'
    _rec_name = 'name'
    _description = 'Website opportunities'
    name = fields.Char(string='Name')
    type = fields.Selection([('A', 'A'), ('A', 'A')], string='Type')
    website = fields.Char(string='Website')
    project_types = fields.Text(string='Project Type')
    countries = fields.Many2one('res.country', string='Countries')
    agencies_domain = fields.Selection([('A', 'A'),('B', 'B')], string='Agencies Domains')
    organization_domains = fields.Selection([('A', 'A'),('B', 'B')], string='')
    about = fields.Text(string='About')
    price_per_year = fields.Float(string='Price per Year')
    last_check = fields.Text(string='Last check')
    two_weeks_insight = fields.Text(string='2 Weeks insights')
    book_mark = fields.Char(string='Bookmark')
