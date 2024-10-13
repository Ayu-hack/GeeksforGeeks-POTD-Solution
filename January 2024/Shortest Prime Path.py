from collections import deque
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes():
    primes = []
    for i in range(1000, 10000):
        if is_prime(i):
            primes.append(i)
    return primes

def solve(num1, num2):
    if num1 == num2:
        return 0
    primes_set = set(generate_primes())
    queue = deque([(num1, 0)])  
    visited = set([num1])
    while queue:
        current, steps = queue.popleft()
        current_str = str(current)
        for i in range(4):
            for d in '0123456789': 
                if d != current_str[i]: 
                    new_num_str = current_str[:i] + d + current_str[i+1:]
                    new_num = int(new_num_str)
                    if new_num in primes_set and new_num not in visited:
                        if new_num == num2:
                            return steps + 1
                        visited.add(new_num)
                        queue.append((new_num, steps + 1))
    return -1
