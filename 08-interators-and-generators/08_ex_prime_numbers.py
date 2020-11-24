def get_primes(sequence):
    for num in sequence:
        is_prime = True
        for x in range(2, num):
            if num % x == 0:
                is_prime = False
                break
        if is_prime and num not in (0, 1):
            yield num

print(list((get_primes([2, 4, 3, 5, 6, 9, 1, 0]))))