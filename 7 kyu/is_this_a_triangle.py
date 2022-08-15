def is_triangle(a, b, c):
    if a >= 0 and b >= 0 and c >=0:
        if a + b > c and a + c > b and c + b > a:
            return True
    return False


def is_triangle_2(a, b, c):
    return (a < b + c) and (b < a + c) and ( c < a + b)


def is_triangle_3(a, b, c):
    a, b, c = sorted([a, b, c])
    return a + b > c