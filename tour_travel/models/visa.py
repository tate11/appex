# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Visa(models.Model):
    _name = 'visa'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Visa"
    
    state = fields.Char()
    name = fields.Char()
    issue_date = fields.Char()
    expiry_date = fields.Char()
    country_id = fields.Char()
    type_id = fields.Char()
    partner_id = fields.Char()
    passport_id = fields.Many2one('passport')
    visa_img = fields.Char()

