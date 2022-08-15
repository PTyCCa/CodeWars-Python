def narcissistic(value):
    # Code away
    num_length = len(str(value))
    sum = 0
    for i in str(value):
        sum += int(i) ** num_length
    return sum == value


def narcissistic_2(value):
    return value == sum(int(x) ** len(str(value)) for x in str(value))