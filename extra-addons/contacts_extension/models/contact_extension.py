from odoo import fields, api, models
import logging
class ContactExtension(models.Model):
    _inherit = 'res.partner'

    company_contact_id = fields.Many2one('company.contact')
    individual_contact_id = fields.Many2one('individual.contact')

    individual_contact_region = fields.Char(related = 'individual_contact_id.region',
                                            readonly=False)

    company_contact_region = fields.Char(related='company_contact_id.region',
                                         readonly=False)
    company_contact_rational = fields.Char(related='company_contact_id.rational',
                                           readonly=False)
    company_contact_type = fields.Selection(related='company_contact_id.type',
                                            readonly=False)
    company_contact_opening_type = fields.Selection(related='company_contact_id.opening_type',
                                                    readonly=False)
    company_contact_next_opening = fields.Date(related='company_contact_id.next_opening',
                                               readonly=False)
    company_contact_next_deadline = fields.Date(related='company_contact_id.next_deadline',
                                                readonly=False)
    company_contact_last_check = fields.Date(related='company_contact_id.last_check',
                                             readonly=False)
    company_contact_about = fields.Text(related='company_contact_id.about',
                                        readonly=False)


    def create(self, vals_list):
        logging.warning(vals_list)
        print(vals_list)
        if vals_list[0]['company_type'] == 'person':
            individual_region = {'region': self.individual_contact_region}
            individual_contact_record = self.env['company.contact'].create(individual_region)
            vals_list[0]['individual_contact_id'] = individual_contact_record.id

        elif vals_list[0]['company_type'] == 'company':
            company_region = { 'region': self.company_contact_region,
                                'rational': self.company_contact_rational,
                                'type': self.company_contact_type,
                                'opening_type': self.company_contact_opening_type,
                                'next_opening': self.company_contact_next_opening,
                                'next_deadline': self.company_contact_next_deadline,
                                'last_check': self.company_contact_last_check,
                                'about': self.company_contact_about}
            company_contact_record = self.env['company.contact'].create(company_region)
            vals_list[0]['company_contact_id'] = company_contact_record.id
        return super(ContactExtension, self).create(vals_list)


