# © 2023 - FactorLibre - Oscar Indias <oscar.indias@factorlibre.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

def pre_init_hook(cr):
    cr.execute(
        """ALTER TABLE sale_order
        ADD COLUMN IF NOT EXISTS invoiced_amount numeric DEFAULT 0.0"""
    )

    cr.execute(
        """ALTER TABLE sale_order_line
        ADD COLUMN IF NOT EXISTS uninvoiced_amount numeric DEFAULT 0.0"""
    )
