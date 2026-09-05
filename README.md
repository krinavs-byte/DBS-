<div align="center">

<img src="https://img.shields.io/badge/Jodo-Business%20Operations%20Platform-2E7BF6?style=for-the-badge&labelColor=0B1120" />
<br/><br/>
<img src="https://img.shields.io/badge/Python-Flask-0FBCB0?style=flat-square&logo=flask&logoColor=white&labelColor=0F1929" />
<img src="https://img.shields.io/badge/Frontend-HTML%20%2F%20CSS%20%2F%20JS-2E7BF6?style=flat-square&labelColor=0F1929" />
<img src="https://img.shields.io/badge/ERP-Odoo%20XML--RPC-0FBCB0?style=flat-square&labelColor=0F1929" />
<img src="https://img.shields.io/badge/AI-Agent%20Enabled-F59E0B?style=flat-square&labelColor=0F1929" />
<img src="https://img.shields.io/badge/Status-In%20Development-7B93B8?style=flat-square&labelColor=0F1929" />

<br/><br/>

<img src="JodooLogo.png" alt="Jodo Logo" />

### Not just another ERP dashboard.
### A role-specific, AI-assisted, fully customisable operations platform — built for every kind of business.

<br/>

</div>

---

## ⚡ The Problem with Odoo (and every ERP like it)

```
┌───────────────────────────────────────────────────────────────────[...]
│                  ODOO — full admin interface                      │
│                                                                  │
│  CRM │ Sales │ Accounting │ HR │ Manufacturing │ Helpdesk │ ...  │
│                                                                  │
│         ↕  every user, every role, sees ALL of this  ↕          │
│                                                                  │
│  Inventory │ Transfers │ Payroll │ POS │ Marketing │ Repairs ... │
└───────────────────────────────────────────────────────────────────[...]

  A warehouse worker. A retail manager. A restaurant owner.
  A freelance agency. All given the same cluttered interface.
  All forced to navigate what they don't need to reach what they do.

                           ↓  Jodo fixes this  ↓

┌──────────────┬───────────────────┬────────────────────────────────[...]
│  Your role   │  Your dashboards  │  Your data — nothing extra   │
│  Your layout │  Your AI agent    │  Connected. Clean. Fast.     │
└──────────────┴───────────────────┴────────────────────────────────[...]
```

---

## 🎯 Who Is Jodo For?

```
                            ┌─────────────┐
                            │    JODO     │
                            │  Platform   │
                            └──────┬──────┘
           ┌──────────────┬────────┼────────┬──────────────┐
           ▼              ▼        ▼         ▼              ▼
    ┌────────────┐ ┌──────────┐ ┌──────┐ ┌──────────┐ ┌──────────┐
    │ Warehouse  │ │  Retail  │ │ Cafe │ │ Agency / │ │  Any SME │
    │ & Logistics│ │  Store   │ │  &   │ │Freelance │ │ that runs│
    │            │ │ Manager  │ │ Food │ │  Team    │ │ on Odoo  │
    └────────────┘ └──────────┘ └──────┘ └──────────┘ └──────────┘
    Stock levels   Sales today  Orders   Project       Custom
    Transfers      Inventory    Kitchen  pipeline      role view
    Reorder alerts POS summary  Staffing Invoices      AI agent
```

Each business type gets its own configured dashboard. No two Jodo setups need to look the same.

---

## ✨ Core Features

### 1 — Customisable Dashboards

```
┌─────────────────────────────────────────────────┐
│  Jodo Dashboard Builder                         │
│                                                 │
│  [ Stock Panel  ▓▓▓▓▓▓▓▓░░ ]  [ + Add panel ]  │
│  [ Transfers    ▓▓▓▓░░░░░░ ]                    │
│  [ Alerts       ▓▓▓▓▓▓░░░░ ]  drag to reorder  │
│                                                 │
│  Role: Warehouse Manager ▾                      │
│  Saved layouts: Morning view / Dispatch view    │
└─────────────────────────────────────────────────┘
```

Users can add, remove, and reorder panels. Layouts save per role and per user. A warehouse manager's morning view looks nothing like an accountant's closing view — and both are built from the same p[...]

---

### 2 — Team Networking (Discord-style)

```
┌─────────────────────────────────────────────┐
│  Jodo Workspace                             │
│                                             │
│  # general          ● Ravi (Warehouse)      │
│  # dispatch-alerts  ● Priya (Accounts)      │
│  # low-stock-watch  ○ Arjun (offline)       │
│                                             │
│  [🔴 ALERT] Corner Protectors — 5 units    │
│  Ravi: on it, reorder submitted             │
│  Priya: invoice raised ✓                   │
│                                             │
│  [ type a message...              ] [send]  │
└─────────────────────────────────────────────┘
```

Persistent, role-aware team channels embedded directly in the platform. Alerts from the dashboard post automatically into the relevant channel. No switching between Slack, WhatsApp, and the ERP.

---

### 3 — AI Operations Agent

```
┌──────────────────────────────────────────────┐
│  Jodo AI Agent                               │
│                                              │
│  You: "Which products are going to run out   │
│         before Friday based on current       │
│         transfer volume?"                    │
│                                              │
│  Agent: Based on today's pending transfers,  │
│  Corner Protectors (5 units, 3 outgoing)     │
│  and Air Pillows (0 units) will hit zero     │
│  before Friday. Shall I raise a reorder?     │
│                                              │
│  [ Yes, raise reorder ] [ Show me the data ] │
└──────────────────────────────────────────────┘
```

The AI agent reads live dashboard data and answers natural language questions about operations. It can flag patterns, suggest reorders, and summarise daily status — without the user building a singl[...]

---

## 🏗️ System Architecture

```mermaid
graph TB
    subgraph Client["🌐 Client — Browser"]
        UI[Jodo Dashboard\nHTML · CSS · JS]
        CHAT[Team Channels\nWebSocket]
        AGENT[AI Agent\nChat interface]
    end

    subgraph Backend["🐍 Flask Backend"]
        ROUTES[Routes\n/ · /api/stock · /api/transfers]
        LOGIC[Business Logic\nget_status · get_alerts · filters]
        WS[WebSocket Server\nreal-time messaging]
        AIMOD[AI Module\nquery parser · response builder]
    end

    subgraph Data["💾 Data Layer"]
        MOCK[mock_data.py\nPhase 1]
        ODOO[(Odoo Instance\nXML-RPC API\nPhase 2)]
    end

    UI -->|HTTP| ROUTES
    CHAT <-->|WebSocket| WS
    AGENT -->|query| AIMOD
    ROUTES --> LOGIC
    LOGIC --> MOCK
    MOCK -.->|swap in Phase 2| ODOO
    AIMOD --> LOGIC

    style Client fill:#0F1929,stroke:#2E7BF6,color:#E2EAF4
    style Backend fill:#0F1929,stroke:#0FBCB0,color:#E2EAF4
    style Data fill:#0F1929,stroke:#4A607A,color:#7B93B8
```

---

## 🔄 Request Flow — How a Dashboard Load Works

```mermaid
flowchart LR
    A([User opens Jodo]) --> B[Browser sends\nGET /]
    B --> C[Flask route\nreceives request]
    C --> D[Calls get_status\nfor every product]
    D --> E{qty vs min_qty}
    E -->|above| F[status: ok]
    E -->|below 100%| G[status: low]
    E -->|below 20%| H[status: critical]
    E -->|zero| I[status: out]
    F & G & H & I --> J[Calls get_alerts\nfilters and sorts by pct]
    J --> K[Passes all data\nto Jinja2 template]
    K --> L([Three panels\nrendered in browser])

    style A fill:#0B1120,stroke:#2E7BF6,color:#E2EAF4
    style L fill:#0B1120,stroke:#0FBCB0,color:#E2EAF4
    style E fill:#132038,stroke:#F59E0B,color:#E2EAF4
```

---

## 🧠 Low-Stock Alert Logic

```mermaid
flowchart TD
    START([Iterate all products]) --> CHK{qty < min_qty?}
    CHK -->|No| SKIP[Skip]
    CHK -->|Yes| PCT[pct = qty ÷ min_qty × 100]
    PCT --> ADD[Add to alerts\nwith pct field]
    ADD --> NEXT([Continue])
    SKIP --> NEXT
    NEXT --> ALL{All done?}
    ALL -->|No| START
    ALL -->|Yes| SORT[Sort ascending by pct\nmost urgent first]
    SORT --> SEV{pct < 20?}
    SEV -->|Yes| RED[🔴 Critical]
    SEV -->|No| AMB[🟡 Warning]
    RED & AMB --> OUT([Render in alerts panel])

    style RED fill:#2A0A0A,stroke:#EF4444,color:#F87171
    style AMB fill:#2A1F06,stroke:#F59E0B,color:#FCD34D
    style OUT fill:#0B1120,stroke:#0FBCB0,color:#E2EAF4
```

---

## 🛠️ How We Are Building It

### Frontend → Backend → Integration

```
PHASE 1 — Frontend shell (Week 1–2)
─────────────────────────────────────────────────────
  Person 3 builds dashboard.html + style.css
  · Topbar, stat cards, three panels
  · Status tag colours (ok / low / critical / out)
  · Filter buttons (All / In stock / Low / Critical)
  · Static mock values hardcoded in HTML for now
  · Goal: looks exactly like the design, no Flask yet

PHASE 2 — Backend + data layer (Week 1–2, parallel)
─────────────────────────────────────────────────────
  Person 2 builds app.py + mock_data.py
  · Flask routes returning JSON from mock data
  · get_status() and get_alerts() logic tested in terminal
  · No HTML involved yet — just clean data in and data out
  · Goal: curl localhost:5000/api/stock returns correct JSON

PHASE 3 — Integration (Week 3)
─────────────────────────────────────────────────────
  Person 2 + Person 3 connect the two halves
  · Replace hardcoded HTML values with Jinja2 template tags
  · Flask passes stock, transfers, alerts, stats to template
  · Person 4 tests edge cases: zero stock, empty transfers,
    all items critical
  · Goal: one working end-to-end dashboard on localhost

PHASE 4 — Features (Week 4–5)
─────────────────────────────────────────────────────
  · script.js: filter buttons work client-side
  · Team channel UI (WebSocket or polling)
  · AI agent query box (reads live dashboard state)
  · Dashboard layout customisation (add / remove panels)

PHASE 5 — Odoo API swap + polish (Week 6)
─────────────────────────────────────────────────────
  · Replace mock_data.py with odoo_client.py
  · Connect to Odoo demo instance via XML-RPC
  · Final UI polish, demo rehearsal, freeze
```

---

## 📁 Project Structure

```
jodo/
│
├── 🐍  app.py                ← Flask routes, business logic
├── 📦  mock_data.py          ← Sample data (Phase 1–3)
├── 🔌  odoo_client.py        ← Odoo XML-RPC connector (Phase 5)
├── 📋  requirements.txt
├── 🔐  .env.example
│
├── templates/
│   ├── 🖥️  dashboard.html    ← Main three-panel view
│   ├── 💬  channels.html     ← Team networking view
│   └── 🤖  agent.html        ← AI agent interface
│
└── static/
    ├── 🎨  style.css         ← Dark cool palette, status colours
    └── ⚡  script.js         ← Filters, WebSocket, agent queries
```

---

## 🚀 Get Running in 60 Seconds

```bash
# Clone
git clone https://github.com/your-org/jodo.git && cd jodo

# Virtual environment
python -m venv venv && source venv/bin/activate

# Install
pip install -r requirements.txt

# Run
python app.py
```

Open **`http://localhost:5000`**

---

## 👥 Team

| Member | Responsibility |
|---|---|
| [Name] | Project lead · report · documentation · AI agent design |
| [Name] | Flask backend · data logic · Odoo API integration |
| [Name] | HTML/CSS frontend · dashboard UI · responsive design |
| [Name] | Testing · edge cases · team channel feature · script.js |

---

## 📎 References

- Odoo. (2025). *XML-RPC external API.* https://www.odoo.com/documentation/17.0/developer/reference/external_api.html
- G2. (2026). *Odoo ERP reviews.* https://www.g2.com/products/odoo-odoo-erp/reviews
- Trustpilot. (2026). *Odoo reviews.* https://www.trustpilot.com/review/odoo.com

---

<div align="center">
<sub>Built on Odoo · Simplified for every role · Course project — Digital Business Systems</sub>
</div>
