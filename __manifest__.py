# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Litoral Movil',
    'version': '1.0',
    'category': 'Extras',
    'author': 'Diego Ruiz',
    'depends': ['product','hr', 'hr_recruitment'],
    'description': """
Extension de Funcionalidades y definicion de campos customizados para la adaptacion de Odoo a la 
operatoria. Afecta a los modulos de Productos y RRHH
    """,
    'data': [
        'views/candidatos_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
