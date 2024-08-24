from odoo import api, fields, models, _ # type: ignore
from odoo.exceptions import UserError, ValidationError # type: ignore


class SonHaEmployee(models.Model):
    _inherit = 'hr.employee'

    list_employee = fields.Many2many('hr.employee', 'ir_employee_group_rel',
                                     'employee_group_rel', 'employee_rel',
                                     string='List Staff')

    lower_grade = fields.Many2many('hr.employee', 'ir_lower_grade_id_rel',
                                   'lower_grade_id_rel', 'lower_grade_id',
                                    string="Lower Grade")

    kpi = fields.Many2many('hr.employee', 'ir_kpi_id_rel',
                           'kpi_id_rel', 'kpi_id',
                           string="Edit KPI")

    department_ids = fields.Many2many('hr.department', 'ir_department_ids_rel',
                                      'department_ids_rel', 'department_ids',
                                      string="Department")

    level = fields.Selection([
        ('N0', 'N0'),
        ('N1', 'N1'),
        ('N2', 'N2'),
        ('N3', 'N3'),
        ('N4', 'N4'),
        ('N5', 'N5'),
    ], string='Level')

    date = fields.Date('Ngày')
    number = fields.Integer('Số')
    status_employee = fields.Selection([
        ('working', "Đang làm việc"),
        ('maternity_leave', "Nghỉ thai sản"),
        ('quit_job', 'Nghỉ việc'),
        ('trial', 'Thử việc')
    ], string='Trạng thái làm việc')

    # các field page hr setting
    onboard = fields.Date('Ngày vào công ty')
    type_contract = fields.Many2one('hr.contract', "Loại hợp đồng")
    employee_code = fields.Char("Mã nhân viên")

    # các field page infomation page 1



   # các field page private infomation page 2
    number_cccd = fields.Char("Số CCCD")
    date_cccd = fields.Date("Ngày cấp")
    place_of_issue = fields.Char("Nơi cấp")
    passport_number = fields.Char("Số hộ chiếu")
    date_passport = fields.Date("Ngày hộ chiếu")
    expiration_date_passport = fields.Date("Ngày hết hạn")
    place_of_issue_passport = fields.Char("Nơi cấp hộ chiếu")
    number_visa = fields.Char("Số visa")
    date_visa = fields.Date("Ngày cấp(visa)")
    expiration_date_visa = fields.Date("Ngày hết hạn(visa)")
    place_of_issue_visa = fields.Char("Nơi cấp(visa)")
    reunion_day = fields.Date("Ngày vào Đoàn")
    place_reunion = fields.Char("Nơi vào(Đoàn)")
    fee_reunion = fields.Boolean("Đoàn phí")
    party_member_day = fields.Date("Ngày vào Đảng")
    place_party_member = fields.Char("Nơi vào Đảng")
    fee_party_member = fields.Boolean("Đảng phí")

    # @api.onchange('list_employee')
    # def _onchange_list_employee(self):
    #     if self.list_employee:
    #         return {'domain': {'kpi': [('id', 'in', self.list_employee.ids)]}}
    #     else:
    #         self.filter_list_employee()
    #         return {'domain': {'kpi': []}}
    #
    # @api.onchange('list_employee')
    # def filter_list_employee(self):
    #     for r in self:
    #         if len(r.lower_grade) > 0:
    #             list_emp = []
    #             for item in r.lower_grade:
    #                 list_emp.append(item.id)
    #                 list_emp.append(item.list_employee.ids)
    #             flattened_list = [item for sublist in list_emp for item in
    #                               (sublist if isinstance(sublist, list) else [sublist])]
    #             r.list_employee = flattened_list
    #         else:
    #             r.list_employee = None