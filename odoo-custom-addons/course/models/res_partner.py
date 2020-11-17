

from odoo import models, fields, api


class Partner(models.Model):
    _inherit = 'res.partner'

    name = fields.Char(string="Name")
    is_student = fields.Boolean(string="Student",
                                default=False
                                )
    is_instructor = fields.Boolean(string="Instructor",
                                   default=False
                                   )