import re 

#pyramid logic
s=input()
t=input()
try:
    for _ in range(int(input())):
        q=int(input())
        totStr=q//len(s)
        dif=abs(q-len(s))
        pyr_str=totStr*s+s[:dif]

        #counting logic
        ans=re.subn(t,t,pyr_str,flags=re.IGNORECASE)
        print(ans[-1])
except:
    pass

