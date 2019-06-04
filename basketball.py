import random as rn
import threading as th

class Teams:
    def __init__(self, players, quaters):
        self.players = players
        self.quaters = quaters
        _gametime = 12 

    def score_rand(self):
        player = self.players
        player_list = list(player.keys())
        rn.shuffle(player_list)
        player[player_list[0]] += rn.randint(0,3)

    def score_summary(self):
        players = self.players
        summary = 0
        for key, values in players.items():
            summary += values
        return summary
        

def game():
    team1 = {"Stephen Curry": 0, "Andre Igudala": 0, "Kevin Durant": 0}
    team2 = {"Kwahi Leonard": 0, "Lowry": 0, "Siakim": 0}

    gsw = Teams(team1, 4)
    tor = Teams(team2, 4)

    for i in range(12):
        t1 = th.Thread(gsw.score_rand())
        t2 = th.Thread(tor.score_rand())

    print ("Golden State Score", gsw.score_summary())
    print ("Toronto Summary", tor.score_summary())

    print (gsw.players)
    print (tor.players)

game()