def fib(n):
    last = 0
    next = 1
    for i in range(1,n):
        last, next = next, last + next
    return next

if __name__ == "__main__":
    print(fib(6))

# use tuples
