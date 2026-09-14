from io import BytesIO
from app import app

app.config['TESTING'] = True
client = app.test_client()

stock_csv = b"Product,SKU,Location,Qty,Min_Qty\nWidget A,WA-100,Main WH,12,5\nWidget B,WB-200,North Hub,7,3\n"
stock_resp = client.post(
    '/upload-data',
    data={'stock_csv': (BytesIO(stock_csv), 'stock.csv')},
    content_type='multipart/form-data'
)
print('STOCK_STATUS', stock_resp.status_code)
with client.session_transaction() as sess:
    print('STOCK_SESSION_LEN', len(sess.get('uploaded_stock', [])))

sales_csv = b"Transaction ID,Item,Quantity,Price Per Unit,Total Spent,Payment Method,Location,Transaction Date\nTXN-1001,Widget A,2,15.00,30.00,Card,Main WH,2026-09-14\nTXN-1002,Widget B,1,25.00,25.00,Cash,North Hub,2026-09-14\n"
sales_resp = client.post(
    '/upload-data',
    data={'stock_csv': (BytesIO(sales_csv), 'sales.csv')},
    content_type='multipart/form-data'
)
print('SALES_STATUS', sales_resp.status_code)
with client.session_transaction() as sess:
    print('SALES_SESSION_LEN', len(sess.get('uploaded_sales', [])))
    print('SALES_SESSION_SAMPLE', sess.get('uploaded_sales', [])[:2])

sales_page = client.get('/app/sales')
print('SALES_PAGE_HAS_TXN', 'TXN-1001' in sales_page.get_data(as_text=True))
analytics_page = client.get('/app/analytics')
html = analytics_page.get_data(as_text=True)
print('ANALYTICS_HAS_55', '55.00' in html or '₹55' in html)
print('ANALYTICS_HAS_2_ORDERS', '2' in html)

invalid_csv = b"Foo,Bar,Baz\n1,2,3\n"
invalid_resp = client.post(
    '/upload-data',
    data={'stock_csv': (BytesIO(invalid_csv), 'bad.csv')},
    content_type='multipart/form-data'
)
print('INVALID_STATUS', invalid_resp.status_code)
print('INVALID_BODY', invalid_resp.get_data(as_text=True)[:200])
