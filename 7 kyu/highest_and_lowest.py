def high_and_low(numbers):
    num_list = list(map(int, numbers.split(" ")))
    max_num = max(num_list)
    min_num = min(num_list)

    return f"{max_num} {min_num}"


def high_and_low_2(numbers): #z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))


def high_and_low_3(numbers):
    nums = sorted(numbers.split(), key=int)
    return '{} {}'.format(nums[-1], nums[0])