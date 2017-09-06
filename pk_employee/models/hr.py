# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Education(models.Model):
    _name = "hr.education"
    _description = "Employee Education Background"
    edu_degree = fields.Char('Education Degree')
    school = fields.Char('School')
    major = fields.Char('Major')
    awards = fields.Char('Awards')
    grade = fields.Char('Grade')


class Employee(models.Model):
    _name = 'hr.employee'
    _inherit = ['hr.employee']
    tax_code = fields.Char("Tax Code")
    social_insurance_id = fields.Char("Social Insurance Id")
    edu_degree = fields.Many2one('hr.education', string="Education Degree")
    school = fields.Many2one('hr.education', string="School")
    major = fields.Many2one('hr.education', string="Major")
    awards = fields.Many2one('hr.education', string="Awards")
    grade = fields.Many2one('hr.education', string="Grade")
