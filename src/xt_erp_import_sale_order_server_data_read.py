"""Example xt_erp_import_sale_order_server_data_read."""

import json

from odoo.res_connection import OdooConnection
from config import TEST_SERVER_ACCESS_CONFIG


def main():
    odoo = OdooConnection(**TEST_SERVER_ACCESS_CONFIG).odoo

    vals = odoo.env['jap.import.sale.order.from.ext.odoo'].search_read(
        [],
        fields=[
            'id', 'url', 'dbname', 'username', 'proxy_host', 'proxy_port'],
        order='id desc',
        )

    vals_json = json.dumps(vals, indent=4)
    print(vals_json)


if __name__ == '__main__':
    main()
