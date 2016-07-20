def is_prime(n):
    for i in range(2, n//2):
        if not n%i:
            return False
    return True

def create_generator(func):
    def generator(seq):
        for s in seq:
            yield func(s)
    return generator

prime_generator = create_generator(is_prime)
for i, x in enumerate(prime_generator(range(100))):
    if x and i > 1:
        print(i)
