import random

class Robot:
    def __init__(self):
        self.Q_table = {}
        self.gamma = 0.8
        self.alpha = 0.1
        self.epsilon = 0.5
        self.epsilon_min = 0.05 # tendre vers ub epsilon très petit pour avoir très peu de hasard une fois le chemin optimal trouvé. 
        self.epsilon_minus = 0.001  # faire baisser epsilon très doucement 

    def get_action(self, etat):
        if etat not in self.Q_table:
            self.Q_table[etat] = [0, 0, 0, 0]

        if random.uniform(0, 1) <= self.epsilon:
            return random.randint(0, 3)
        else:
            scores = self.Q_table[etat]
            return scores.index(max(scores))
        
    def update_Q_table(self, etat0, action, rwd, etat1, go):
        if etat0 not in self.Q_table:
            self.Q_table[etat0] = [0, 0, 0, 0]
        
        if etat1 not in self.Q_table:
            self.Q_table[etat1] = [0, 0, 0, 0]
        
        scores0 = self.Q_table[etat0]

        new_score = scores0[action]

        if go:
            max_new_score = 0
        else:
            max_new_scores = self.Q_table[etat1]
            max_new_score = max(max_new_scores)

        self.Q_table[etat0][action] = new_score + self.alpha*(rwd + self.gamma * max_new_score - new_score)
