import csv
from pathlib import Path

from app import detect_upload_type, map_stock_columns, map_sales_columns


def run_case(label, path, kind):
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []
        rows = list(reader)
    print(f'CASE={label}')
    print(f'HEADERS={headers}')
    print(f'TYPE={detect_upload_type(headers)}')
    if kind == 'stock':
        print(f'MATCHED={map_stock_columns(rows, headers)}')
    else:
        print(f'MATCHED={map_sales_columns(headers)}')
    print('---')

run_case('inventory_real', 'SAMPLE_DATA/bloom_and_batter_bakery_data/inventory.csv', 'stock')
run_case('sample_stock', 'sample_stock.csv', 'stock')
run_case('sample_sales', 'sample_sales.csv', 'sales')
print('BAD_TYPE=', detect_upload_type(['Foo', 'Bar', 'Baz']))
