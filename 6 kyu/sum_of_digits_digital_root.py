def digital_root(n):
    while n >= 10:
        n = sum(int(i) for i in str(n))

    return n


def digital_root_2(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))


def digital_root_3(n):
    return n%9 or n and 9 