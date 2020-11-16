

from odoo import models, fields, api


class Course(models.Model):
    _name = 'bimo.course'
    _description = 'Model for Course'

    name = fields.Char(
        string="Course Name",
        required=True,
        help="Fill course name"
    )
    # value = fields.Integer()
    author = fields.Char(
        string="Course Author",
        required=True,
        help="Fill course author"
    )
    description = fields.Text(
        string="Course Description",
        required=True,
        help="Fill course description"
    )

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
