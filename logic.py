from datetime import datetime


def get_status(item):
    qty = item.get("qty", 0)
    min_qty = item.get("min_qty", 0)

    if qty == 0:
        return "out"
    if qty < min_qty * 0.2:
        return "critical"
    if qty < min_qty:
        return "low"
    return "ok"


def get_alerts(stock):
    alerts = []
    for item in stock:
        qty = item.get("qty", 0)
        min_qty = item.get("min_qty", 0)
        if qty < min_qty:
            pct = 0 if min_qty == 0 else (qty / min_qty) * 100
            alerts.append({
                "product": item.get("product"),
                "sku": item.get("sku"),
                "location": item.get("location"),
                "qty": qty,
                "min_qty": min_qty,
                "status": get_status(item),
                "pct": pct,
            })
    alerts.sort(key=lambda item: item["pct"])
    return alerts


def compute_stats(stock, transfers):
    today = datetime.now().strftime("%Y-%m-%d")

    total_skus = len({item.get("sku") for item in stock if item.get("sku")})

    pending_transfers = 0
    for transfer in transfers:
        state = str(transfer.get("state", "")).lower()
        if state in {"pending", "in_transit", "awaiting_review", "waiting"}:
            pending_transfers += 1

    due_today = 0
    for transfer in transfers:
        if transfer.get("due") == today:
            due_today += 1

    alert_count = 0
    for item in stock:
        if item.get("qty", 0) < item.get("min_qty", 0):
            alert_count += 1

    critical_count = 0
    for item in stock:
        if get_status(item) in {"critical", "out"}:
            critical_count += 1

    return {
        "total_skus": total_skus,
        "pending_transfers": pending_transfers,
        "due_today": due_today,
        "alert_count": alert_count,
        "critical_count": critical_count,
    }
