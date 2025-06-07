def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes_in_range(start, end):
    """Find all prime numbers in a given range."""

    numbers = range(start, end + 1)

    primes = filter(is_prime, numbers)

    return list(primes)

start = 10
end = 50
print(f"Prime numbers between {start} and {end} are: {find_primes_in_range(start, end)}")
