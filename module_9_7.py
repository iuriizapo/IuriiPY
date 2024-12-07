def is_prime(func):
    def wrapper(*args):
        n = func(*args)
        prime = True
        i = 2
        while i <= n**0.5:
            if n % i == 0:
                prime = False
                break
            i += 1
        if prime:
            print('Простое')
        else:
            print('Составное')
        return n
    return wrapper

@is_prime
def sum_three(*args):
    res = sum(args)
    return res


result = sum_three(2, 3, 6)
print(result)


