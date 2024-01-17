a, b = map(int, input().split())

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

if a <= b:
    count = sum(1 for i in range(a, b+1) if is_prime(i))
    print(f"main order - amount: {count}")
else:
    count = sum(1 for i in range(b, a+1) if is_prime(i))
    print(f"reverse order - amount: {count}")