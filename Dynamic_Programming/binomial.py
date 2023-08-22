def BC(n, k):
    if k == 0 or k == n:
        return 1
    else:
        # print(n, k)
        return BC(n - 1, k - 1) + BC(n - 1, k)
if __name__ == "__main__":
    print(BC(5,3))