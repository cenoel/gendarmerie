# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class GnAffectation(models.Model):
    _name = 'gn.affectation'

    name = fields.Char('Numero d\'affectation', required=True)
    personnel_id = fields.Many2one('gn.personnel',string='Personnel concerné')
    ancien_poste = fields.Many2one('gn.lieu.travail','Ancien poste')
    nouvelle_poste = fields.Many2one('gn.lieu.travail',string='Nouvelle poste', required=True)
    status_affectation = fields.Selection([
        ('encour','En cours'),
        ('fini','Fini'),
    ],default='encour')

    @api.onchange('personnel_id')
    def se_numero_affectation(self):
        if self.name == False:
            self.name = self.env['ir.sequence'].next_by_code('set_numero_affectation')
        if self.personnel_id.id != False:
            affectation_list = self.env['gn.affectation'].search([
                                                              ('personnel_id', '=', self.personnel_id.id)
                                                              ], limit=1, order='id desc')
            self.ancien_poste = affectation_list.nouvelle_poste.id
            if self.name == False:
                self.name = self.personnel_id.matricule +\
                            '-' +\
                            self.env['ir.sequence'].next_by_code('set_numero_affectation')[-22:]
            else:
                self.name = self.personnel_id.matricule + '-' + self.name[-22:]


    @api.model
    def create(self, values):
        affectation_obj = super(GnAffectation, self).create(values)
        affectation_list = self.env['gn.affectation'].search(['&',
                                           ('id', '!=', affectation_obj.id),
                                           ('personnel_id', '=', affectation_obj.personnel_id.id)
                                           ])
        for line in affectation_list:
            if line.id:
                set_terminer = self.env['gn.affectation'].browse(line.id)
                set_terminer.update({
                    'status_affectation': 'fini'
                })

        return affectation_obj