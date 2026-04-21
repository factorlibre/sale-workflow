# Copyright Komit <http://komit-consulting.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


def _build_patched_onchange():
    @api.onchange("product_uom_qty", "product_uom", "route_id")
    def _onchange_product_id_check_availability(self):
        if (
            self.product_id
            and not self.product_id.product_tmpl_id._check_stock_on_sale()
        ):
            return {}
        return _onchange_product_id_check_availability.origin(self)
    return _onchange_product_id_check_availability


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    def _register_hook(self):
        self.env[self._name]._patch_method(
            "_onchange_product_id_check_availability",
            _build_patched_onchange(),
        )
        return super()._register_hook()
