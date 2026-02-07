def validate_request(payload: dict):
    if not isinstance(payload,dict):
        return False ,'Invalid Data'
    req = {'user_id','action'}
    if not req.issubset(payload):
        return False, 'Missing required data'

    user_id = payload.get('user_id')
    if not isinstance(user_id,int):
        return False, "User ID must be Integer"
    if user_id<=0:
        return False, 'User ID must be positive'
    action = payload.get('action')

    if not isinstance(action,str) or not action:
        return False,'Action must be a string'
    action = action.strip().lower()
    if action not in {'create', 'read', 'update', 'delete'}:
        return False, 'Action not allowed'
    return True, {
    "user_id": user_id,
    "action": action,
    "is_admin": payload.get("is_admin", False)
}

def authorise_action(action,is_admin):
    if not isinstance(is_admin,bool):
        return False,"is_admin must be a Boolean"

    if action == 'delete' and not is_admin:
        return False,'Only admins and dalete'
    return True,None

DATABASE = {
    1: {"name": "Raghav", "role": "user"},
    2: {"name": "Admin", "role": "admin"}
}
def perform_action(user_id, action):
    if user_id not in DATABASE:
        return "User not found"

    if action == "read":
        return DATABASE[user_id]

    if action == "create":
        return "User created"

    if action == "update":
        return "User updated"

    if action == "delete":
        return "User deleted"

def handle_request(payload):
    valid, result = validate_request(payload)

    if not valid:
        return {
            "status": False,
            "message": result,
            "data": None
        }

    auth_ok, error = authorise_action(
        result["action"],
        result["is_admin"]
    )

    if not auth_ok:
        return {
            "status": False,
            "message": error,
            "data": None
        }
    execution_result = perform_action(
        result["user_id"],
        result["action"]
    )
    return {
        "status": True,
        "message": "Request processed successfully",
        "data": {
            'result':execution_result
        }
    }

