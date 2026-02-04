def validate_user(username, age):
    if not isinstance(username, str):
        return "Username must be a string"

    if not isinstance(age, int):
        return "Age must be an integer"

    if username.strip() == "":
        return "Username cannot be empty"

    if age < 18:
        return "Age must be 18 or above"

    return "User validated"
