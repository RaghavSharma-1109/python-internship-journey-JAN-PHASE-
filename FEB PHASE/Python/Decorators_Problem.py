class TypeValidationError(Exception):
    pass
def type_check(func):
    def wrapper(*args,**kwargs):
        annotations = func.__annotations__
        para_names = func.__code__.co_varnames[:func.__code__.co_argcount]
        values = {}
        # Case of args
        for name,value in zip(para_names,args):
            values[name] = value
        # Case of kwargs
        for name,value in kwargs.items():
            values[name] = value

        #Type Validation
        for name, expected_type in annotations.items():
            if name == 'return':
                continue
            if name in values:
                if not isinstance(values[name], expected_type):
                    raise TypeValidationError(
                        f"{name} must be of {expected_type}, got {type(values[name])}"
                    )
        result = func(*args,**kwargs)
        if 'return' in annotations:
            if not isinstance(result,annotations['return']):
                raise TypeValidationError(
                    f"Return must be of type {annotations['return']}, got{type(result)}"
                    )
        return result
    
    return wrapper
@type_check
def greet(name: str, age: int) -> str:
    return f"{name} is {age} years old"