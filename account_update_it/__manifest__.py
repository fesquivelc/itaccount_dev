# -*- coding: utf-8 -*-
{
    'name': u"Actualización de cuentas ",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "ITGroup",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account_accountant', 'odoope_einvoice_base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/account_cash_update.xml',
        'views/account_sale_update.xml',
        'views/account_update_menus.xml',
        'wizard/account_update_wizard.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
