def insertionSort(A):
    for j in range(1, len(A)):
        temp = A[j]
        i = j - 1 
        while i >= 0 and A[i] > temp:
            A[i + 1] = A[i] # move up
            i -= 1
        A[i + 1] = temp
    return A
    

if __name__=='__main__':
    print(insertionSort([5,6,7,8,1,2,3]))
