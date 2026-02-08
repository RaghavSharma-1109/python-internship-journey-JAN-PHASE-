def validate_input(data:dict):
    if not isinstance(data, dict):
        return False,'Data must be dict'
    if not data:
        return False, 'Data may not be empty'
    req = {'user_id','role','action'}
    if not req.issubset(data):
        return False,'Missing required fields'


    user_id = data.get('user_id')
    if not isinstance(user_id,int):
        return False, 'User ID must be Integer only'
    if user_id<=0:
        return False, 'User Id must be positive only'
    

    role = data.get('role')
    if not isinstance(role,str):
        return False, 'Role must be in string'
    role = role.strip().lower()
    if role not in {'admin','user'}:
        return False, 'Invalid Request'
    

    action = data.get('action')
    if not isinstance(action,str):
        return False,'Action must be string'
    action = action.strip().lower()
    if action not in {'read','write','delete'}:
        return False, 'Inavalid Action'
    
    return True, {
        'user_id':user_id,
        'role':role,
        'action': action
    }

def authorize(role: str, action: str):
    if action == 'delete' and role != 'admin':
        return False, 'Not authorized'
    return True,None

def execute(action:str):
    return f"{action} executed successfully"
    

def handle_request(request):
    valid,result = validate_input(request)
    if not valid:
        return {
            'status':False,
            'message': result,
            'data': None
        }
    auth_ok,error = authorize(result['role'],result['action'])
    if not auth_ok:
        return {
            'status':False,
            'message': error,
            'data': None
        }
    execution = execute(result['action'])
    return {
            'status':True,
            'message': 'Request processed successfullly',
            'data': execution
        }