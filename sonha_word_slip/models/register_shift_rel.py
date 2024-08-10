from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class RegisterShiftRel(models.Model):
    _name = 'register.shift.rel'

    date = fields.Date("Ngày")
    shift = fields.Many2one('config.shift', string="Ca")
    register_shift = fields.Many2one('register.shift')

    @api.constrains('date')
    def validate_date(self):
        for r in self:
            if r.register_shift and r.register_shift.type_register == 'about_day' and r.register_shift.from_date and r.register_shift.to_date:
                if r.register_shift.from_date <= r.date <= r.register_shift.to_date:
                    pass
                else:
                    raise ValidationError(f"Bạn chỉ được chọn ngày trong khoảng {r.register_shift.from_date} đến {r.register_shift.to_date}")
