#    Author: Rafael Valle
#    Author: Zahra Velasco
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp.tests.common import TransactionCase


class TestSaleOrderAddVariants(TransactionCase):

    def setUp(self):
        super(TestSaleOrderAddVariants, self).setUp()
        self.partner = self.env['res.partner'].create({
            'name': 'Cliente prueba',
        })
        self.product = self.env['product.template'].create({
            'name': 'Producto 1',
            'type': 'consu',
            'categ_id': 1,
            'lst_price': 10

        })
        self.variant1 = self.env['product.product'].create({
            'name': 'Variante 1',
            'type': 'consu',
            'categ_id': 1,
            'product_tmpl_id': self.product.id
        })

        sale_add_variants_env = self.env['sale.add.variants']
        sale_order_env = self.env['sale.order']

        self.sale_order = sale_order_env.create({
            'partner_id': self.partner.id
        })
        self.sale_add_variants = sale_add_variants_env.with_context({
            'active_model': 'sale.order',
            'active_ids': [self.sale_order.id],
            'active_id': self.sale_order.id
        }).create({
            'product_tmpl_id': self.product.id
        })
        self.sale_add_variants._onchange_product_tmpl_id()

    def test_number_lines_into_order(self):
        self.sale_add_variants.variant_line_ids[0].product_uom_qty = 5
        self.sale_add_variants.add_to_order()
        self.assertEqual(
            len(self.sale_order.order_line),
            1,
            "Order lines number not match"
        )

    def test_amount_order(self):
        self.sale_add_variants.variant_line_ids[0].product_uom_qty = 10
        self.sale_add_variants.add_to_order()
        self.assertEqual(
            self.sale_order.amount_untaxed,
            100,
            "Order amount is not correct"
        )
