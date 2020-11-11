

def max3(xs):
    if len(xs) == 0:
        return []
    elif len(xs) == 1:
        return xs[0]
    elif xs[0] >= max3(xs[1:]):
        return xs[0]
    else:
        return max3(xs[1:])
