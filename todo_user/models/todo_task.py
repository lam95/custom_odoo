# -*- coding: utf-8 -*- 
from odoo import models, fields, api 
class TodoTask(models.Model): 
    _inherit = 'todo.task' 
    user_id = fields.Many2one('res.users', 'Responsible') 
    date_deadline = fields.Date('Deadline')
    name = fields.Char(help="What needs to  be  done?")
    @api.multi 
    def do_clear_done(self): 
        domain = [('is_done', '=', True),'|',('user_id', '=', self.env.uid), ('user_id', '=', False)] 
        dones = self.search(domain) 
        dones.write({'is_done': False}) 
        return True
