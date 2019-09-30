# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Todo(models.Model):
    _name = 'todo.todo'
    #Draft --> Waiting for Approval --> Approved or Rejected.
    state = fields.Selection([
        ('draft', 'Draft'),
        ('waiting_for_approval', 'Waiting for Approval'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('cancel', 'Cancel')
        ], default='draft')
    description = fields.Text()
    created_date = fields.Date()
    deadline = fields.Date()
    responsible_id = fields.Many2one('res.users')
    manager_id = fields.Many2one('res.users')
    

    @api.multi
    def action_draft(self):
        self.state = 'draft'    
    @api.multi
    def action_waiting_for_approval(self):
        self.state = 'waiting_for_approval'
    @api.multi
    def action_approved(self):
        self.state = 'approved'
    @api.multi
    def action_rejected(self):
        self.state = 'rejected'
    @api.multi
    def action_cancel(self):
        self.state = 'cancel'    
        
    
    

