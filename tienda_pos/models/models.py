# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    x_reordenar = fields.Boolean(compute='_get_is_low_stock',
                                              string="Stock Bajo",
                                              store=True)

    @api.depends('qty_available','reordering_min_qty','virtual_available')
    def _get_is_low_stock(self):
        for r in self:
            if r.qty_available < r.reordering_min_qty:
                if r.qty_available == r.virtual_available:
                    r['x_reordenar'] = True
                else:
                    r['x_reordenar'] = False
            else:
                r['x_reordenar'] = False
