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
    '''
    desc: the elements of the list are arranged into those greater than the pivot (chosen as the first element)
            and those lower.
    :param T: the list we want to pivot about
    :return: a list pivoted about the first element and the location of the pivot in the final list
    '''
    p = T[0]
    k = 0
    l = len(T) - 1
    while k < len(T) and T[k] <= p:
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
    logging.debug(f'swapping {T[0]} with {T[l]}')
    T = interchange(T, 0, l)
    logging.debug(f'new list: {T}')
    return T, l

def quicksort(T):
    if len(T) == 0:
        return T
    else:
        T, l = pivot(T)
        print("T", T, "l", l)
        a = quicksort(T[:l])
        b = quicksort(T[l+1:])
        return a + [T[l]] + b

if __name__=='__main__':
    print(quicksort([5,6,7,8,1,2,3]))
