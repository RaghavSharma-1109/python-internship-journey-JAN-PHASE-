def normalize_payload(data):
    if data is None:
        return None

    if isinstance(data, (str, list, dict)) and len(data) == 0:
        return None

    if not isinstance(data, dict):
        return "Invalid"

    result = {}

    for key, value in data.items():
        if not isinstance(key, str):
            return "Invalid"

        normalized_key = key.lower()

        if value is None:
            continue

        if isinstance(value, str):
            result[normalized_key] = value.strip()
        else:
            result[normalized_key] = value

    if len(result) == 0:
        return None

    return result
