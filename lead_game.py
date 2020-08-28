# cook your dish here
lst=[0,0]
leaders=[]
try:
    for _ in range(int(input())):
        scores=list(map(int,input().split()))
        lst[0]=lst[0]+scores[0]
        lst[1]=lst[1]+scores[1]
        if lst[0]>lst[1]:
            leaders.append((1,lst[0]-lst[1]))
        else:
            leaders.append((2,lst[1]-lst[0]))
    leaders=sorted(leaders,key=lambda leaders:leaders[1],reverse=True)
    if leaders[0][0]==1:
        print(1,leaders[0][1])
    else:
        print(2,leaders[0][1])  
except:
    pass