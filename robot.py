import random

class Robot:
    def __init__(self):
        self.Q_table = {}
        self.gamma = 0.9    # importance du futur, très important pour aller vers gros bonus
        self.alpha = 0.1      # besoin de bcp d'essais pour adopter une bonne route, pas très influençable par le little bonus
        self.epsilon = 0.5      # 1/2 chance de faire action random au départ poru explorer presque partout
        self.epsilon_min = 0.01  # tendre vers un epsilon très petit pour avoir très peu de hasard une fois le chemin optimal trouvé. (mieux 0.01 que 0.05 pour 1000 et 10 000 essais)
        self.epsilon_minus = 0.0005  # faire baisser epsilon très doucement mais pas trop (0.0005 mieux que 0.0001 pour 1000 et 10 000 essais)

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
