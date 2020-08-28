for _ in range(int(input())):
    chef_score=0
    mon_score=0
    
    for i in range(int(input())):
        cards_inp=list(map(int,input().split()))
        chef_card=cards_inp[0]%10
        mon_card=cards_inp[1]%10
        
        if chef_card>mon_card:
            chef_score+=1
        elif mon_card>chef_card:
            mon_score+=1
        else:
            chef_score+=1
            mon_score+=1
    
    if chef_score>mon_score:
        print(0)
    elif chef_score<mon_score:
        print(1)
    else:
        print(2)
            
        


        
        
        
       
