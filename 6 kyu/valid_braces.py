def valid_braces(string):
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


def validBraces_2(string):
    braces = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for character in string:
        if character in braces.keys():
            stack.append(character)
        else:
            if len(stack) == 0 or braces[stack.pop()] != character:
                return False
    return len(stack) == 0


def validBraces_3(s):
  while '{}' in s or '()' in s or '[]' in s:
      s=s.replace('{}','')
      s=s.replace('[]','')
      s=s.replace('()','')
  return s==''