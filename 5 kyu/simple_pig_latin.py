def pig_it(text):
    #your code heres
    split_text = text.split(" ")
    res = []
    for i in split_text:
        if i.isalpha():
            res.append(f"{i[1:]}{i[0]}ay")
        else:
            res.append(i)

    return " ".join(res)


def pig_it_2(text):
    return " ".join(x[1:] + x[0] + "ay" if x.isalnum() else x for x in text.split())