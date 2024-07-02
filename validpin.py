def valid_pin(n):
    if n.isdigit() and (len(n)==4 or len(n)==6):
        return True
    else:
        return False
n=input("enter a pin:  ")
print(valid_pin(n))