# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Pos Folio',
    'version': '10.0.0.1',
    'category': 'Point Of Sale',
    'sequence': 6,
    'summary': 'Touchscreen Interface for Shops',
    'author': 'Serpent Consulting Services Pvt. Ltd',
    'website': 'http://www.serpentcs.com',
    'installable': True,
    'application': True,
    'depends': ['hotel', 'pos_order_for_restaurant'],
    'data':[
            'view/pos_folio_view.xml',
            'view/templates.xml',
           ],
    'qweb': ['static/src/xml/*.xml'],
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
