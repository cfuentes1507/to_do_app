# -*- coding: utf-8 -*-

from odoo import models, fields

class ToDo(models.Model):
    _name = 'todo.app' #Nombre DB: todo_app
    _description = 'Lista de Tareas'

    name = fields.Char(string="Nombre")
    status = fields.Char(string="Estado")
    description = fields.Char(string="Descripcion")





























# class to_do_app(models.Model):
#     _name = 'to_do_app.to_do_app'
#     _description = 'to_do_app.to_do_app'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
