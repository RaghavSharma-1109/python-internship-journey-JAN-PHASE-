def analyze_numbers(nums: list):
    if not isinstance(nums,list):
        return {
            'status': False,
            'message':'Input must be list',
            'data': None
        }
    if len(nums)==0:
        return {
            'status': False,
            'message':'List can not be empty',
            'data': None
        }
    positive = 0
    negative = 0
    zero =0
    total =0
    for num in nums:
        if not isinstance(num,(int,float)) or isinstance(num, bool):
            return {
            'status': False,
            'message':'Number must be integer or float (booleans not allowed)',
            'data': None
            }
        if num>0:
            positive+=1
             
        elif num<0:
            negative+=1
             
        elif num ==0:
            zero+= 1
        
        total += num
    average = round(total /len(nums),2)

    return {
            'status': True,
            'message':'All numbers Analyzes',
            'data': {
                'positive': positive,
                'negative': negative,
                'zero': zero,
                'total': total,
                'average': average
                }
            }