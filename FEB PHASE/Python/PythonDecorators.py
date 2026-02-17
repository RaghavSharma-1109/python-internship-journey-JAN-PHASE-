def validate_types(func):
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__
        
        param_names = func.__code__.co_varnames[:func.__code__.co_argcount]
        
        arguments = dict(zip(param_names, args))
        arguments.update(kwargs)

        for param, expected_type in annotations.items():
            if param == "return":
                continue
            
            if param in arguments:
                value = arguments[param]

                # Strict rule for int
                if expected_type is int:
                    if type(value) is not int:
                        raise TypeError(
                            f"Argument '{param}' must be strictly of type int"
                        )

                # Flexible rule for float
                elif expected_type is float:
                    if not isinstance(value, (int, float)):
                        raise TypeError(
                            f"Argument '{param}' must be numeric (int or float)"
                        )

                # Strict rule for everything else
                else:
                    if type(value) is not expected_type:
                        raise TypeError(
                            f"Argument '{param}' must be of type {expected_type.__name__}"
                        )


        result = func(*args, **kwargs)

        if "return" in annotations:
            expected_return = annotations["return"]

            if expected_return is float:
                if not isinstance(result, (int, float)):
                    raise TypeError(
                        f"Return value must be numeric (int or float)"
                    )
            else:
                if type(result) is not expected_return:
                    raise TypeError(
                        f"Return value must be of type {expected_return.__name__}"
                    )


        return result

    return wrapper
@validate_types
def calculate_emi(principal: float, rate: float, years: int) -> float:
    monthly_rate = rate / (12 * 100)
    months = years * 12
    
    emi = (principal * monthly_rate * (1 + monthly_rate) ** months) / \
          ((1 + monthly_rate) ** months - 1)

    return float(emi)

print(calculate_emi(500000.0, 8.5, 10))