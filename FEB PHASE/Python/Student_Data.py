def process_student_data(payload: dict):
    if not isinstance(payload,dict):
        return {
            'status': False,
            'error':'Data must be in Dict'
        }
    if len(payload) ==0:
        return {
            'status': False,
            'error':'Data can not be empty.'
        }
    for key in payload.keys():
        if not isinstance(key,str):
            return {
            'status': False,
            'error':'Key must be in string.'
        }
    req = {'name','age','marks'}
    if not req.issubset(payload):
        return {
            'status': False,
            'error':'Missing required fields'
        }
    
    name = payload.get('name')
    if name is None:
        return {
            'status': False,
            'error':'Name can not be empty.'
        }
    if not isinstance(name, str):
        return {
            'status': False,
            'error':'Name must be string'
        }
    name = name.strip().lower()
    if len(name) ==0:
        return {
            'status': False,
            'error':'Name can not be empty'
        }
    
    age = payload.get('age')
    if age is None:
        return {
            'status': False,
            'error':'Enter a valid age'
        }
    if not isinstance(age,int):
        return {
            'status': False,
            'error':'Age must be integer'
        }
    if age<16 or age>60:
        return {
            'status': False,
            'error':'Age limit crossed '
        }
    
    marks = payload.get('marks')
    if marks is None or not isinstance(marks,list):
        return {
        'status': False,
        'error':'Marks must be List'
    }
    if len(marks)<3:
        return {
            'status': False,
            'error':'Invalid Marks '
        }
    total = 0
    for mark in marks:
        if not isinstance(mark,int):
            return {
            'status': False,
            'error':'Marks must be List'
        }
        total += mark
    average = total// len(marks)
    passed = average >=40
    return {
            'status': True,
            'data':{
                'Name': name,
                'Age': age,
                'Average_Marks': average,
                'Passed' : passed
            }
        }