def process_request(user_id, action="view", is_admin='False'):
    if is_admin=='True':
        return "Action allowed"
    elif action == "delete":
        return "Permission denied"
    else:
        return "Action allowed"