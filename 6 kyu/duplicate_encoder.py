from collections import Counter


def duplicate_encode(word):
    #your code here
    str_counter = Counter(word.lower())
    encoded_string = ""
    for ch in word.lower():
        if str_counter[ch] > 1:
            encoded_string += ")"
        else:
            encoded_string += "("
    return encoded_string


def duplicate_encode_2(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])
