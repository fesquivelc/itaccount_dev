# coding=utf-8
from odoo import fields, models, api


class AccountUpdate(models.AbstractModel):
    _name = 'account.update.it'

    catalog01_id = fields.Many2one('einvoice.catalog.01', u'Documento', required=True)
    serial_number = fields.Char(u'Serie', size=4, required=True)
    state = fields.Char(u'Estado', size=1, required=True)
    journal_id = fields.Many2one('account.journal', u'Libro', required=True)
    date_start = fields.Date(u'Fecha de inicio', required=True)
    date_end = fields.Date(u'Fecha de fin', required=True)

    @api.onchange('serial_number')
    def onchange_serial_number(self):
        for update in self:
            serial_number = '{:0>4}'.format(update.serial_number)
            update.serial_number = serial_number
