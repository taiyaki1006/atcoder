al = 0
bo = 0
count = 0

n = int(input())
a = [int(x) for x in input().split()]

a = sorted(a, reverse=True)
for i in a:
    count += 1
    if count%2==1:
        al += i
    else:
        bo += i

print(al-bo)