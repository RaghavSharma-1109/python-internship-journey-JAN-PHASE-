def calculate_bill(amount,gst=18):
    if not isinstance(amount,(int,float)):
        return 'Amount must be a number'
    if not isinstance(gst,(int,float)):
        return 'GST must be a number'

    if amount<=0:
        return 'Amount must be greater than 0'
    
    total = amount + amount*(gst/100)
    return total

bill1 = calculate_bill(1000,3)
print(bill1)