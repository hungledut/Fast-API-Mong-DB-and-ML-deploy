def user_serializer(user) -> dict:
    return {
        "id": str(user["_id"]),
        "username": user["username"],
        "password": user["password"],
    }

def users_serializer(users) -> list:
    return [user_serializer(user) for user in users]