# 0 1 2 3 4 5 6 7  8  9  10 ... <- index
# 0 1 1 2 3 5 8 13 21 34 55 ... <- Fibonacci number
# ^^^
# base cases
#
# fib(0): 0
# fib(1): 1
# fib(n): fib(n - 1) + fib(n - 2)
​


def fib(n):
    # Base case
    if n == 0:
        return 0
    if n == 1:
        return 1


    # if n <= 1: return n
​
return fib(n-1) + fib(n-2)  # O(2^n)
​
for i in range(100):
    print(f'{i}: {fib(i)}')
