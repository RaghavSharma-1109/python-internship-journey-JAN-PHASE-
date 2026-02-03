def validate_login_request(**kwargs):
    if not kwargs:
        return 'Data can not be empty!!'
    if 'email' not in kwargs or 'password' not in kwargs:
        return 'Enter valid Email/Password'

    email = kwargs.get('email')
    password = kwargs.get('password')

 
    if not isinstance(email,str):
        return 'Invalid Input!!'
    if not isinstance(password,str):
        return 'Invalid Input!!'
    
    if email.count('@') != 1:
        return 'Invalid Email'
    host,domain = email.split('@')
    if '.' not in domain:
        return 'Invalid Email'

    if len(password)<=8:
        return 'Weak Password'
    has_digit = False
    for ch in password:
        if ch.isdigit():
            has_digit = True
            break
    if not has_digit:
        return 'Weak password'
    
    print('Login Detais Validated!!')

    print(f'email:{email}')
    print('password:********')
    
    required = ['email', 'password']
    for key,value in kwargs.items():
        if key not in required:
            print(f'{key}:{value}')
    