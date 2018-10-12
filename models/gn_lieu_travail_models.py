# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError
REGION = [
            ('Diana', 'Diana'),
            ('Sava', 'Sava'),
            ('Itasy', 'Itasy'),
            ('Analamanga', 'Analamanga'),
            ('Vakinankaratra', 'Vakinankaratra'),
            ('Bongolava', 'Bongolava'),
            ('Sofia', 'Sofia'),
            ('Boeny', 'Boeny'),
            ('Betsiboka', 'Betsiboka'),
            ('Melaky', 'Melaky'),
            ('Alaotra-Mangoro', 'Alaotra-Mangoro'),
            ('Atsinanana', 'Atsinanana'),
            ('Analanjirofo', 'Analanjirofo'),
            ('Amoro-Mania', 'Amoron\'i Mania'),
            ('Haute Matsiatra', 'Haute Matsiatra'),
            ('Vatovavy-Fitovinany', 'Vatovavy-Fitovinany'),
            ('Atsimo-Atsinanana', 'Atsimo-Atsinanana'),
            ('Ihorombe', 'Ihorombe'),
            ('Menabe', 'Menabe'),
            ('Atsimo-Andrefana', 'Atsimo-Andrefana'),
            ('Androy', 'Androy'),
            ('Anôsy', 'Anôsy'),
        ]
PROVINCE = [
            ('Tananarive','Tananarive'),
            ('Diego-Suarez','Diego-Suarez'),
            ('Fianarantsoa','Fianarantsoa'),
            ('Majunga','Majunga'),
            ('Tamatave','Tamatave'),
            ('Tuléar','Tuléar'),
        ]

class GnLieuTravail(models.Model):
    _name = 'gn.lieu.travail'

    name = fields.Char('Nom du ville', required=True)
    type_ville = fields.Selection([
        ('prefecture', 'Préfecture'),
        ('sous-prefecture', 'Sous-préfecture'),
        ('district', 'District'),
        ('canton', 'Canton'),
        ('commune', 'Commune'),
    ], string='Type du ville')
    ville_parent_id = fields.Many2one('gn.lieu.travail', string='Ville parent')
    region = fields.Selection(REGION, 'Region')
    province = fields.Selection(PROVINCE, 'Province')
    type_poste = fields.Many2many('gn.type.centre.travail',string='Type de centre de travail',required=True)

    @api.onchange('ville_parent_id')
    def get_info_parent(self):
        self.region = self.ville_parent_id.region
        self.province = self.ville_parent_id.province






