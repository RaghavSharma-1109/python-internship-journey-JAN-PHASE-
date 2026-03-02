import inspect
class TypeValidationError(Exception):
    pass

def type_check(func):
    def wrapper(*args,**kwargs):
        sig = inspect.signature(func)
        try: 
            bound = sig.bind(*args,**kwargs)
            bound.apply_defaults()
        except TypeError as e:
            raise TypeValidationError(str(e))
        for name,param in sig.parameters.items():
            if param.annotation == inspect._empty:
                continue
            if not isinstance(bound.arguments[name],param.annotation):
                raise TypeValidationError(
                    f"Parameter '{name}' must be {param.annotation}, got {type(bound.arguments[name])}"
                )
        result = func(*args,**kwargs)
        return_type = sig.return_annotation
        if return_type is not inspect._empty:
            if return_type is None:
                if result is not None:
                    raise TypeValidationError(
                        f"Return Type must be None"
                    )
            elif not isinstance(result,return_type):
                raise TypeValidationError(
                    f"Return Type must be {return_type}, got {type(result)}"
                )
        return result
    return wrapper