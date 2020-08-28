for _ in range(int(input())):
    a=list(map(int,input().split()))
    def scorer(h,p):
        if h<1 or p<1:
            return (h,p)
        h=h-p
        p=p/2
        return scorer(h,p)

    s=scorer(a[0],a[1])

    if s[0]<s[1]:
        print(1)
    else:print(0)

