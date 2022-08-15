def hex_to_rgb(color):
    return tuple(int(color.lstrip("#")[i:i+2], 16) for i in (0, 2, 4))


def brightest_2(colors):
    return sorted(enumerate(map(max, list(map(hex_to_rgb, colors)))), key = lambda x: (x[1], -x[0]), reverse=True)


# String comparison is enough, no need to convert
def brightest(colors):
    return max(colors, key=lambda c:max(c[1:3], c[3:5], c[5:]))