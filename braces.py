def fix_multi_digits(expr):
    import re
    tmp = re.split(r"(\*|\+|\-|/|\(|\)){1}", expr)
    tmp = list(filter(lambda x: x != " " and x, tmp))
    return tmp


def is_operator(val):
    if val == "+" or val == "-" or val == "/" or val == "*" or val == "(" or val == ")":
        return True
    return False


def braces(A):
    A = fix_multi_digits(A)
    stack = []
    for i in A:
        if is_operator(i):
            if i == ")":
                opt_count = 0
                for idx in range(len(stack)-1, 0, -1):
                    if stack[idx] != "(":
                        stack.pop()
                        opt_count += 1
                    else:
                        stack.pop()
                        break
                if opt_count == 0:
                    return 1
            else:
                stack.append(i)
    return 0


print(braces("((a + b))"))
