
def moves(k,ar):
    for i in ar:
        if k%i==0:
            return i
    return -1 
try:
    for _ in range(int(input())):
        p,k=map(int,input().split())
        ar=map(int,input().split())
        ar=sorted(ar,reverse=True)
        print(moves(k,ar))
except:
    pass
            