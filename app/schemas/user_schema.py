"User Schema"

def user_serializer(user) -> dict:
    "User Serializer"
    return {
        "id": str(user["_id"]),
        "username": user["username"],
        "password": user["password"],
    }

def users_serializer(users) -> list:
    "Users Serializer"
    return [user_serializer(user) for user in users]
