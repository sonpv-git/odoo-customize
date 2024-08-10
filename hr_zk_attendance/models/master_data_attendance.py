from odoo import models, fields

class MasterDataAttendance(models.Model):
    _name = 'master.data.attendance'
    _description = 'Master Data Attendance'

    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    attendance_time = fields.Datetime(string='Attendance Time', required=True)
