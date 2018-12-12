# coding=utf-8

from odoo import fields, models, api


class AccountCashUpdate(models.Model):
    _name = 'account.cash.update.it'
    _inherit = 'account.update.it'
    _rec_name = 'account10_id'

    account10_id = fields.Many2one('account.account', u'Cuenta 10', required=True)
    account12_id = fields.Many2one('account.account', u'Cuenta 12', required=True)

    @api.multi
    def do_update(self):
        sql12_template = """
            UPDATE account_move_line 
            SET account_id='{}' WHERE id IN 
            (
                SELECT move_line.id 
                FROM account_move_line move_line
                    INNER JOIN account_invoice inv ON move_line.invoice_id = inv.id
                    LEFT JOIN account_move move ON move.id=move_line.move_id
                    LEFT JOIN account_account account ON account.id=move_line.account_id
                WHERE 
                    move.journal_id='{}'
                    AND  
                    LEFT(account.code,2)='12'                    
                    AND move.fecha_contable BETWEEN '{}' AND '{}'
                    AND move_line.ref LIKE '{}%'
                    AND move_line.name LIKE '{}'
                    AND inv.it_type_document = '{}'
            )
            """
        sql10_template = """
            UPDATE account_move_line 
            SET account_id='{}' WHERE id IN 
            (
                SELECT move_line.id 
                FROM account_move_line move_line
                    INNER JOIN account_invoice inv ON move_line.invoice_id = inv.id
                    LEFT JOIN account_move move ON move.id=move_line.move_id
                    LEFT JOIN account_account account ON account.id=move_line.account_id
                WHERE 
                    move.journal_id='{}'
                    AND  
                    LEFT(account.code,2)='10'                 
                    AND move.fecha_contable BETWEEN '{}' AND '{}'
                    AND move_line.ref LIKE '{}%'
                    AND move_line.name LIKE '{}'
                    AND inv.it_type_document = '{}'
            )
        """
        for update in self:
            sql12 = sql12_template.format(update.account12_id.id,
                                          update.journal_id.id,
                                          update.date_start,
                                          update.date_end,
                                          update.serial_number,
                                          update.state,
                                          update.catalog01_id.id
                                          )
            sql10 = sql10_template.format(update.account10_id.id,
                                          update.journal_id.id,
                                          update.date_start,
                                          update.date_end,
                                          update.serial_number,
                                          update.state,
                                          update.catalog01_id.id
                                          )
            self.env.cr.execute(sql12)
            self.env.cr.execute(sql10)
            self.env.cr.commit()
