def unnecessary_complexity(x):
    if x == True:
        return True
    else:
        return False

def redundant_code(a, b):
    sum = a + b
    if sum > 0:
        return True
    if sum <= 0:
        return False

def magic_numbers():
    return 86400 * 7

def long_method(a, b, c, d, e, f, g):
    result = a + b - c
    result = result * d
    result = result / e
    if result > f:
        return result - g
    else:
        return result + g

def global_variable():
    global counter
    counter += 1
    return counter

counter = 0

def repeated_code():
    x = 5
    y = x * 2
    z = y + 3

    a = 7
    b = a * 2
    c = b + 3

    return z, c