def flatten_list(nested_list):
    if not isinstance(nested_list):
        return 'Input must be a list'
    for i in nested_list:
        if isinstance(i,list):
            nested_list.remove(i)
            for num in i:
                nested_list.append(num)
    return nested_list

print(flatten_list([1, [2, 3], [4, [5, 6]], 7]
))        