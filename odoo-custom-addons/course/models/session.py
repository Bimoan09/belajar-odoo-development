

from odoo import models, fields, api, exceptions
from odoo.exceptions import ValidationError


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
    taken_seats = fields.Float(string="Taken seats",
                               compute="_compute_taken_seats",
                               store=True,
                               required=False,)

    @api.depends('min_attendee', 'attendee_ids')
    def _compute_taken_seats(self):
        for record in self:
            if not record.min_attendee:
                 record.taken_seats = 0.0
            else:
                 record.taken_seats = 100.0 * len(record.attendee_ids) / record.min_attendee

    @api.onchange('min_attendee', 'attendee_ids')
    def onchange_attendee(self):
        if self.min_attendee < 0:
            return {
                'warning': {
                    'title': "Data is wrong!",
                    'message': "Min Attendee must not be less than 0",
                },
            }
        if self.min_attendee < len(self.attendee_ids):
            return {
                'warning': {
                    'title': "Too many attendees",
                    'message': "Increase attendee or remove excess attendees",
                },
            }



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

