# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class GnGrades(models.Model):
    _name = 'gn.grades'

    name = fields.Char('Nom du grade', required=True)
    image = fields.Binary("Image")
    description = fields.Text('Description du grade')
    personnel_ids = fields.One2many('gn.personnel','grades_id', string='Personnel liés',readonly=True)