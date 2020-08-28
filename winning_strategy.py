for _ in range(int(input())):
    num=int(input())
    arr=list(map(int,input().split()))
    n=len(arr)
    if n==1:
        print('first')
    elif n==2:
        print('draw')
    elif n>=3: 
        if (n-3)%2==0:
            print('second')
        elif (n-3)%2!=0:
            print('draw')
