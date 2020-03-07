def fib(n):
    yield 0
    if n > 0: yield 1
    last = 0
    next = 1
    for _ in range(1,n):
        last, next = next, last + next
        yield next

if __name__ == "__main__":
    for i in fib(6):
        print(i)

# use tuples instead of temporal variavels
