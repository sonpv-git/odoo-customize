from odoo import api, fields, models


class ConfigWordSlip(models.Model):
    _name = 'config.word.slip'

    name = fields.Char("Tên đơn từ")
    paid = fields.Boolean("Tính tiền", default=False)
    date = fields.Boolean("Hiển thị từ ngày đến ngày", default=False)
    description = fields.Text("Lý do")
