def solution(number):
    mul_set = set()
    for i in range(number):
        if i > 0 and i * 3 < number:
            mul_set.add(i * 3)
        if i > 0 and i * 5 < number:
            mul_set.add(i * 5)
            
    return sum(mul_set)


def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)