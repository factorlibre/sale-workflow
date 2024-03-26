# Copyright 2017 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    def _get_order_lines_by_invoice_policy(self, invoice_policy):
        so_lines = self.filtered(
            lambda x, p=invoice_policy: x.order_id.invoice_policy == p
        ).with_prefetch()
        return so_lines

    def _set_invoice_policy_on_product_templates(self, invoice_policy):
        product_templates = self.mapped("product_template_id").filtered(
            lambda p: p.invoice_policy != invoice_policy
            and p.detailed_type != "service"
        )
        if product_templates:
            product_templates.write({"invoice_policy": invoice_policy})

    @api.depends(
        "qty_invoiced",
        "qty_delivered",
        "product_uom_qty",
        "state",
        "order_id.invoice_policy",
    )
    def _compute_qty_to_invoice(self):
        invoice_policies = set(self.mapped("order_id.invoice_policy"))
        line_by_id = {line.id: line for line in self}
        done_lines = self.env["sale.order.line"]
        for invoice_policy in invoice_policies:
            so_lines = self._get_order_lines_by_invoice_policy(invoice_policy)
            so_lines._set_invoice_policy_on_product_templates(invoice_policy)
            if so_lines:
                done_lines |= so_lines
                super(SaleOrderLine, so_lines)._compute_qty_to_invoice()
                for line in so_lines:
                    # due to the change of context in compute methods,
                    # assign the value in the modified context to self
                    line_by_id[line.id].qty_to_invoice = line.qty_to_invoice
        # Not to break function if (it could not happen) some records
        # were not in so_lines
        super(SaleOrderLine, self - done_lines)._compute_qty_to_invoice()
        return True

    @api.depends(
        "state",
        "product_uom_qty",
        "qty_delivered",
        "qty_to_invoice",
        "qty_invoiced",
        "order_id.invoice_policy",
    )
    def _compute_invoice_status(self):
        invoice_policies = set(self.mapped("order_id.invoice_policy"))
        line_by_id = {line.id: line for line in self}
        done_lines = self.env["sale.order.line"]
        for invoice_policy in invoice_policies:
            so_lines = self._get_order_lines_by_invoice_policy(invoice_policy)
            so_lines._set_invoice_policy_on_product_templates(invoice_policy)
            done_lines |= so_lines
            if so_lines:
                super(SaleOrderLine, so_lines)._compute_invoice_status()
                for line in so_lines:
                    # due to the change of context in compute methods,
                    # assign the value in the modified context to self
                    line_by_id[line.id].invoice_status = line.invoice_status
        # Not to break function if (it could not happen) some records
        # were not in so_lines
        super(SaleOrderLine, self - done_lines)._compute_invoice_status()
        return True
