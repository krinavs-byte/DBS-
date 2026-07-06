# DBS-# Odoo Warehouse Dashboard

A simplified warehouse operations dashboard built on top of Odoo's XML-RPC API. This project addresses a documented usability gap in Odoo's interface: operational staff such as warehouse workers are currently presented with the same administrative interface as system managers, which introduces unnecessary complexity into routine daily tasks.

This prototype replaces that experience with a focused, single-purpose dashboard that surfaces only what a warehouse-floor user needs.

---

## The Problem

Odoo is a widely used ERP platform with a shared database architecture that integrates sales, inventory, accounting, and warehouse operations. Its underlying data model is sound. However, independent user reviews consistently identify that warehouse workflows require excessive navigation and too many clicks to complete routine actions (G2, 2026; Trustpilot, 2026). Warehouse staff do not need access to accounting configurations, CRM pipelines, or HR records. Presenting those options alongside daily operational tasks slows down work and increases the likelihood of error.

## The Solution

A role-specific web dashboard that connects to a live Odoo instance via its XML-RPC API and presents three focused panels:

- **Stock levels** — current on-hand quantities across all warehouse locations
- **Pending transfers** — outgoing and internal transfers awaiting action, prioritized by scheduled date
- **Low-stock alerts** — products that have fallen below their configured reorder threshold

No Odoo login is required for warehouse staff. The dashboard reads directly from the API using a service account, presenting data in a clear, uncluttered layout.

---

## Project Structure

```
odoo-warehouse-dashboard/
├── app.py                  # Flask application entry point
├── odoo_client.py          # XML-RPC connection and API call functions
├── requirements.txt        # Python dependencies
├── .env.example            # Environment variable template (copy to .env)
├── templates/
│   └── dashboard.html      # Main dashboard template
├── static/
│   ├── style.css           # Dashboard styles
│   └── script.js           # Frontend refresh and interactivity logic
└── README.md
```

---

## Prerequisites

- Python 3.9 or higher
- A running Odoo instance (self-hosted or Odoo.com demo account)
- An Odoo user account with read access to the Inventory and Stock modules

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-org/odoo-warehouse-dashboard.git
cd odoo-warehouse-dashboard
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your environment variables

Copy the example file and fill in your Odoo credentials:

```bash
cp .env.example .env
```

Open `.env` and set the following values:

```
ODOO_URL=https://your-odoo-instance.odoo.com
ODOO_DB=your-database-name
ODOO_USERNAME=your-login-email
ODOO_PASSWORD=your-api-key-or-password
```

> **Note:** For Odoo.com hosted instances, use an API key rather than your account password. Generate one under Settings → Technical → API Keys.

### 5. Run the application

```bash
python app.py
```

Open your browser at `http://localhost:5000`.

---

## How It Works

The dashboard uses Odoo's XML-RPC interface, which is part of Odoo's public API and requires no additional plugins or modifications to your Odoo instance.

On each page load, the Flask backend makes three API calls:

| Panel | Odoo Model | Fields Fetched |
|---|---|---|
| Stock levels | `stock.quant` | `product_id`, `quantity`, `location_id` |
| Pending transfers | `stock.picking` | `name`, `scheduled_date`, `state`, `picking_type_id` |
| Low-stock alerts | `stock.warehouse.orderpoint` | `product_id`, `qty_on_hand`, `product_min_qty` |

Results are passed to the HTML template and rendered without a page framework or JavaScript build step.

---

## Development Notes

- The `odoo_client.py` module handles all API communication. If you need to add a new data panel, add a function there and call it from `app.py`.
- All credentials are read from environment variables. Never commit your `.env` file.
- The dashboard does not write any data back to Odoo. It is read-only by design.

---

## Team

Built as a course project for [Course Name], [University Name].

| Member | Responsibility |
|---|---|
| [Name] | Project lead, report, documentation |
| [Name] | Odoo API integration, Flask backend |
| [Name] | HTML/CSS dashboard frontend |
| [Name] | Data logic, low-stock thresholds, testing |

---

## References

- Bista Solutions. (2022). *Odoo modules: The complete list of Odoo modules.* https://www.bistasolutions.com/resources/blogs/odoo-modules-list/
- G2. (2026). *Odoo ERP reviews 2026.* https://www.g2.com/products/odoo-odoo-erp/reviews
- Odoo. (2025). *Odoo XML-RPC external API documentation.* https://www.odoo.com/documentation/17.0/developer/reference/external_api.html
- Trustpilot. (2026). *Odoo reviews.* https://www.trustpilot.com/review/odoo.com
