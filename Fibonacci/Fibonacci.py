import timeit


def fib_recursive(n):
    if n <= 1:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n-2)

def fib_bottom_up(n):
    if n <= 1:
        return 1
    a = 1
    b = 1
    while n > 1:
        temp = b
        b += a
        a = temp

        # decrement
        n -= 1
    return b
def fib_memoisation(n):
    global memo
    memo = {}
    return fib_memoisation2(n)

def fib_memoisation2(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        res = 1
        memo[n] = res
        return res
    res = fib_memoisation2(n - 1) + fib_memoisation2(n-2)
    memo[n] = res
    return res


def test_execution_time(func, n):
    # Wrap the function to test with a lambda to pass the argument n
    wrapper = lambda: func(n)

    # Use timeit to measure execution time
    exec_time = timeit.timeit(wrapper, number=1)

    return exec_time

if __name__ == "__main__":
    n = 45  # or whatever value you'd like to test

    recursive_time = test_execution_time(fib_recursive, n)
    bottom_up_time = test_execution_time(fib_bottom_up, n)
    memoisation_time = test_execution_time(fib_memoisation, n)

    print(f"Recursive execution time for n={n}: {recursive_time:.6f} seconds")
    print(f"Bottom-up execution time for n={n}: {bottom_up_time:.6f} seconds")
    print(f"Memoisation execution time for n={n}: {memoisation_time:.6f} seconds")