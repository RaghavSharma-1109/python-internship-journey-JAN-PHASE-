def validate_request(payload: dict):
    if not isinstance(payload, dict):
        return {"status": False, "error": "Payload must be a dictionary"}

    required_keys = {"user_id", "action", "is_admin"}
    if not required_keys.issubset(payload):
        return {"status": False, "error": "Missing required fields"}

    user_id = payload.get("user_id")
    action = payload.get("action")
    is_admin = payload.get("is_admin")

    if not isinstance(user_id, int):
        return {"status": False, "error": "user_id must be an integer"}

    if user_id <= 0:
        return {"status": False, "error": "user_id must be positive"}

    if not isinstance(action, str):
        return {"status": False, "error": "action must be a string"}

    if action not in {"read", "write", "delete"}:
        return {"status": False, "error": "Invalid action"}

    if not isinstance(is_admin, bool):
        return {"status": False, "error": "is_admin must be boolean"}

    if action == "delete" and not is_admin:
        return {"status": False, "error": "Admin privileges required"}

    return {"status": True, "message": "Request validated"}

def process_request(payload:dict):
    validation = validate_request(payload)
    if validation['status'] == False:
        return validation
    action = payload.get('action')
    return {
    "status": True,
    "performed": action
    }