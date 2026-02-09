def sanitize_input(data):
    if data is None:
        return None
    if isinstance(data,(str,list,dict)) and len(data) == 0:
        return None
    if not isinstance(data,dict):
        return "Invalid"
    for key in data.keys():
        if not isinstance(key,str):
            return "Invalid"
    return data
