STOCK_LEVELS = [
    {"product": "Corner Protectors", "sku": "CP-001", "location": "Main WH", "qty": 5, "min_qty": 50},
    {"product": "Industrial Cable Ties", "sku": "CT-204", "location": "Main WH", "qty": 82, "min_qty": 80},
    {"product": "Safety Gloves", "sku": "SG-015", "location": "North Hub", "qty": 12, "min_qty": 40},
    {"product": "Packaging Tape", "sku": "PT-110", "location": "East DC", "qty": 0, "min_qty": 28},
    {"product": "Thermal Labels", "sku": "TL-409", "location": "Main WH", "qty": 18, "min_qty": 24},
    {"product": "Battery Packs", "sku": "BP-330", "location": "South Hub", "qty": 46, "min_qty": 50},
    {"product": "Machine Oil 5L", "sku": "MO-099", "location": "Main WH", "qty": 74, "min_qty": 60},
    {"product": "Hex Bolts M8", "sku": "HB-812", "location": "West Yard", "qty": 8, "min_qty": 35},
    {"product": "Workstation Chairs", "sku": "WC-521", "location": "HQ", "qty": 21, "min_qty": 18},
    {"product": "A4 Print Paper", "sku": "PP-119", "location": "Office Store", "qty": 140, "min_qty": 100},
    {"product": "Scanner Cartridges", "sku": "SC-220", "location": "IT Cabinet", "qty": 4, "min_qty": 20},
    {"product": "Forklift Filters", "sku": "FF-442", "location": "Plant 2", "qty": 7, "min_qty": 24},
    {"product": "Adhesive Foam Pads", "sku": "AF-700", "location": "Main WH", "qty": 60, "min_qty": 55},
    {"product": "Warehouse Bins", "sku": "WB-062", "location": "North Hub", "qty": 16, "min_qty": 18},
    {"product": "Laser Sensor Units", "sku": "LS-505", "location": "Plant 1", "qty": 31, "min_qty": 30},
]

TRANSFERS = [
    {"ref": "TR-1048", "due": "2026-09-14", "state": "pending", "type": "Inbound", "assigned_to": "Asha"},
    {"ref": "TR-1049", "due": "2026-09-14", "state": "in_transit", "type": "Outbound", "assigned_to": "Nikhil"},
    {"ref": "TR-1050", "due": "2026-09-15", "state": "pending", "type": "Transfer", "assigned_to": "Mira"},
    {"ref": "TR-1051", "due": "2026-09-16", "state": "complete", "type": "Inbound", "assigned_to": "Daniel"},
    {"ref": "TR-1052", "due": "2026-09-14", "state": "awaiting_review", "type": "Outbound", "assigned_to": "Asha"},
    {"ref": "TR-1053", "due": "2026-09-17", "state": "complete", "type": "Transfer", "assigned_to": "Lena"},
    {"ref": "TR-1054", "due": "2026-09-18", "state": "pending", "type": "Inbound", "assigned_to": "Nikhil"},
]

CUSTOMERS = [
    {"name": "Arjun Patel", "email": "arjun.patel@northline.co", "orders": 18, "spent": 245000, "status": "active", "segment": "Enterprise"},
    {"name": "Sofia Raman", "email": "sofia@luminaretail.com", "orders": 9, "spent": 181000, "status": "active", "segment": "Retail"},
    {"name": "Bright Retail Ltd.", "email": "hello@brightretail.com", "orders": 25, "spent": 675000, "status": "vip", "segment": "Retail"},
    {"name": "GreenMart", "email": "sales@greenmart.in", "orders": 14, "spent": 331000, "status": "active", "segment": "Wholesale"},
    {"name": "Tech Corner", "email": "service@techcorner.io", "orders": 11, "spent": 155000, "status": "at_risk", "segment": "SMB"},
    {"name": "Aster Foods", "email": "ops@asterfoods.com", "orders": 22, "spent": 412000, "status": "active", "segment": "Food"},
    {"name": "Harbor Supply Co.", "email": "team@harborsupply.com", "orders": 6, "spent": 96000, "status": "new", "segment": "Industrial"},
]

SALES_ORDERS = [
    {"ref": "SO-2041", "customer": "Bright Retail Ltd.", "amount": 75600, "status": "Paid", "date": "2026-09-10", "items": 12},
    {"ref": "SO-2042", "customer": "Aster Foods", "amount": 53200, "status": "Paid", "date": "2026-09-11", "items": 8},
    {"ref": "SO-2043", "customer": "GreenMart", "amount": 42100, "status": "Pending", "date": "2026-09-12", "items": 6},
    {"ref": "SO-2044", "customer": "Arjun Patel", "amount": 89000, "status": "Paid", "date": "2026-09-13", "items": 15},
    {"ref": "SO-2045", "customer": "Tech Corner", "amount": 24600, "status": "Review", "date": "2026-09-13", "items": 4},
    {"ref": "SO-2046", "customer": "Sofia Raman", "amount": 31500, "status": "Paid", "date": "2026-09-14", "items": 5},
]

TEAM = [
    {"name": "Ananya Sharma", "email": "ananya@jodoo.com", "department": "Marketing", "role": "Growth Lead", "status": "active"},
    {"name": "Rahul Mehra", "email": "rahul@jodoo.com", "department": "Sales", "role": "Account Manager", "status": "active"},
    {"name": "Sneha Iyer", "email": "sneha@jodoo.com", "department": "Finance", "role": "Controller", "status": "on_leave"},
    {"name": "Nikhil Rao", "email": "nikhil@jodoo.com", "department": "Operations", "role": "Warehouse Lead", "status": "active"},
    {"name": "Leah Gomez", "email": "leah@jodoo.com", "department": "Support", "role": "Customer Success", "status": "active"},
    {"name": "Daniel Chen", "email": "daniel@jodoo.com", "department": "IT", "role": "System Admin", "status": "active"},
]

NETWORK_POSTS = [
    {"author": "EcoPack Solutions", "role": "Sustainability Partner", "content": "We provide sustainable packaging solutions for businesses of all sizes. Let's build a greener tomorrow, together. 🌱", "likes": 24, "timestamp": "2h ago"},
    {"author": "TechHub India", "role": "Hiring Partner", "content": "Hiring: Full Stack Developer (React + Node.js). Join our team and help us build the future of business automation!", "likes": 15, "timestamp": "4h ago"},
    {"author": "LogiFast Services", "role": "Logistics Partner", "content": "We help retailers reduce last-mile delivery delays with smarter fulfillment workflows.", "likes": 31, "timestamp": "6h ago"},
    {"author": "DesignCraft Studio", "role": "Brand Studio", "content": "Brand refresh packages now include AI-generated creative concepts and storefront optimization support.", "likes": 18, "timestamp": "1d ago"},
]
