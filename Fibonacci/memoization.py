memo = {0: 0, 1: 1} # bases cases

def fib(n):
    if n not in memo:
        memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

print(fib(6))
