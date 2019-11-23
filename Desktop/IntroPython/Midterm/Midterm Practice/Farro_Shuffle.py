
#in shuffle and out shuffle will just be the inverse starting point
#out shuffle means first half then second half of deck
#in shuffle means second half then first half of the deck

def slice(d): #Function slices the deck in half
    B, C = d[:int(len(d) / 2 )], d[int(len(d) / 2):]
    return B,C


def weave(d,t):
    B, C = slice(d) # Bring back the slicing function within the weaving function for future loops
    if t == "out":
        list=([a for b in zip(B, C) for a in b]) #performs an out shuffle
        return list
    if t=="in":
        list=([a for b in zip(C,B) for a in b])#performs an in shuffle
        return list
    else:
        return "Shuffle can only be 'in' or 'out'! That's the point of a faro shuffle!"


def single_faro_shuffle(d,t): #function presents on complete faro shuffle
    list = weave(d, t)
    return list


def faro_shuffle(d,n,t): #function completes multiple faro shuffles
    ps = d
    if type(n)== int:
        for i in range (n):
            ps = single_faro_shuffle(ps,t)
        return ps
    else:
        return "n must be an integer!"





cards = [n for n in range(0,52)]
donald= [1,2,3]

print("Single faro in shuffle = \n", faro_shuffle(cards,4,"in"), "\n")

print(type(cards))





