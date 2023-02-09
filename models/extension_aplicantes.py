# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
class CamposExtrasAplicantes(models.Model):
    _inherit = 'hr.applicant'
    apellidos=fields.Char('Apellidos')
    tipos=fields.Char('Tipo Identificación')
    identificacións=fields.Char('Identificación')
    f_aplicacion=fields.Date('Fecha aplicación')
    f_actu_cv=fields.Date('Fecha última actualización CV')
    f_nacimiento=fields.Date('Fecha de nacimiento')
    edad=fields.Integer('Edad')
    direccion=fields.Char('Dirección')
    cp=fields.Char('Código Postal')
    ciudad=fields.Char('Ciudad')
    provincia=fields.Char('Provincia')
    pais=fields.Char('País')
    nacionalidad=fields.Char('Nacionalidad')
    tipo_tel=fields.Char('Tipo Teléfono')
    tel=fields.Char('Teléfono')
    genero=fields.Char('Género')
    estado_civil=fields.Char('Estado civil')
    lic_de_conducir=fields.Char('Licencias de conducir')
    vehiculo_propio=fields.Char('Dispone de vehículo propio')
    disp_viajar=fields.Char('Disponibilidad para viajar')
    camb_residencia=fields.Char('Disponibilidad para cambio de residencia')
    discapa=fields.Char('Discapacidad')
    exp_lab=fields.Text('Experiencia profesional')
    formacion=fields.Text('Formación')
    idiomas=fields.Char('Idiomas')
    hab_y_conoci=fields.Text('Habilidades y conocimientos')
    evaluacion=fields.Char('Evaluaciones')
    test_de_comp=fields.Char('Test de Competencias')
    pres_filtrado_puntuacion=fields.Char('Preguntas de filtrado: Puntuación')
    pregunta_filtrado=fields.Char('Preguntas de filtrado')
    adecuacion=fields.Char('Adecuación')
    ia_match=fields.Char('IA-Match')
    
    
    _sql_constraints = [
                     ('identificacións_unique', 
                      'unique(identificacións)',
                      'Choose another value - it has to be unique!')
]