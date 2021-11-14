#similar way to .lower()
#.lower() and .casefold() behave the same, but occasionally, they do not:
if __name__=='__main__':
    print('ς'.casefold()) #both ς and σ are the Greek letter sigma
    print('ς'.lower())  # however, lower recognizes them as different
    #if you intended to compare two equivalent Greek words, one using ς and other σ.
    print('ρμησ' == 'ρμης')
    print('ρμησ'.lower() == 'ρμης'.lower())
    print('ρμησ'.casefold() == 'ρμης'.casefold())
