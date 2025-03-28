# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Animal(models.Model):
    _name = 'animal.zoo'
    _description = 'animal.zoo'

    name = fields.Char(string = "Nombre", required=True)
    especie = fields.Char(string = "Especie", required=True)
    identificador = fields.Char(string = "Identificador", required=True)
    pais_procedencia = fields.Many2one('res.country', 'Pais', required=True)
    edad = fields.Integer(string = "Edad", required=True)
    fecha_entrada = fields.Datetime(string = "Fecha de entrada", required=True)

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

class Espacio(models.Model):
    _name = 'espacio.zoo'
    _description = 'espacio.zoo'

    codigo_espacio = fields.Char(string = "Código", required=True)
    tipo = fields.Selection([('jaula', 'Jaula'),
                             ('vallado', 'Vallado'),
                             ('acuario', 'Acuario'),
                             ('terrarium', 'Terrarium')], string = "Tipo", required=True)
    area_tematica = fields.Selection([('europa', 'Europa'),
                            ('asia', 'Asia'),
                            ('africa', 'África'),
                            ('america', 'América'),
                            ('oceania', 'Oceanía')
                            ], string='Área Temática', required=True)

