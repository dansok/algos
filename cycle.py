# def periodicSequence(s0, a, b, m):
#     # tortoise and hare algorithm

#     def next(s, a, b, m):
#         return (a * s + b) % m
    
#     tortoise = next(s0, a, b, m)
#     hare = next(tortoise, a, b, m)
#     while tortoise != hare:
#         tortoise = next(tortoise, a, b, m)
#         hare = next(tortoise, a, b, m)
        
#     mu = 0
#     tortoise = s0
#     while tortoise != hare:
#         tortoise = next(tortoise, a, b, m)
#         hare = next(hare, a, b, m)
#         mu += 1
        
#     lam = 1
#     hare = next(tortoise, a, b, m)
#     while tortoise != hare:
#         hare = next(hare, a, b, m)
#         lam += 1

#     return lam


def periodicSequence(s0, a, b, m):

    def f(s, a, b, m):
        return (a * s + b) % m

    tortoise = f(s0, a, b, m)
    hare = f(f(s0, a, b, m), a, b, m)
    while tortoise != hare:
        tortoise = f(tortoise, a, b, m)
        hare = f(f(hare, a, b, m), a, b, m)  
    mu = 0
    tortoise = s0
    while tortoise != hare:
        tortoise = f(tortoise, a, b, m)
        hare = f(hare, a, b, m)
        mu += 1

    lam = 1
    hare = f(tortoise, a, b, m)
    while tortoise != hare:
        hare = f(hare, a, b, m)
        lam += 1
 
    return lam

def main():
    print periodicSequence(11, 2, 6, 12)


if __name__ == "__main__":
    main()
