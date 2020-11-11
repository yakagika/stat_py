

def max2(xs):
    tmp = xs[0]
    for i in range(1, len(xs)):
        if xs[i] >= tmp:
            tmp = xs[i]
    return tmp


def max3(xs):
    if len(xs) == 0:
        return []
    elif len(xs) == 1:
        return xs[0]
    elif xs[0] >= max3(xs[1:]):
        return xs[0]
    else:
        return max3(xs[1:])


def and_list(xs):
    res = xs[0]
    for x in xs:
        res = x and res
    return res

def max4(xs):
    return [x for x in xs if and_list([x >= y for y in xs])]
