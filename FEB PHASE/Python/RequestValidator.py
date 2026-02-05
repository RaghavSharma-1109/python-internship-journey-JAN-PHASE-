def validate_request(payload: dict):
    if not isinstance(payload,dict):
        return {
        "status": False,
        "error": "Only Dicts are allowed"
        }

print(validate_request('h':1))
