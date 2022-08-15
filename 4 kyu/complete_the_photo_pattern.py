m = '   + +   \n  +o o+  \n +  u  + \n  + ~ +  \n    |    \n  +-o-+  \n_/| o |\\_\n  +-o-+  \n   | |   \n   I I   '
print(m)

n = enumerate(m.split("\n"))
c = {}
for i, j in n:
    c[i] = j

print(c)

height = [2, 3, 1]


