# Jodo — Business Operations Platform

> **Not just another ERP dashboard.**

Jodo is a role-specific, AI-assisted, and customisable business operations platform built on top of Odoo. It replaces one giant, one-size-fits-all ERP screen with a **dashboard tailored to each role**, a **team communication layer**, and an **AI operations agent** that can answer questions about the business in plain language — and act on them.

```
Your Role → Your Dashboard → Your Data → Your AI Assistant
```

---

## The Problem

Traditional ERPs (Odoo, SAP, etc.) bundle dozens of modules — CRM, Sales, Accounting, HR, Manufacturing, Inventory, POS, Marketing — into a single interface. A warehouse worker, a cafe owner, a retail manager, and an accountant all log into the *same* screen, even though each cares about a completely different slice of the data.

Jodo sits on top of Odoo (or mock data during development) and reshapes the same underlying data into role-specific views, adds a chat-style team layer, and gives everyone an AI agent to query operations in natural language instead of building reports manually.

---

## Documentation

| Doc | Covers |
|---|---|
| [`docs/FEATURES.md`](docs/FEATURES.md) | Dashboards, team channels, the AI operations agent, low-stock alert system |
| [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) | System layers, tech stack, data flow, how the AI connects at the API level |
| [`docs/IMPLEMENTATION.md`](docs/IMPLEMENTATION.md) | Project structure, AI agent tools/loop, development roadmap, setup instructions |

---

## Quick Start

```bash
git clone https://github.com/your-org/jodo.git
cd jodo
python -m venv venv
source venv/bin/activate      # venv\Scripts\activate on Windows
pip install -r requirements.txt
cp .env.example .env          # then add your ANTHROPIC_API_KEY
python app.py
```

Open **http://localhost:5000**. See [`docs/IMPLEMENTATION.md`](docs/IMPLEMENTATION.md) for full setup details.

---

## Tech Stack (at a glance)

| Layer | Technology |
|---|---|
| Frontend | HTML, CSS, JavaScript, Jinja2 |
| Backend | Python, Flask |
| Real-time | WebSocket / Polling |
| AI | LLM API with function calling (no model training) |
| Data | Mock data (Phase 1) → Odoo XML-RPC API (Phase 2+) |

Full breakdown in [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md).

---

## Project Status

**In Development** — building phase by phase, from the dashboard shell through backend/data, real-time features, the AI agent, and finally live Odoo integration. Full roadmap in [`docs/IMPLEMENTATION.md`](docs/IMPLEMENTATION.md).

---

## References

* Odoo — XML-RPC External API
* G2 — Odoo ERP Reviews
* Trustpilot — Odoo Reviews

---

<div align="center">

**Jodo**
*Built on Odoo · Simplified for every role*

</div>
