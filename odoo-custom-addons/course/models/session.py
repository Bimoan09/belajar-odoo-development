

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
                                   default=fields.Datetime.now(),
                                   required=True,
                                   )
    min_attendee = fields.Integer(string="Minimal Attendee",
                                  required=True,
                                  )

    attendee_ids = fields.One2many(comodel_name="bimo.attendee",
                                   inverse_name="session_id",
                                   string="Attendee",
                                   required=False, )


    class Attendee(models.Model):
        _name = 'bimo.attendee'
        _description = 'Data Course Attendee'

        name = fields.Integer(string="Registration Number",
                           required=True,
                           )
        student_id = fields.Many2one(comodel_name="res.partner",
                                    string="Attendee",
                                    domain="[('is_student', '=', True)]",
                                    required=True, )
        reg_date = fields.Datetime(string="Registration date",
                                   default=fields.Datetime.now(),
                                   required=True, )
        session_id = fields.Many2one(comodel_name="bimo.session",
                                     string="Session",
                                     required=True, )
        remark = fields.Char(string="Note", required=False, )

