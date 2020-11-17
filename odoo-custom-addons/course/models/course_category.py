

from odoo import models, fields, api


class CourseCategory(models.Model):
    _name = 'bimo.course.category'
    _description = 'Model for Course Category'

    name = fields.Char(
        string="Course category Name",
        required=True,
        help="Fill course category name"
    )

    description = fields.Text(
        string="Course category Description",
        required=True,
        help="Fill course category description"
    )

    active = fields.Boolean(
        string="Active",
        default=True,
    )

    course_ids = fields.One2many(comodel_name="bimo.course",
                                    inverse_name="category_id",
                                    string="Lists Course",
                                    required=True, )

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
