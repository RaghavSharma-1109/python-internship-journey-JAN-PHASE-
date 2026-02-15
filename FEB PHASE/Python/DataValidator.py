def validate_dataset(data):
    errors = []
    clean_data = []

    required_keys = {"age", "salary", "experience"}

    if not isinstance(data, list):
        return {
            "status": False,
            "errors": ["Data must be a list"],
            "clean_data": []
        }

    for idx, item in enumerate(data):
        row_errors = []

        if not isinstance(item, dict):
            errors.append(f"Row {idx}: Item is not a dictionary")
            continue

        # Check keys
        if not required_keys.issubset(item.keys()):
            row_errors.append("Missing required keys")

        age = item.get("age")
        salary = item.get("salary")
        experience = item.get("experience")

        # Type check (block bool)
        for field_name, value in [("age", age), ("salary", salary), ("experience", experience)]:
            if type(value) is not int:
                row_errors.append(f"{field_name} must be integer")

        # Value rules
        if type(age) is int and age <= 0:
            row_errors.append("age must be > 0")

        if type(salary) is int and salary < 0:
            row_errors.append("salary must be >= 0")

        if type(experience) is int and experience < 0:
            row_errors.append("experience must be >= 0")

        if row_errors:
            errors.append(f"Row {idx}: " + ", ".join(row_errors))
        else:
            clean_data.append(item)

    return {
        "status": len(errors) == 0,
        "errors": errors,
        "clean_data": clean_data
    }
data =[
    {"age": 22, "salary": 50000, "experience": 1},        # ✅ valid
    {"age": -5, "salary": 40000, "experience": 2},        # ❌ invalid age
    {"age": 25, "salary": "60000", "experience": 3},      # ❌ salary wrong type
    {"salary": 30000, "experience": 1},                   # ❌ missing age
    {"age": 30, "salary": 70000, "experience": 5},        # ✅ valid
    {"age": True, "salary": 45000, "experience": 2},      # ❌ bool trap
    {"age": 28, "salary": -1000, "experience": 4},        # ❌ negative salary
    {"age": 24, "salary": 35000, "experience": -1},       # ❌ negative experience
    "random_string",                                      # ❌ not dict
]
print(validate_dataset(data))