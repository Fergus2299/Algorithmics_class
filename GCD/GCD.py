'''
Greatest common denominator (assumes positive ints)
'''

# intuitive approach
def GCD(n, m):
    i = min(n, m)

    while  n % i != 0 or  m % i != 0:
        i -= 1
    return i

def Euclid(n, m):
    while m > 0:
        t = n % m
        n = m
        m = t
    return n


if __name__ == "__main__":
    print(Euclid(9,54))