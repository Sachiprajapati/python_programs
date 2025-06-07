def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def prime_numbers_upto(N):
    prime_list = []
    for num in range(2, N + 1):
        if is_prime(num):
            prime_list.append(num)
    return prime_list

N = int(input("Enter the value of N: "))
prime_list = prime_numbers_upto(N)

print("Prime numbers up to {N} are:")
for prime in prime_list:
    print(prime)
