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
    for i,j in kwargs.items():
        print(f'{i}: {j}')

        
            
