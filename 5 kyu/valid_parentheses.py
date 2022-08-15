def valid_parentheses(string):
    #your code here
    stack = []
    opening = set('([{')
    closing = set(')]}')
    pair = {')' : '(' , ']' : '[' , '}' : '{'}
    for i in string :
        if i in opening :
            stack.append(i)
        if i in closing :
            if not stack :
                return False
            elif stack.pop() != pair[i] :
                return False
            else :
                continue
    if not stack :
        return True
    else :
        return False


def valid_parentheses_2(string):
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False