def closest_higher_mod_5(x):
    if x % 5 == 0:
        return x
    else:
        y = x % 5
    return x + (5 - y)
