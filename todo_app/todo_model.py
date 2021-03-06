# -*- coding: utf-8 -*- 
from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)


class TodoTask(models.Model): 
    _name = 'todo.task' 
    _description = 'To-do Task by laamNguyen'
    name = fields.Char('Description', required=True)
    is_done = fields.Boolean('Done?') 
    active = fields.Boolean('Active?', default=True)
    
    @api.multi
    def do_toggle_done(self): 
        for task in self: 
            task.is_done = not task.is_done 
        return True

    @api.multi
    def do_clear_done(self):
        dones = self.search([('is_done', '=', True)])
        dones.write({'is_done': False})
        return True
