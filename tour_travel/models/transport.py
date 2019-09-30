# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Transport(models.Model):
    _name = 'tour.transport'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Transport Provider"
    transport_line = fields.Char()
    partner_id = fields.Many2one('res.partner')
