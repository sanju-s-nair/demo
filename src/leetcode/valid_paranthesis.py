def isValid(s):
    close_to_open = {
        ")" : "(",
        "]" : "[",
        "}" : "{"
    }

    stack = []

    for brackets in s:
        if brackets in close_to_open:
            #closing bracket
            if not stack:
                return False
            top = stack.pop()
            if close_to_open[brackets] != top:
                return False
        else:
            #opening bracket
            stack.append(brackets)
    if stack:
        return False
    else:
        return True

print(isValid("([])"))
