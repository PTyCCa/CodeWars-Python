def last(s):
    #your code here
    return sorted(s.split(" "), key = lambda x: x[-1])