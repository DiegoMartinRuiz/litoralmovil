# -*- coding: utf-8 -*- 
from odoo import models, fields, api 
class CamposExtrasProductos(models.Model): 
    _inherit = 'product.product' 
    imei = fields.Float('IMEI', size=20, digits=(20, 0),required=False)
    mac_address = fields.Char('Mac Address')
    grupo= fields.Char('Grupo')
    marca= fields.Char('Marca')
    tipo=fields.Char('Tipo')