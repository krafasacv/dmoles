# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    x_reordenar = fields.Boolean(compute='_get_is_low_stock',
                                              string="Stock Bajo",
                                              store=True)

    @api.depends('qty_available','reordering_min_qty')
    def _get_is_low_stock(self):
        for r in self:
            if r.qty_available < r.reordering_min_qty:
                r['x_reordenar'] = True
