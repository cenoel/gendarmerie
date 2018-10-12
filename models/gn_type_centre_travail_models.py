# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class GnTypeCentreTravail(models.Model):
    _name = 'gn.type.centre.travail'

    name = fields.Char('Nom du type centre de travail', required=True)
    description = fields.Text('Description du centre')