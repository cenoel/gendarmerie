# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class GnPersonnel(models.Model):
    _name = 'gn.personnel'
    _order = 'id desc'

    name = fields.Char('Nom et prénom', required=True)
    image = fields.Binary("Image")
    date_naissance = fields.Date('Date de naissance')
    lieu_naissance = fields.Char('Lieu de naissance')
    sexe = fields.Selection([
        ('femme', 'Femme'),
        ('Homme', 'Homme'),
    ])
    cin = fields.Char('Carte d\'Identité Nationale (CIN)',required=True)
    lieu_cin = fields.Char('Lieu de création CIN')
    date_cin = fields.Date('Date de création CIN')
    est_une_duplicata_cin = fields.Boolean('Est une CIN dupliqué?', default=False)
    lieu_duplicata_cin = fields.Char('Lieu du duplicata CIN')
    date_duplicata_cin = fields.Date('Date de duplicata CIN')
    matricule = fields.Char('Numero matricule',required=True)
    status_personnel = fields.Selection([
        ('fonction','En fonction'),
        ('retraite','En retraite'),
        ('demission','En demission'),
        ('deces','Décès suite aux travail'),
    ],default='fonction')
    affectation_ids = fields.One2many('gn.affectation','personnel_id',string='Les affectations liés')
    calcul_affectation = fields.Float('Nombre total d\'affectation',compute='_calcul_nombre_affectation')
    grades_id = fields.Many2one('gn.grades',string='Grade')

    @api.constrains('cin')
    def check_cin(self):
        if self.cin.isdigit() == False:
            raise UserError('CIN ne peux pas comporter des lettre alpha')
        if self.cin.isdigit() == True:
            if len(self.cin) < 12 or len(self.cin) > 12:
                raise UserError('CIN ne peut pas etre inferiere ou superieur a 12 chiffre')

    @api.multi
    @api.depends('affectation_ids')
    def _calcul_nombre_affectation(self):
        for line in self:
            line.calcul_affectation = len(line.affectation_ids)

    @api.multi
    def selectionner_tout_affectation_lie(self):
        return {
            'name': _('Affectation personnel'),
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'gn.affectation',
            'type': 'ir.actions.act_window',
            'context': {'default_personnel_id': self.id},
            'domain': [('personnel_id', '=', self.id)],
        }

