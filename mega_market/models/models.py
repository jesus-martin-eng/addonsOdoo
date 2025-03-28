# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Electrodomestico(models.Model):
    _name = 'megamarket.electrodomestico'
    _description = 'Electrodomésticos'

    name = fields.Char(string="Nombre", required = True, help ="nombre del electrodoméstico")
    codigo = fields.Char(string = "Código de Producto", required=True) 
    pais_id = fields.Many2one('res.country', 'Pais', required=True)
    importe_compra = fields.Float(string = "Importe de Compra", required=True)
    moneda_id = fields.Many2one('res.currency', 'Moneda', required=True) 
    precio_venta = fields.Float(string = "Precio de Venta", required=True, )

class Cliente(models.Model):
    _name = 'megamarket.cliente'
    _description = 'Cliente'

    name = fields.Char(string = "Nombre", required=True, help = "nombre del cliente")
    apellidos = fields.Char(string = "Apellidos", required=True, help = "apellidos del cliente")
    nif = fields.Char(string = "NIF", required=True)
    direccion = fields.Text()
    fecha_nacimiento = fields.Datetime(string = "Fecha de Nacimiento", required=True)
    telefono = fields.Char(string="Teléfono", required=True)
