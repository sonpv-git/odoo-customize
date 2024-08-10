from odoo import api, fields, models


class ConfigShift(models.Model):
    _name = 'config.shift'

    name = fields.Char("Tên ca")
