##UEFA
for _ in range(int(input())):
    
    team_pts={}
    team_gd_1={}
    team_gd_2={}
    team_gd={}
    
    for i in range(12):
        game_play=list(map(str,input().split()))
        
        HomeTeamGoals=int(game_play[1])
        AwayTeamGoals=int(game_play[3])
        
        #logic for goal difference    
        team_gd_1[game_play[0]]=team_gd_1.get(game_play[0],0)+(HomeTeamGoals-AwayTeamGoals)
        team_gd_2[game_play[4]]=team_gd_2.get(game_play[4],0)+(AwayTeamGoals-HomeTeamGoals)
        for k,v in team_gd_1.items():
            team_gd[k]=v+team_gd_2.get(k,0)
        
        #logic for pts(+3)
        if HomeTeamGoals>AwayTeamGoals:
            team_pts[game_play[0]]=team_pts.get(game_play[0],0)+3
        elif AwayTeamGoals>HomeTeamGoals:
            team_pts[game_play[4]]=team_pts.get(game_play[4],0)+3
        else:
            team_pts[game_play[0]]=team_pts.get(game_play[0],0)+1
            team_pts[game_play[4]]=team_pts.get(game_play[4],0)+1
    
    team_pts=sorted(team_pts.items(),key=lambda x:x[1],reverse=True)
    team_gd=sorted(team_gd.items(),key=lambda y: y[1],reverse=True)

    if team_pts[0][1]==team_pts[1][1]:
        print(team_gd[0][0],team_gd[1][0])
    else:
        print(team_pts[0][0],team_pts[1][0])
    
        
    

        
        
            
        

    

    
