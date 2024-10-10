numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers:
    if i > 1:      # простое число - это натуральное число n > 1
        is_prime = True
        for j in range(2, i):
            if i % j == 0 and i != j:    # and  для (2) тк простое число делется только на 1 и на само себя
                not_primes.append(i)
                is_prime = False
                break

        if is_prime == True:
            primes.append(i)

print('Primes:', primes)
print('Not Primes:', not_primes)