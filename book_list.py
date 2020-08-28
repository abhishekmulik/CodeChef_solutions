try:
    m=int(input())
    bks=list(map(int,input().split()))
    entries=int(input())
    for i in range(entries):
        entry=int(input())-1
        print(bks.pop(entry))
except:
    pass