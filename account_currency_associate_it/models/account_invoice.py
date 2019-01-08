# coding=utf-8

from odoo import fields, api, models


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.depends('partner_id')
    @api.onchange('currency_id')
    def onchange_currency_id(self):
        if self.currency_id:
            account_id = self.env['account_currency_name_it.currency_name'].search(
                [('currency_id', '=', self.currency_id.id)])

            if account_id:
                self.account_id = account_id
