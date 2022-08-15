from collections import Counter

def find_it(seq):
    seq_counter = Counter(seq)
    for key, value in seq_counter.items():
        if value % 2 != 0:
            return key
    return None


def find_it_2(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i


def find_it_3(seq):
    return [x for x in seq if seq.count(x) % 2][0]