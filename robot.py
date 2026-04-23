import grille
import random

class Robot:
    def __init__(self):
        self.Q_table = {}
        self.gamma = 0.8
        self.alpha = 0.1
        self.epsilon = 0.15

    def get_action(self, etat):
        if etat not in self.Q_table:
            self.Q_table[etat] = [0, 0, 0]

        if random.uniform(0, 1) <= self.epsilon:
            return random.randint(0, 3)
        else:
            scores = self.Q_table[etat]
            return scores.index(max(scores))
        
    def update_Q_table(self, etat0, action, rwd, etat1, go):
        if etat0 not in self.Q_table:
            self.Q_table[etat0] = [0, 0, 0]
        
        


