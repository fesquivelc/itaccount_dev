# coding=utf-8

from odoo import fields, api, models


class CurrencyName(models.Model):
    _inherit = 'account_currency_name_it.currency_name'

    account_id = fields.Many2one('account.account', u'Cuenta asociada')
