def test(n):
    if n%9==0:
        return n//9
    else:
        return (n//9)+1
try:
    for _ in range(int(input())):
        arr=list(map(int, input().split()))
        chef,rick=arr[0],arr[1]
        chef_score=test(chef)
        rick_score=test(rick)
        if chef_score<rick_score:
            print(0,chef_score)
        elif rick_score<chef_score:
            print(1,rick_score)
        elif rick_score==chef_score:
            print(1,rick_score)
except:
    pass