from firebase import db


def add_user(user_id, username, first_name):
    if db is None:
        return

    db.collection("users").document(str(user_id)).set({
        "user_id": user_id,
        "username": username,
        "first_name": first_name,
    })


def get_user(user_id):
    if db is None:
        return None

    doc = db.collection("users").document(str(user_id)).get()

    if doc.exists:
        return doc.to_dict()

    return None


def get_all_users():
    if db is None:
        return []

    users = []
    docs = db.collection("users").stream()

    for doc in docs:
        users.append(doc.to_dict())

    return users