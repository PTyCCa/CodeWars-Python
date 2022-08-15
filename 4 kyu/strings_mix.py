def mix(s1, s2):
    hist = {}
    for ch in "abcdefghijklmnopqrstuvwxyz":
        val1, val2 = s1.count(ch), s2.count(ch)
        print(val1, val2)
        if max(val1, val2) > 1:
            which = "1" if val1 > val2 else "2" if val2 > val1 else "="
            hist[ch] = (-max(val1, val2), which + ":" + ch * max(val1, val2))
    return "/".join(hist[ch][1] for ch in sorted(hist, key=lambda x: hist[x]))


import string
from collections import Counter


def mix_2(s1, s2):
    store = []
    result = []
    for stringy in (s1, s2):
        store.append(Counter([x for x in stringy if x.islower()]))
    for count in range(2):
        result.append([k * v for k, v in store[count].items() if v > 1 and v >= store[(count + 1) % 2].get(k, 0)])
        result[-1].sort()
    return "/".join(
        sorted(
            ["1:{}".format(x) for x in result[0] if x not in result[1]] + ["2:{}".format(x) for x in result[1] if x not in result[0]] + ["=:{}".format(x) for x in result
    [0] if x in result[1]],
            key=len,
            reverse=True))

