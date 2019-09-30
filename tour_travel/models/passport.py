# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Visa(models.Model):
    _name = 'passport'
    _description = "passport"
    
    image = fields.Char()
    state = fields.Char()
    name = fields.Char()
    partner_id = fields.Char()
    issue_date = fields.Char()
    expiry_date = fields.Char()
    visa_ids = fields.One2many('visa','passport_id')
    
    
    
class Visa2(models.Model):
    _name = 'passportkaka'
    _description = "passport"
    
    image = fields.Char()
    state = fields.Char()
    name = fields.Char()
    partner_id = fields.Char()
    issue_date = fields.Char()
    expiry_date = fields.Char()
    visa_ids = fields.One2many('visa','passport_id')



