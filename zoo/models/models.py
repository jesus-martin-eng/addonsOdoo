# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Animal(models.Model):
    _name = 'animal.zoo'
    _description = 'animal.zoo'

    name = fields.Char()
    especie = fields.Char()
    identificador = fields.Char()
    pais_procedencia = fields.Many2one('res.country', 'Pais', required=True)
    edad = fields.Integer()
    fecha_entrada = fields.Datetime()



