# -*- coding: utf-8 -*-
{
    'name': 'Đơn từ Sơn Hà',
    'version': '1.7',
    'category': 'Word Slip',
    'summary': 'Đơn từ Sơn Hà',
    'website': 'https://',
    'description': "Đơn từ Sơn Hà",
    'depends': ['base', 'hr', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/config_word_slip_views.xml',
        'views/word_slip_views.xml',
        'views/form_word_slip_views.xml',
        'views/config_shift_views.xml',
        'views/register_shift_rel_views.xml',
        'views/register_shift_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
