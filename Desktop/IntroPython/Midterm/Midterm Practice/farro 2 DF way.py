def split(d):
    mid = int(len(d) / 2)
    top = d[:mid]
    bottom = d[mid:]
    result = bottom + top
    return result


def shuffle(d, t):
    mid = int(len(d) / 2)
    top = d[:mid]
    bottom = d[mid:]
    result = []

    for i in range(0, mid):
        if t == "in":
            result.append(top[i])
            result.append(bottom[i])
        else:
            result.append(bottom[i])
            result.append(top[i])
        return result


def single_faro_shuffle(d, t):
    result = split(d)
    result = shuffle(d, t)
    return result


def faro_shuffle(d, n, t):
    ps = d
    for i in range(0, n):
        ps = single_faro_shuffle(ps, t)
        return ps

cards = [n for n in range(0,52)]

print("Single faro in shuffle = \n", faro_shuffle(cards,1,"in"), "\n")
print("Single faro out shuffle = \n", faro_shuffle(cards,1,"out"), "\n")
print("8 faro in shuffles = \n", faro_shuffle(cards,8,"in"), "\n")
print("26 faro out shuffles = \n", faro_shuffle(cards, 26, "out"), "\n")