def unique(sequence):
    if not sequence:
        return[]
    unique_list= [sequence[0]]
    
    for item in sequence[1:]:
        if item != unique_list[-1]:
            unique_list.append(item)
    return unique_list

result1=unique('AAAABBBCCDAABBB')
print(result1)
result2=unique('ABBCcAD') 
print(result2)
result3=unique([1, 2, 2, 3, 3]) 
print(result3)
        