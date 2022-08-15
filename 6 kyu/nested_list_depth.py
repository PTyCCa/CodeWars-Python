def depth_2(l):
    return isinstance(l, list) and max(map(depth, l)) + 1 if l else 1 

def list_depth(l):
    if l == []:
        return 1
    if isinstance(l, list):
        return 1 + max(list_depth(item) for item in l)
    return 0

def list_depth_3(l):
    depths = [1]
    for x in l:
        if isinstance(x, list):
            depths.append(list_depth(x) + 1)
    return max(depths)