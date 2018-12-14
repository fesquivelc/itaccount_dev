# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _

_logger = logging.getLogger(__name__)


class AccountUpdateWizard(models.TransientModel):
    _name = 'account.update.wizard'

    def _get_sale_data(self):
        if self._context['active_model'] == 'account.sale.update.it':
            return [(6, False, self._context.get('active_ids', []))]

    # cash_update_ids = fields.Many2many('account.cash.update.it', 'rel_update_wizard_account_cash_update', default=_get_cash_data)
    sale_update_ids = fields.Many2many('account.sale.update.it', 'rel_update_wizard_account_sale_update', default=_get_sale_data)
    journal_id = fields.Many2one('account.journal', u'Libro', required=True)

    @api.multi
    def do_update(self):
        for wizard in self:
            # if wizard.cash_update_ids:
            #     wizard.cash_update_ids.do_update(wizard.journal_id.id)
            if wizard.sale_update_ids:
                wizard.sale_update_ids.do_update(wizard.journal_id.id)
