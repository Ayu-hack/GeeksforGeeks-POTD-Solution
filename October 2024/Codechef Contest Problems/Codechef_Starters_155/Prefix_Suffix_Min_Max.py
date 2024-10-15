t = int(input())

for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    max = 0

    for i in range(n-1):
        if (max<b[i+1]-b[i]):
            max = b[i+1]-b[i]
    
    print(max, end=" ")

    for i in range(n-1):
        print(b[i+1]-b[i], end=" ")

    print()