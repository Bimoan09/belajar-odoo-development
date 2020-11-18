

from odoo import models, fields, api


class Session(models.Model):
    _name = 'bimo.session'
    _description = 'Data Course Session'

    name = fields.Char(string="name")
    course_id = fields.Many2one(comodel_name="bimo.course",
                                string="Course",
                                required=True, )
    instructor_id = fields.Many2one(comodel_name="res.partner",
                                    string="Instructor",
                                    domain="[('is_instructor', '=', True)]",
                                    required=True, )
    session_date = fields.Datetime(string="Session date",
                                   default=fields.Datetime.now()
                                   )
    min_attendee = fields.Integer(string="Minimal Attendee",
                                  required=True,
                                  )
