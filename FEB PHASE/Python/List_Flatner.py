def flatten_list(nested_list):
    if not isinstance(nested_list, list):
        raise ValueError("Input must be a list")
    
    result = []

    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))  # recursive call
        else:
            result.append(item)

    return result    