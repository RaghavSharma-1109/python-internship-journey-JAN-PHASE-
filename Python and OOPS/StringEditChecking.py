def is_one_edit_away(s1,s2):
    if abs(len(s1)-len(s2))>1:
        return False
    if len(s1)>len(s2):
        s1,s2 = s2,s1
    i=j=0
    edits = 0
    while i<len(s1) and j<len(s2):
        if s1[i] ==s2[j]:
            i+=1
            j+=1
        else:
            edits+= 1
            if edits>1:
                return False
            if len(s1) == len(s2):
                i+=1
            j+=1
    return True
s1 = input('Enter your first string:') 
s2 = input('Enter your second string:')
result = is_one_edit_away(s1,s2)
if result:
    print('Strings are one edit away from being same.')
else:
    print('String are not one edit away from being same.')