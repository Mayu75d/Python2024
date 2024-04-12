def stats_per_players(names, goals, goals_avoided, assists):
    names = names.split(',')
    players = {}
    for name, goals_scored, avoided, assist in zip(names, goals, goals_avoided, assists):
        players[name] = (goals_scored, avoided, assist)
    return players

def find_top_scorer(players):
    top_scorer = max(players.items(), key=lambda item: item[1][0]) 
    return top_scorer[0], top_scorer[1][0] 

def most_influential_player(players):
    most_influential = max(players.items(), key=lambda item: item[1][0] * 1.5 + item[1][1] * 1.25 + item[1][2] * 1)
    return most_influential[0]

def team_average(goals):
    ta = sum(goals) / 25  
    return ta

def top_scorer_average(players):
    _, goals = find_top_scorer(players)
    return goals / 25  


