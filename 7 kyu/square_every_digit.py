def square_digits(num):
    return int(''.join([str(n) for n in [int(x)**2 for x in str(num)]]))


def square_digits_2(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)