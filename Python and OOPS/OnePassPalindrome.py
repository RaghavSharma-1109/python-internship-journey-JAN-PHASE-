def is_palindrome(s):


    left = 0
    right = len(s)-1
    count = 0   
    while left <= right:
        
        if s[left]!=s[right]:
            count +=1
            if count>1:
                return False
        left +=1
        right -=1
    
    return True

s = input('Enter a string: ')
result = is_palindrome(s)

if result:
    print(f'Ths string {s} can be make a PALINDROME by one change.')
else:
    print(f'Ths string {s} can not make a PALINDROME by one change.')
    