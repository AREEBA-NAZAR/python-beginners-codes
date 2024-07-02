def reverse(str):
    words =  str.split()
    reversed_words = [word[::-1] for word in words]
    reversed_string = ' ' .join(reversed_words)
    return reversed_string
print(reverse("This is an example!"))
print(reverse("double  spaces"))