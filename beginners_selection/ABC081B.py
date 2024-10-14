a = int(input())
result = 0
b = 0
count = 0
c = 0
list1=[int(x) for x in input().split()]
while count < 100:
    if(c==1):
        break
    count += 1
    d = 0
    for i in list1:
        if(i%2==0):
            b = i // 2
            list1[d:d+1] = [b]
            d += 1 
        else:
            c = 1
            break

print(count-1)