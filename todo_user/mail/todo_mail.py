from odoo import models 
class TodoTask(models.Model): 
    _name = 'todo.task' 
    _inherit = 'mail.thread'