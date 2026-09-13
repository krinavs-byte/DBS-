# Implementation Status and Ownership

This file documents current implementation work, who contributed, which tasks are completed, and the next steps. Branch with implementation changes: `impl/cleanup-duplicates`.

Contributors (Person mapping)
- Person 1: Vaibhavi
- Person 2: Aayoshi
- Person 3: Prachi
- Person 4: Triesha
- Person 5: Krina

Completed tasks (summary)
- Core backend models (User, Product, StockLevel, Transfer, SalesOrder, TeamMember, DashboardLayout) — present in `db.py` (pre-existing).  
  Implemented/maintained by the team (original uploads by team members).

- Seed data and development seed script (`seed.py`) to create admin user, sample products, stock levels, transfers, sales orders, team members, and role-default dashboard layouts — present (pre-existing).

- Dashboard backend routes and API endpoints (`dashboard/routes.py`) — canonical implementation for dashboard features (login-protected view, CSRF handling, layout CRUD, panel endpoints).  
  Canonical file kept: `dashboard/routes.py` (chosen to be the canonical blueprint).

- Authentication routes (login/logout, password-reset skeleton) — available in `auth/` (use `auth/routes.py`).

- Consolidation & cleanup (migrations, audit, client JS, duplicate cleanup script) — implemented in branch `impl/cleanup-duplicates` and committed to the branch. Implemented by: Krina (Person 5) with assistant.
  - Added AuditLog model to `db.py`.
  - Added alembic migrations under `alembic/versions/`:
    - `0001_add_audit_logs.py` (fixed FK -> `user.id`)
    - `0002_add_dashboard_layout.py`
  - Added client-side script `static/script.js` (Sortable-based reorder + CSRF header + save flow).
  - Added `scripts/remove_duplicates.sh` to remove legacy duplicate folders (safe helper; run locally to apply deletions).
  - Added a basic pytest skeleton `tests/test_dashboard_api.py`.

Files/dirs consolidated or removed (planned)
- Merged useful migration files from `alembic1/versions/` into `alembic/versions/`.
- Duplicate folders to be removed (script added, deletion performed locally when you run the script): `alembic1/`, `dashboard1/`, `auth1/`, `docs1/`, `templates1/`, and `README_FIRST1.md`.

Who did / owns which area (current assignment)
- Backend & DB migrations: Owner — Vaibhavi (Person 1) and Krina (Person 5) for cleanup/migration fixes
- Authentication & session handling: Owner — Aayoshi (Person 2)
- Initial dashboard implementation and templates: Owner — Prachi (Person 3)
- Frontend dashboard UI (customize, reorder, client script): Owner — Triesha (Person 4) and Krina (Person 5) for the quick client script
- Seed & sample data: Owner — Prachi (Person 3)
- Audit logging, alembic consolidation, CI setup: Owner — Krina (Person 5)

Notes on the current canonical setup
- We use `dashboard/routes.py` as the canonical dashboard blueprint. If you prefer the alternate copy (`dashboard1/routes.py`) we will merge the necessary differences but the canonical file is `dashboard/routes.py` in this branch.
- Migrations must live under `alembic/versions/` for `alembic upgrade head` to work. The branch consolidates migrations to that folder.
- The cleanup script `scripts/remove_duplicates.sh` will `git rm` duplicate folders. Review the branch changes before running the script locally.

How to verify locally (short checklist)
1. Fetch the branch and checkout:
   git fetch origin
   git checkout -b impl/cleanup-duplicates origin/impl/cleanup-duplicates

2. (Optional) Inspect and remove duplicates by running (review script first):
   bash scripts/remove_duplicates.sh

3. Create virtualenv and install requirements:
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt

4. Apply migrations (recommended) or run seed for dev:
   alembic upgrade head
   # or
   python seed.py

5. Start the app:
   python app.py

6. Manual checks:
   - Login at /login: admin@example.com / passw0rd
   - Visit /app/dashboard -> layout should render and cookie `csrf_token` should be set
   - Customize, reorder panels, Save -> should POST/PUT with `X-CSRF-Token` and persist
   - Verify audit rows in DB table `audit_logs`

Pending work / recommended next steps (prioritized)
1. Add unit and integration tests for layout CRUD, schema validation, and optimistic-locking (I can add these now).  
2. Add GitHub Actions CI workflow to run migrations, seed (or create DB), run pytest and optionally Cypress.  
3. Improve frontend to GridStack for resize/position persistence (if required).  
4. Add rate-limiting and monitoring (/metrics) for production readiness.

If you want, I will now:
- Run the duplicate deletion in this branch (permanently remove the *1 folders) and push the changes, or
- Add the unit tests & CI workflow to the same branch and update the PR.

Please reply which of the two you want next: `Delete duplicates now` or `Add tests & CI`.
