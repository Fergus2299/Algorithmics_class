def BinSearch(arrA, i, j, x):
    if i==j:
        return i
    k = (i + j + 1) // 2
    if x < arrA[k]:
        return BinSearch(arrA, i, k - 1, x)
    else: return BinSearch(arrA, k, j, x)


if __name__=="__main__":
    arrA = [2,3,3,4,6,7,8,9]



    print(BinSearch(arrA, 1, len(arrA), 6))
