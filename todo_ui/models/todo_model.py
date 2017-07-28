# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.addons.base.res.res_request import referenceable_models

class Tag(models.Model):
    """docstring for Tag"""
    _name = 'todo.task.tag'
    _description = 'Todo Tag'
    _parent_store = True
    name = fields.Char(size=40, string='Name')
    task_ids = fields.Many2many('todo.task','todo_task_tag_rel', 'tag_id', 'task_id', string='Tasks')
    parent_id = fields.Many2one('todo.task.tag', 'Parent Tag', ondelete='restrict')
    parent_left = fields.Integer('parent Left', index=True)
    parent_right = fields.Integer('parent Right', index=True)
    child_ids = fields.One2many('todo.task.tag', 'parent_id', 'Child Tags')

class Stage(models.Model):
    """docstring for Stage"""
    _name = 'todo.task.stage'
    _description = 'Todo Stage'
    _order = 'sequence, name'
    #string field
    name = fields.Char(size=40, string='Name')
    desc = fields.Text('Description')
    state = fields.Selection([('draft','New'),('open','Started'),('done','Closed')],'State')
    doc = fields.Html('Documentation')
    #number field
    sequence = fields.Integer('Sequence')
    perc_complete = fields.Float('% Complete', (3, 2))
    #data field
    date_effective = fields.Date('Effective Date')
    date_changed = fields.Datetime('Last Changed')
    #other field
    fold = fields.Boolean('Folded?')
    image = fields.Binary('Image')
    tasks =fields.One2many('todo.task', 'stage_id', 'Task in this Stage')

class TodoTask(models.Model):
    _inherit = 'todo.task'
    stage_id = fields.Many2one('todo.task.stage', 'Stage')
    # Task <-> Tag relation (keyword args):
    tag_ids = fields.Many2many('todo.task.tag','todo_task_tag_rel','task_id', 'tag_id', string='Tags')
    #refers_to = fields.Reference([('res.user', 'User'), ('res.partner', 'Partner')], 'Refers to')
    refers_to = fields.Reference(referenceable_models, 'Refers to')
    stage_fold = fields.Boolean('Stage Folded?', compute='_compute_stage_fold')

    @api.depends('stage_id.fold')
    def _compute_stage_fold(self):
        for task in self:
            task.stage_fold = task.stage_id.fold
