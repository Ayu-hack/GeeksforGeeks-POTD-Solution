def check_total_primes(N,M):
    prime_count = 0
    for num in range(N,M+1):
        if check_prime(num) == 1:
            prime_count += 1
    return prime_count
N,M = map(int, input().split())
print(check_total_primes(N,M))