def caching_fibonacci(n, cache={}):

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci(n)


print(caching_fibonacci(10))