def fibonacci(num, x=None):
    """Return Fibonacci of num using recursion and memoization."""
    if x is None:
        x = [None] * (num + 1)
    if not num:
        return 0
    if num == 1:
        return 1
    if x[num] is not None:
        return x[num]
    x[num] = fibonacci(num - 1, x) + fibonacci(num - 2, x)
    return x[num]

n = int(input())
print(fibonacci(n))
