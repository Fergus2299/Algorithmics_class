import logging

logging.basicConfig(filename='quicksort.log', encoding='utf-8', level=logging.DEBUG)
def interchange(lst, a, b):
    '''

    :param lst: any list
    :param a: index of item
    :param b: index of item
    :return: list with two items at index a and b switched
    '''
    temp_val = lst[a]
    lst[a] = lst[b]
    lst[b] = temp_val
    return lst


def pivot(T):
    p = T[0]
    k = 0
    l = len(T) - 1
    while not(T[k] > p or k >= len(T)):
        k += 1
    while not T[l] <= p:
        l = l - 1
    while k < l:
        logging.debug(f'swapping {T[k]} with {T[l]}')
        T = interchange(T, k, l)
        logging.debug(f'new list: {T}')
        while not T[k] > p:
            k += 1
        while not T[l] <= p:
            l = l - 1
    T = interchange(T, 0, l)
    return T, l

if __name__=='__main__':
    print(pivot([5,6,7,8,1,2,3]))
