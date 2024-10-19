a = 0
count = 0

n = int(input())
d = [int(input()) for _ in range(n)]
d = sorted(d)
for i in d:
    if a<i:
        count += 1
    a = i
print(count)