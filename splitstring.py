def break_cammel_case(string):
    result=""
    for char in string:
        if char.isupper():
            result += ' ' + char
        else:
            result += char
    return result.lstrip() if result else "Empty String"
print(break_cammel_case("camelCasting"))
print(break_cammel_case("identifier"))
print(break_cammel_case(""))