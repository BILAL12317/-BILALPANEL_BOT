from firebase import db
from datetime import datetime


def create_order(user_id, plan, amount, status="Pending"):
    if db is None:
        return

    order = {
        "user_id": user_id,
        "plan": plan,
        "amount": amount,
        "status": status,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    db.collection("orders").add(order)


def get_orders(user_id):
    if db is None:
        return []

    docs = (
        db.collection("orders")
        .where("user_id", "==", user_id)
        .stream()
    )

    orders = []
    for doc in docs:
        orders.append(doc.to_dict())

    return orders


def get_all_orders():
    if db is None:
        return []

    docs = db.collection("orders").stream()

    orders = []
    for doc in docs:
        orders.append(doc.to_dict())

    return orders