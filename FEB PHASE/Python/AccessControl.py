class AccessDeniedError(Exception):
    pass
current_role = input("Enter your role: ")
def require_role(role):
    def decorator(func):
        def wrapper(*args,**kwargs):
            if not isinstance(current_role, str):
                raise AccessDeniedError("Invalid current role")
            if current_role != role:
                raise AccessDeniedError('Access Denied')
            print(f"User with role {current_role} tried accessing {func.__name__}")
            return func(*args,**kwargs)
        return wrapper
    return decorator

@require_role("admin")
def delete_user():
    print("User Deleted")
@require_role("admin")
def create_user():
    print("User created")   
@require_role("admin","user") 
def view_dashboard():
    print("Dashboard opened")   