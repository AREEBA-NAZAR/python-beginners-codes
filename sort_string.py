def sorted_string(input_str):
    if not input_str:
        return ""
    words= input_str.split()
    sorted_words = sorted(words, key=lambda word: int(''.join(filter(str.isdigit, word) or '0')))

    return ' '.join (sorted_words)
print(sorted_string("is2 Thi1s T4est 3a"))
print(sorted_string("4of Fo1r pe6ople g3ood th5e the2"))
print(sorted_string(""))