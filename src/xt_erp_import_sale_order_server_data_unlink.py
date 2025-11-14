"""Example xt_erp_import_sale_order_server_data_unlink."""

from odoo.res_connection import OdooConnection
from config import TEST_SERVER_ACCESS_CONFIG


def main():
    odoo = OdooConnection(**TEST_SERVER_ACCESS_CONFIG).odoo

    record_ids = odoo.env['jap.import.sale.order.from.ext.odoo'].search(
        domain=[],
        order='id desc',
        )

    if not record_ids:
        print("No records found")
        return

    odoo.env['jap.import.sale.order.from.ext.odoo'].unlink(
        record_ids,
        )


if __name__ == '__main__':
    main()
