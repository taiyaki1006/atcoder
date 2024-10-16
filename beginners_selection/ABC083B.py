n, a, b = map(int, input().split())

j = 0
result = 0

for i in range(n+1):
    j = sum(map(int, str(i)))
    if(j>=a and j<=b):
        result += i

print(result)