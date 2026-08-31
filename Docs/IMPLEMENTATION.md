# Jodo — Project Implementation Tracker

> **How to use this file**
> Update every row the moment a task changes state. Do not reconstruct history at the end.
> Every completed task must have a commit hash or file reference in the Evidence column.
> AI assistance must be recorded honestly — the student listed in *Completed By* is the person who reviewed, integrated, tested and verified the work.

---

## Team

| ID | Name | Role focus |
|---|---|---|
| P1 | [Name] | Project lead · Architecture · Documentation · Scalability |
| P2 | [Name] | Flask backend · Routes · Database · Odoo API |
| P3 | [Name] | Frontend · HTML/CSS · Jinja2 templates · UI logic |
| P4 | [Name] | Business logic · Algorithm · Testing · AI agent |

---

## Status key

| Status | Meaning |
|---|---|
| Pending | Identified, not started |
| In Progress | Started, not complete |
| Completed | Implemented and verified |
| Blocked | Cannot proceed — dependency documented |
| Reopened | Found to contain a problem, needs rework |

---

## Phase 1 — Project Foundation

*Goal: repo is set up, folder structure exists, everyone can run the project locally.*

| Task ID | Task | Component | Assigned To | Status | Completed By | Date Completed | AI Assistance | Evidence |
|---|---|---|---|---|---|---|---|---|
| T001 | Create GitHub repository and add all members | Repo | P1 | Done | Prachi | — | No | — |
| T002 | Define and commit folder structure (`app.py`, `mock_data.py`, `templates/`, `static/`, `docs/`) | Repo | P1 | done | Prachi| — | No | — |
| T003 | Write `requirements.txt` with Flask, python-dotenv, requests | Repo | P2 | Done | Krina | 2026-08-29 | Yes | requirements.txt — commit 1a45d0c61426211c3750ac44de67460484bac516 |
| T004 | Write `.env.example` with `ANTHROPIC_API_KEY`, `ODOO_URL`, `ODOO_DB`, `ODOO_USERNAME`, `ODOO_PASSWORD` | Config | P2 | Done | Krina | 2026-08-29 | Yes | .env.example — commit 1a45d0c61426211c3750ac44de67460484bac516 |
| T005 | Write `README.md` with setup instructions (clone → venv → install → run) | Docs | P1 | Done | Vaibhavi and Prachi | — | Yes | — |
| T006 | Commit `docs/architecture.md` (existing document) | Docs | P1 | Done | Vaibhavi | — | No | — |
| T007 | Create this file (`docs/project-implementation.md`) and commit it | Docs | P1 | Done | Prachi | — | No | — |

---

## Phase 2 — Mock Data and Database Schema

*Goal: all data shapes are defined. Frontend and backend can both reference the same field names.*

| Task ID | Task | Component | Assigned To | Status | Completed By | Date Completed | AI Assistance | Evidence |
|---|---|---|---|---|---|---|---|---|
| T008 | Write `mock_data.py` — `STOCK_LEVELS` list with fields: product, sku, location, qty, min_qty | Data | P4 | Done | Prachi | — | Yes | — |
| T009 | Write `mock_data.py` — `TRANSFERS` list with fields: ref, due, state, type, assigned_to | Data | P4 | Done | Prachi | — | Yes | — |
| T010 | Write `mock_data.py` — `CUSTOMERS` list with fields: name, email, orders, spent, status, segment | Data | P4 | Done | Prachi | — | Yes | — |
| T011 | Write `mock_data.py` — `SALES_ORDERS` list with fields: ref, customer, amount, status, date, items | Data | P4 | Done | Prachi | — | Yes | — |
| T012 | Write `mock_data.py` — `TEAM` list with fields: name, email, department, role, status | Data | P4 | Done | Prachi | — | Yes | — |
| T013 | Write `mock_data.py` — `NETWORK_POSTS` list with fields: author, role, content, likes, timestamp | Data | P4 | Done | Aayoshi | — | Yes | — |
| T014 | Design database schema — 6 tables: User, Product, StockLevel, Transfer, SalesOrder, TeamMember | Database | P2 | Done | Aayoshi | — | Yes | — |
| T015 | Draw ER diagram showing all 6 tables, attributes, primary keys and 5+ relationships | Database | P2 | Done | Aayoshi | — | Yes | — |
| T016 | Add ER diagram to `docs/architecture.md` | Docs | P1 | Done | Aayoshi | — | No | — |
| T017 | Set up SQLite database with SQLAlchemy — `db.py` with all 6 models defined | Database | P2 | Done | Aayoshi | — | Yes | — |
| T018 | Write database seed script — `seed.py` — populates DB from mock_data.py for local dev | Database | P2 | Pending | — | — | Yes | — |

---

## Phase 3 — Flask Backend

*Goal: every route returns correct data. All routes testable with a browser or curl before any template work.*

| Task ID | Task | Component | Assigned To | Status | Completed By | Date Completed | AI Assistance | Evidence |
|---|---|---|---|---|---|---|---|---|
| T019 | Create `app.py` skeleton — Flask init, blueprint registration, `if __name__ == '__main__'` | Backend | P2 | Pending | — | — | Yes | — |
| T020 | Implement `GET /` — serves landing page | Backend | P2 | Pending | — | — | No | — |
| T021 | Implement `GET /login` and `POST /login` — form renders and processes | Backend/Auth | P2 | Pending | — | — | Yes | — |
| T022 | Implement session-based authentication — role stored in session (`user` or `manager`) | Backend/Auth | P2 | Pending | — | — | Yes | — |
| T023 | Implement `GET /logout` — clears session, redirects to `/` | Backend/Auth | P2 | Pending | — | — | No | — |
| T024 | Implement `GET /app/dashboard` — passes stock, transfers, alerts, stats to template | Backend | P2 | Pending | — | — | Yes | — |
| T025 | Implement `GET /app/inventory` — passes full stock list to template | Backend | P2 | Pending | — | — | Yes | — |
| T026 | Implement `GET /app/customers` — passes customer list to template | Backend | P2 | Pending | — | — | Yes | — |
| T027 | Implement `GET /app/sales` — passes sales orders to template | Backend | P2 | Pending | — | — | Yes | — |
| T028 | Implement `GET /app/analytics` — passes aggregated KPI data to template | Backend | P2 | Pending | — | — | Yes | — |
| T029 | Implement `GET /app/team` — passes team list to template | Backend | P2 | Pending | — | — | Yes | — |
| T030 | Implement `GET /app/network` — passes network posts to template | Backend | P2 | Pending | — | — | Yes | — |
| T031 | Implement `GET /app/settings` and `POST /settings/save` — form loads and saves | Backend | P2 | Pending | — | — | Yes | — |
| T032 | Implement `GET /manager/dashboard` — manager-only route, role check, aggregate KPIs | Backend/Auth | P2 | Pending | — | — | Yes | — |
| T033 | Implement `GET /manager/users` — list of all registered users with role and status | Backend/Auth | P2 | Pending | — | — | Yes | — |
| T034 | Add `@login_required` and `@manager_required` decorators for route protection | Backend/Auth | P2 | Pending | — | — | Yes | — |

---

## Phase 4 — Business Logic and Algorithm

*Goal: all data processing functions written, tested independently, and integrated into Flask routes.*

| Task ID | Task | Component | Assigned To | Status | Completed By | Date Completed | AI Assistance | Evidence |
|---|---|---|---|---|---|---|---|---|
| T035 | Write `get_status(item)` — returns `ok`, `low`, `critical`, or `out` based on qty vs min_qty | Logic | P4 | Pending | — | — | No | — |
| T036 | Write `get_alerts(stock)` — filters items below threshold, sorts by urgency percentage ascending | Logic | P4 | Pending | — | — | No | — |
| T037 | Write `compute_stats(stock, transfers)` — returns total_skus, pending, due_today, alerts, critical | Logic | P4 | Pending | — | — | No | — |
| T038 | **[ALGORITHM]** Write `reorder_priority_score(item, transfers)` — scores each low-stock product using: `(1 - qty/min_qty) * 0.5 + (outgoing_transfers / max_transfers) * 0.3 + (1 / days_unti[...]
| T039 | **[ALGORITHM]** Write `rank_reorder_queue(stock, transfers)` — applies reorder_priority_score to all low-stock items, returns sorted list with score and recommended action (Urgent / Soon /[...]
| T040 | **[ALGORITHM]** Document the algorithm — problem, inputs, processing logic, pseudocode, example input, example output, location in code | Docs | P4 | Pending | — | — | No | — |
| T041 | Write `customer_segment(customer)` — labels customers as High Value / Regular / At Risk based on order count and spend | Logic | P4 | Pending | — | — | Yes | — |
| T042 | Write unit tests for `get_status()` — covers all four states including boundary conditions | Testing | P4 | Pending | — | — | No | — |
| T043 | Write unit tests for `reorder_priority_score()` — covers normal input, zero outgoing transfers, same-day delivery | Testing | P4 | Pending | — | — | No | — |
| T044 | Integrate all logic functions into Flask routes — confirm routes receive correctly processed data | Integration | P4 | Pending | — | — | No | — |
| T045 | Edge case test: empty STOCK_LEVELS → dashboard shows zero-state messages, no crash | Testing | P4 | Pending | — | — | No | — |
| T046 | Edge case test: all items critical → alert panel shows all items, priority order correct | Testing | P4 | Pending | — | — | No | — |
| T047 | Edge case test: TRANSFERS empty → pending panel shows "No pending transfers" message | Testing | P4 | Pending | — | — | No | — |

---

## Phase 5 — Frontend Templates

*Goal: every page renders correctly with Jinja2 data. Matches the prototype design.*

| Task ID | Task | Component | Assigned To | Status | Completed By | Date Completed | AI Assistance | Evidence |
|---|---|---|---|---|---|---|---|---|
| T048 | Extract all CSS from prototype into `static/style.css` — verify no hex values remain in HTML | Frontend | P3 | Pending | — | — | No | — |
| T049 | Extract all JavaScript from prototype into `static/script.js` | Frontend | P3 | Pending | — | — | No | — |
| T050 | Create `templates/base.html` — shared `<head>`, CSS link, JS link, meta tags | Frontend | P3 | Pending | — | — | Yes | — |
| T051 | Create `templates/landing.html` — hero section, features, CTA buttons with `data-go` links | Frontend | P3 | Pending | — | — | Yes | — |
| T052 | Create `templates/login.html` — split panel, form with email + password + role selector | Frontend | P3 | Pending | — | — | Yes | — |
| T053 | Create `templates/dashboard.html` — KPI strip, stock table, transfers panel, alerts panel using Jinja2 loops and conditionals | Frontend | P3 | Pending | — | — | Yes | — |
| T054 | Create `templates/inventory.html` — full stock table with status pills, filter buttons (`data-filter`) | Frontend | P3 | Pending | — | — | Yes | — |
| T055 | Create `templates/customers.html` — customer table with segment pills and spend figures | Frontend | P3 | Pending | — | — | Yes | — |
| T056 | Create `templates/sales.html` — sales orders table with status pills and totals | Frontend | P3 | Pending | — | — | Yes | — |
| T057 | Create `templates/analytics.html` — KPI cards and SVG chart panels | Frontend | P3 | Pending | — | — | Yes | — |
| T058 | Create `templates/team.html` — employee directory with status indicators | Frontend | P3 | Pending | — | — | Yes | — |
| T059 | Create `templates/network.html` — post feed with tabs, composer form | Frontend | P3 | Pending | — | — | Yes | — |
| T060 | Create `templates/settings.html` — business profile form | Frontend | P3 | Pending | — | — | Yes | — |
| T061 | Create `templates/manager_dashboard.html` — aggregate KPIs across all users, role badge | Frontend | P3 | Pending | — | — | Yes | — |
| T062 | Create `templates/manager_users.html` — user list with role, status, last active | Frontend | P3 | Pending | — | — | Yes | — |
| T063 | Implement stock table filter buttons in `script.js` — `data-filter` on buttons, `data-status` on rows | Frontend | P3 | Pending | — | — | Yes | — |
| T064 | Implement page-switching navigation from `script.js` — `data-go` attribute, `.page.active` toggle | Frontend | P3 | Pending | — | — | No | — |
| T065 | Verify all Jinja2 variables render with real Flask data — no `undefined` or `None` visible on any page | Frontend | P3 | Pending | — | — | No | — |

---

## Phase 6 — AI Agent

*Goal: Jule chat interface sends a query, receives a grounded answer based on system data.*

| Task ID | Task | Component | Assigned To | Status | Completed By | Date Completed | AI Assistance | Evidence |
|---|---|---|---|---|---|---|---|---|
| T066 | Create `ai_agent.py` — `ask_agent(message, history)` function calling Claude API via `requests` | AI | P4 | Pending | — | — | Yes | — |
| T067 | Define tool schemas in `ai_agent.py` — `get_stock_levels`, `get_alerts`, `get_transfers`, `raise_reorder` | AI | P4 | Pending | — | — | Yes | — |
| T068 | Write `run_tool(name, input)` dispatcher — maps tool name to Python function, returns result | AI | P4 | Pending | — | — | Yes | — |
| T069 | Implement tool-use loop in `app.py` `/api/agent/query` route — loops until AI returns final text | AI | P2 | Pending | — | — | Yes | — |
| T070 | Create `templates/jule.html` — two-panel chat interface, message bubbles, input + send button | Frontend | P3 | Pending | — | — | Yes | — |
| T071 | Wire Jule chat UI to `/api/agent/query` via `fetch()` in `script.js` | Frontend | P3 | Pending | — | — | Yes | — |
| T072 | Test Jule with query: "Which products need reordering?" — verify grounded answer from mock data | Testing | P4 | Pending | — | — | No | — |
| T073 | Test Jule edge case: empty message sent — no API call, no empty bubble displayed | Testing | P4 | Pending | — | — | No | — |

---

## Phase 7 — Odoo API Integration

*Goal: `mock_data.py` is replaced by `odoo_client.py`. Live data feeds the dashboard.*

| Task ID | Task | Component | Assigned To | Status | Completed By | Date Completed | AI Assistance | Evidence |
|---|---|---|---|---|---|---|---|---|
| T074 | Create `odoo_client.py` — `OdooClient` class with XML-RPC authentication | Integration | P2 | Pending | — | — | Yes | — |
| T075 | Implement `fetch_stock()` — reads `stock.quant`, maps to STOCK_LEVELS shape | Integration | P2 | Pending | — | — | Yes | — |
| T076 | Implement `fetch_transfers()` — reads `stock.picking`, maps to TRANSFERS shape | Integration | P2 | Pending | — | — | Yes | — |
| T077 | Implement `fetch_alerts()` — reads `stock.warehouse.orderpoint`, maps to alerts shape | Integration | P2 | Pending | — | — | Yes | — |
| T078 | Swap `mock_data` imports in `app.py` for `odoo_client` calls — no template changes required | Integration | P2 | Pending | — | — | No | — |
| T079 | Test on Odoo demo instance — confirm stock data matches Odoo backend within 5 seconds | Testing | P4 | Pending | — | — | No | — |
| T080 | Test API failure scenario — Odoo unreachable → Flask returns graceful error, no crash | Testing | P4 | Pending | — | — | No | — |

---

## Phase 8 — Documentation and Scalability

*Goal: `docs/architecture.md` satisfies the CIA III rubric completely.*

| Task ID | Task | Component | Assigned To | Status | Completed By | Date Completed | AI Assistance | Evidence |
|---|---|---|---|---|---|---|---|---|
| T081 | Add current system architecture diagram to `docs/architecture.md` (Mermaid) | Docs | P1 | Pending | — | — | No | — |
| T082 | Add ER diagram to `docs/architecture.md` | Docs | P1 | Pending | — | — | No | — |
| T083 | Add data flow diagram (sequence diagram) to `docs/architecture.md` | Docs | P1 | Pending | — | — | No | — |
| T084 | Document proposed AWS cloud deployment — EC2, RDS, S3, CloudFront, ALB | Docs | P1 | Pending | — | — | Yes | — |
| T085 | **[SCALABILITY]** Calculate user growth: 10,000 base × 1.25^N for years 1–5. Show formula → values → result → interpretation | Docs | P1 | Pending | — | — | No | — |
| T086 | **[SCALABILITY]** Calculate peak concurrent users at 100K, 500K, 1M, 5M (multiply by 10%). Show all steps. | Docs | P1 | Pending | — | — | No | — |
| T087 | **[SCALABILITY]** Calculate requests per minute and per second at 10K, 50K, 100K, 500K active users (×5 req/min). Show all steps. | Docs | P1 | Pending | — | — | No | — |
| T088 | Document 1M-user scaling approach — app servers, DB read replicas, caching layer, CDN | Docs | P1 | Pending | — | — | Yes | — |
| T089 | Document 5M-user scaling approach — horizontal scaling, sharding, global CDN, microservices split | Docs | P1 | Pending | — | — | Yes | — |
| T090 | Document 8 security mechanisms — authentication, authorisation, data protection, network, DB, backup, monitoring, account protection | Docs | P1 | Pending | — | — | Yes | — |
| T091 | Document 5 failure scenarios with impact, detection, and recovery for each | Docs | P1 | Pending | — | — | Yes | — |
| T092 | Final review of `docs/architecture.md` against CIA III checklist — all sections present | Docs | P1 | Pending | — | — | No | — |

---

## Phase 9 — Final Polish and Submission

*Goal: everything works end to end. Every person can explain their own tasks.*

| Task ID | Task | Component | Assigned To | Status | Completed By | Date Completed | AI Assistance | Evidence |
|---|---|---|---|---|---|---|---|---|
| T093 | Full end-to-end walkthrough — user login → dashboard → inventory → Jule chat → logout | Testing | P4 | Pending | — | — | No | — |
| T094 | Full end-to-end walkthrough — manager login → manager dashboard → user management → logout | Testing | P4 | Pending | — | — | No | — |
| T095 | Verify all 6 database tables have data after running `seed.py` | Testing | P2 | Pending | — | — | No | — |
| T096 | Verify `docs/project-implementation.md` — every completed task has a commit reference | Docs | P1 | Pending | — | — | No | — |
| T097 | Code freeze — no new features after this point | Repo | P1 | Pending | — | — | No | — |
| T098 | Each person reads and can explain every task they are listed as Completed By | Viva prep | All | Pending | — | — | No | — |
| T099 | Final submission checklist verified against CIA III Section 27 | Docs | P1 | Pending | — | — | No | — |

---

## Algorithm Documentation — Reorder Priority Scorer

*Required by CIA III Section 5. Every algorithm must be documented here.*

**Task reference:** T038, T039, T040

**Problem being solved:**
When multiple products are below their reorder threshold simultaneously, warehouse staff need to know which ones to restock first. Ordering everything at once is not always possible — the algor[...]

**Inputs:**
- `item` — a stock record with `qty`, `min_qty`
- `transfers` — list of pending outgoing transfers referencing this product
- `days_until_delivery` — expected days until the next supplier delivery

**Processing logic:**

```
score = (stock_deficit_ratio × 0.5)
      + (outgoing_pressure_ratio × 0.3)
      + (delivery_urgency_ratio × 0.2)

where:
  stock_deficit_ratio     = 1 - (qty / min_qty)           # 0 = fine, 1 = empty
  outgoing_pressure_ratio = outgoing_count / max_outgoing  # how many transfers are drawing on this product
  delivery_urgency_ratio  = 1 / days_until_delivery        # higher when delivery is sooner needed
```

**Output:** float between 0 and 1. Score above 0.7 → Urgent. Score 0.4–0.7 → Soon. Below 0.4 → Monitor.

**Pseudocode:**

```
function reorder_priority_score(item, transfers, days_until_delivery):
    deficit = 1 - (item.qty / item.min_qty)
    outgoing = count transfers where product matches item
    pressure = outgoing / MAX_TRANSFERS_CONSTANT
    urgency = 1 / max(days_until_delivery, 1)   # avoid division by zero
    score = (deficit × 0.5) + (pressure × 0.3) + (urgency × 0.2)
    return clamp(score, 0, 1)

function rank_reorder_queue(stock, transfers):
    candidates = filter stock where qty < min_qty
    for each candidate:
        candidate.score = reorder_priority_score(candidate, transfers, candidate.days_until_delivery)
        candidate.action = classify(candidate.score)
    return sort candidates by score descending
```

**Where it is implemented:** `logic.py` → `reorder_priority_score()` and `rank_reorder_queue()`

**Example input:**

```python
item = { "product": "Corner Protectors", "qty": 5, "min_qty": 50 }
transfers = [ { "ref": "WH/OUT/00412", "product": "Corner Protectors" } ]
days_until_delivery = 3
```

**Example output:**

```python
{ "product": "Corner Protectors", "score": 0.82, "action": "Urgent" }
```

---

## Scalability Calculations

*Required by CIA III Section 16. All steps shown.*

### User Growth (25% per year, base 10,000)

**Formula:** Users(N) = 10,000 × 1.25^N

| Year | Formula | Result | Interpretation |
|---|---|---|---|
| 1 | 10,000 × 1.25^1 | 12,500 | Small team tooling — single server handles this comfortably |
| 2 | 10,000 × 1.25^2 | 15,625 | Still within single-instance capacity |
| 3 | 10,000 × 1.25^3 | 19,531 | Approaching point where read replicas become worthwhile |
| 4 | 10,000 × 1.25^4 | 24,414 | Caching layer (Redis) should be in place by this point |
| 5 | 10,000 × 1.25^5 | 30,518 | Load balancer across multiple app instances required |

### Peak Concurrent Users (10% of registered users)

**Formula:** Concurrent = Registered × 0.10

| Registered Users | Formula | Peak Concurrent | Interpretation |
|---|---|---|---|
| 100,000 | 100,000 × 0.10 | 10,000 | 2–3 app servers behind a load balancer |
| 500,000 | 500,000 × 0.10 | 50,000 | Auto-scaling group, read replicas for database |
| 1,000,000 | 1,000,000 × 0.10 | 100,000 | CDN for static assets, DB connection pooling essential |
| 5,000,000 | 5,000,000 × 0.10 | 500,000 | Global deployment, database sharding, microservices split |

### Requests per Minute and per Second (5 requests per active user per minute)

**Formula:** RPM = Active Users × 5 · RPS = RPM ÷ 60

| Active Users | RPM Formula | RPM | RPS Formula | RPS | Interpretation |
|---|---|---|---|---|---|
| 10,000 | 10,000 × 5 | 50,000 | 50,000 ÷ 60 | 833 | Nginx handles this on a single server |
| 50,000 | 50,000 × 5 | 250,000 | 250,000 ÷ 60 | 4,167 | Multiple Flask workers with Gunicorn required |
| 100,000 | 100,000 × 5 | 500,000 | 500,000 ÷ 60 | 8,333 | Horizontal scaling + load balancer essential |
| 500,000 | 500,000 × 5 | 2,500,000 | 2,500,000 ÷ 60 | 41,667 | CDN offloads static requests; only dynamic hits Flask |

---

*Last updated: [date] · Maintained by P1*
