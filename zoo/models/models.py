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

class Cuidador(models.Model):
    _name = 'cuidador.zoo'
    _description = 'cuidador.zoo'

    name = fields.Char(string = "Nombre", required=True, )
    apellidos = fields.Char(string = "Apellidos", required=True)
    cargo = fields.Selection([
        ('supervisor', 'Supervisor'),
        ('encargado', 'Encargado'),
        ('cuidador', 'Cuidador')
    ], string='Cargo', required=True)
    fecha_incorporacion = fields.Datetime(string = "Fecha de Incorporación", required=True)



