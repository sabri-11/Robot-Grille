import pygame
import random

ROBOT_COLOR = (39, 111, 245)
BACKGROUND_COLOR = (40, 91, 56)
MALUS_COLOR = (255, 0, 25)
BONUS_COLOR = (0, 255, 25)
LITTLE_BONUS_COLOR = (242, 245, 39)
GRILLE_COLOR = (0, 0, 0)

DROITE = 0
HAUT = 1
GAUCHE = 2
BAS = 3

class Grille:
    def __init__(self):
        pygame.init()

        # self.l = info.current_w
        # self.h = info.current_h
        # ## Tests ###
        self.l = 1000
        self.h = 600

        # self.screen = pygame.display.set_mode((self.l, self.h), pygame.FULLSCREEN)
        self.screen = pygame.display.set_mode((self.l, self.h))

        self.nb_cases_x = self.nb_cases_y = 5
        self.nb_bonus_cases = 2
        self.nb_malus_cases = 2

        self.longeur_jeu = int(self.l*50/100)
        self.hauteur_jeu = int(self.h*50/100)

        self.t_cases = self.longeur_jeu // self.nb_cases_x
        
        self.xt = (self.l - (self.nb_cases_x * self.t_cases)) // 2
        self.yt = (self.h - (self.nb_cases_y * self.t_cases)) // 2

        self.t_robot = self.t_cases // 2
        self.coord_robot = (0, 0)

        self.grille = [(i, j) for i in range(self.nb_cases_x) for j in range(self.nb_cases_y)]

        self.gain = []

        ## Malus 
        m1 = (1, 1)
        m2 = (3, 2)
        m3 = (1, 3)
        self.coord_malus  = [m1, m2, m3]

        ## Bonus 
        self.coord_bonus = [(4, 4)]

        ## Little Bonus
        self.coord_little_bonus = [(2, 2)]



        pygame.display.set_caption("Robot chercheur")
        self.clock = pygame.time.Clock()

        

    def affichage(self, coords):
        
        self.dessiner_grille()
        self.dessiner_robot(coords)
        self.dessiner_malus(self.coord_malus[0], self.coord_malus[1], self.coord_malus[2])
        self.dessiner_little_bonus(self.coord_little_bonus[0])
        self.dessiner_bonus(self.coord_bonus[0])
        

    def dessiner_grille(self):

        for ligne in range(self.nb_cases_x+1):
            debut_ligne_vert = (self.xt + (ligne*self.t_cases), self.yt)
            fin_ligne_vert = (self.xt + (ligne*self.t_cases), self.yt + self.nb_cases_y*self.t_cases)

            pygame.draw.line(self.screen, GRILLE_COLOR, debut_ligne_vert, fin_ligne_vert, int(1/10*self.t_cases))
        for col in range(self.nb_cases_y+1):
            debut_ligne_hor = (self.xt, self.yt + (col*self.t_cases))
            fin_ligne_hor = (self.xt + self.nb_cases_x*self.t_cases, self.yt + (col*self.t_cases))

            pygame.draw.line(self.screen, GRILLE_COLOR, debut_ligne_hor, fin_ligne_hor, int(1/10*self.t_cases))

    def dessiner_robot(self, coords):

        center_x = self.xt + (coords[0] * self.t_cases) + (self.t_cases // 2)
        center_y = self.yt + (coords[1] * self.t_cases) + (self.t_cases // 2)

        pt_1 = (center_x - (self.t_robot // 2), center_y + (self.t_robot // 2))
        pt_2 = (center_x + (self.t_robot // 2), center_y + (self.t_robot // 2))
        pt_3 = (center_x, center_y - (self.t_robot // 2))
        

        pygame.draw.polygon(self.screen, ROBOT_COLOR, [pt_1, pt_2, pt_3])


    def dessiner_malus(self, m1, m2, m3):
        

        center_x1 = self.xt + (m1[0] * self.t_cases) + (self.t_cases // 2)
        center_y1 = self.yt + (m1[1] * self.t_cases) + (self.t_cases // 2)

        center_x2 = self.xt + (m2[0] * self.t_cases) + (self.t_cases // 2)
        center_y2 = self.yt + (m2[1] * self.t_cases) + (self.t_cases // 2)

        center_x3 = self.xt + (m3[0] * self.t_cases) + (self.t_cases // 2)
        center_y3 = self.yt + (m3[1] * self.t_cases) + (self.t_cases // 2)

        coord1 = (center_x1 - self.t_robot//2, center_y1 - self.t_robot//2)
        coord2 = (center_x2 - self.t_robot//2, center_y2 - self.t_robot//2)
        coord3 = (center_x3 - self.t_robot//2, center_y3 - self.t_robot//2)

        ep = int(1/10*self.t_cases)

        pygame.draw.line(self.screen, MALUS_COLOR, (coord1[0], coord1[1]), (coord1[0] + self.t_robot, coord1[1] + self.t_robot), ep)
        pygame.draw.line(self.screen, MALUS_COLOR, (coord1[0], coord1[1] + self.t_robot), (coord1[0] + self.t_robot, coord1[1]), ep)

        pygame.draw.line(self.screen, MALUS_COLOR, (coord2[0], coord2[1]), (coord2[0] + self.t_robot, coord2[1] + self.t_robot), ep)
        pygame.draw.line(self.screen, MALUS_COLOR, (coord2[0], coord2[1] + self.t_robot), (coord2[0] + self.t_robot, coord2[1]), ep)

        pygame.draw.line(self.screen, MALUS_COLOR, (coord3[0], coord3[1]), (coord3[0] + self.t_robot, coord3[1] + self.t_robot), ep)
        pygame.draw.line(self.screen, MALUS_COLOR, (coord3[0], coord3[1] + self.t_robot), (coord3[0] + self.t_robot, coord3[1]), ep)
    

    def dessiner_little_bonus(self, lb):

        taille = self.t_cases // 3

        cx = self.xt + (lb[0] * self.t_cases) + (self.t_cases // 2) - (taille // 2)
        cy = self.yt + (lb[1] * self.t_cases) + (self.t_cases // 2) - (taille // 2)
        
        pygame.draw.rect(self.screen, LITTLE_BONUS_COLOR, (cx, cy, taille, taille))
    

    def dessiner_bonus(self, b):

        center_x = self.xt + (b[0] * self.t_cases) + (self.t_cases // 2)
        center_y = self.yt + (b[1] * self.t_cases) + (self.t_cases // 2)

        pygame.draw.circle(self.screen, BONUS_COLOR, (center_x, center_y), self.t_robot // 2)

    def reset(self):
        self.gain = []
        self.dessiner_robot((0, 0))

    def step(self, action):
        if action == DROITE:
            new_coord_robot = (self.coord_robot[0]+1, self.coord_robot[1])
            reward = self.faire_action(new_coord_robot)
        elif action == HAUT:
            new_coord_robot = (self.coord_robot[0], self.coord_robot[1]-1)
            reward = self.faire_action(new_coord_robot)
        elif action == GAUCHE:
            new_coord_robot = (self.coord_robot[0]-1, self.coord_robot[1])
            reward = self.faire_action(new_coord_robot)
        elif action == BAS:
            new_coord_robot = (self.coord_robot[0], self.coord_robot[1]+1)
            reward = self.faire_action(new_coord_robot)
        
        return self.coord_robot, reward


    def faire_action(self, new_coord_robot):
        if self.est_dans_limites(new_coord_robot[0], new_coord_robot[1]):
                self.coord_robot = new_coord_robot
                
                return self.give_reward(new_coord_robot)
        else:
            return -1
            print(f"Mouvement impossible.")


    def est_dans_limites(self, x, y):
        return (x >= 0 and x < self.nb_cases_x and y >= 0 and y < self.nb_cases_y) 
            
    def give_reward(self, coords):
        if coords in self.coord_bonus:
            reward = 150
        elif coords in self.coord_little_bonus:
            reward = 10
        elif coords in self.coord_malus:
            reward = -10
        else:
            reward = -1
        
        return reward

    



if __name__ == "__main__":
    grille = Grille()
    running = True  
    while running:

        # 1. On écoute le système (évite que la fenêtre "plante")
        for event in pygame.event.get():
            # Permet de fermer la fenêtre avec la croix (si on n'est pas en plein écran)
            if event.type == pygame.QUIT:
                running = False
            # ASTUCE : Permet de quitter le plein écran en appuyant sur Échap !
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        # Déplacement avec les flèches
                if event.key == pygame.K_RIGHT:
                    grille.step(DROITE)
                elif event.key == pygame.K_LEFT:
                    grille.step(GAUCHE)
                elif event.key == pygame.K_UP:
                    grille.step(HAUT) 
                elif event.key == pygame.K_DOWN:
                    grille.step(BAS)
    
        
        # 2. DESSIN (On affiche l'état ACTUEL du robot)
        grille.screen.fill(BACKGROUND_COLOR)
        grille.affichage(grille.coord_robot) 
        pygame.display.flip() 
        
        grille.clock.tick(60)
    pygame.quit()


        