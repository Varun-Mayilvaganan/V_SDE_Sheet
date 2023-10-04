#Card Swipe

for i in range(int(input())):
    a = int(input())
    lis = list(map(int,input().split()))
    b = 1
    newlist = set()
    for j in range(a):
        if lis[j] not in newlist:
            newlist.add(lis[j])
        else:
            newlist.remove(lis[j])
        b = max(b, len(newlist))
    print(b)    
