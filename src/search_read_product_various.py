"""Example search_read_product_various."""
__author__ = 'Joan A. Pinol  (japinol)'

from odoo.res_connection import OdooConnection
from config import TEST_SERVER_ACCESS_CONFIG


def get_odoo_client():
    return OdooConnection(**TEST_SERVER_ACCESS_CONFIG).odoo


def get_sale_product(odoo, min_price, max_price):
    products_vals = odoo.env['product.template'].search_read([
        ('sale_ok', '=', True),
        ('list_price', '>=', min_price),
        ('list_price', '<=', max_price),
        ],
        fields=['name'],
        order='id desc',
        limit=1,
        )
    return products_vals and products_vals[0]['name'] or None


def get_product_price(odoo, product_name):
    products_vals = odoo.env['product.template'].search_read([
        ('name', '=', product_name),
        ],
        fields=['name', 'list_price'],
        order='id desc',
        limit=1,
        )
    return products_vals and products_vals[0]['list_price'] or None


def main():
    odoo = get_odoo_client()
    min_price, max_price = 160, 2_000
    product_name = get_sale_product(odoo, min_price, max_price)

    if not product_name:
        print(f"No sale product found with price "
              f"between {min_price} and {max_price}")
        return

    product_price = get_product_price(odoo, product_name)
    print(f"Product name: {product_name}, product price: {product_price}")


if __name__ == '__main__':
    main()
