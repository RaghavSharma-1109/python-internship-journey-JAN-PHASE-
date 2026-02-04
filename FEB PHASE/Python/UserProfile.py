def create_user_profile(**kwargs):
    if not kwargs:
        return 'Data can not be empty.'

    for i in ['name','role','age']:
        if i not in kwargs:
            return 'Missing Required Fileds'


    name = kwargs.get('name')
    role = kwargs.get('role')
    age = kwargs.get('age')


    if not isinstance(name,str):
        return 'Invalid Input.'
    if not isinstance(age,int) or age<=0:
        return 'Invalid Input.'
    if not isinstance(role,str):
        return 'Invalid Input.'

    print("User Profile Created")
    print(f"name : {name}")
    print(f"age : {age}")
    print(f"role : {role}")

    extra_fields = ['name', 'age', 'role']

    has_extra = False
    for key, value in kwargs.items():
        if key not in extra_fields:
            if not has_extra:
                print("Extra fields:")
                has_extra = True
            print(f"{key} : {value}")


        
            
