# -*- coding: utf-8 -*- 
from odoo import models, fields, api 
class CamposExtrasEmployees(models.Model): 
    _inherit = 'hr.employee' 
    dni = fields.Float('DNI', size=8, digits=(20, 0),required=False)
    cuit = fields.Float('Cuit', size=11, digits=(20, 0),required=False)
    nombre_pila= fields.Char('Nombre de Pila')
    apellido=fields.Char('Apellido')
    legajo= fields.Integer('Legajo')
    num_cta_bco=fields.Char('Numero de Cuenta Bancaria')