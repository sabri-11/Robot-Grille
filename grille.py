import pygame
import random

ROBOT_COLOR = (39, 111, 245)
BACKGROUND_COLOR = (40, 91, 56)
MALUS_COLOR = (255, 0, 25)
BONUS_COLOR = (0, 255, 25)
LITTLE_BONUS_COLOR = (242, 245, 39)
GRILLE_COLOR = (0, 0, 0)

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

        self.grille = [(i, j) for i in range(self.nb_cases_x) for j in range(self.nb_cases_y)]

        pygame.display.set_caption("Robot chercheur")
        self.clock = pygame.time.Clock()

        

    def affichage(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.dessiner_grille()
        self.dessiner_robot()
        self.dessiner_malus()
        self.dessiner_little_bonus()
        self.dessiner_bonus()
        pygame.display.flip()

    def dessiner_grille(self):

        for ligne in range(self.nb_cases_x+1):
            debut_ligne_vert = (self.xt + (ligne*self.t_cases), self.yt)
            fin_ligne_vert = (self.xt + (ligne*self.t_cases), self.yt + self.nb_cases_y*self.t_cases)

            pygame.draw.line(self.screen, GRILLE_COLOR, debut_ligne_vert, fin_ligne_vert, int(1/10*self.t_cases))
        for col in range(self.nb_cases_y+1):
            debut_ligne_hor = (self.xt, self.yt + (col*self.t_cases))
            fin_ligne_hor = (self.xt + self.nb_cases_x*self.t_cases, self.yt + (col*self.t_cases))

            pygame.draw.line(self.screen, GRILLE_COLOR, debut_ligne_hor, fin_ligne_hor, int(1/10*self.t_cases))

    def dessiner_robot(self, x_grid=0, y_grid=0):

        center_x = self.xt + (x_grid * self.t_cases) + (self.t_cases // 2)
        center_y = self.yt + (y_grid * self.t_cases) + (self.t_cases // 2)

        pt_1 = (center_x - (self.t_robot // 2), center_y + (self.t_robot // 2))
        pt_2 = (center_x + (self.t_robot // 2), center_y + (self.t_robot // 2))
        pt_3 = (center_x, center_y - (self.t_robot // 2))
        

        pygame.draw.polygon(self.screen, ROBOT_COLOR, [pt_1, pt_2, pt_3])

    def dessiner_malus(self):
        x1, y1 = 1, 1
        x2, y2 = 3, 2
        x3, y3 = 1, 3

        center_x1 = self.xt + (x1 * self.t_cases) + (self.t_cases // 2)
        center_y1 = self.yt + (y1 * self.t_cases) + (self.t_cases // 2)

        center_x2 = self.xt + (x2 * self.t_cases) + (self.t_cases // 2)
        center_y2 = self.yt + (y2 * self.t_cases) + (self.t_cases // 2)

        center_x3 = self.xt + (x3 * self.t_cases) + (self.t_cases // 2)
        center_y3 = self.yt + (y3 * self.t_cases) + (self.t_cases // 2)

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
    

    def dessiner_little_bonus(self):

        taille = self.t_cases // 3

        cx = self.xt + (2 * self.t_cases) + (self.t_cases // 2) - (taille // 2)
        cy = self.yt + (2 * self.t_cases) + (self.t_cases // 2) - (taille // 2)
        
        pygame.draw.rect(self.screen, LITTLE_BONUS_COLOR, (cx, cy, taille, taille))
    

    def dessiner_bonus(self):

        x, y = 4, 4
        center_x = self.xt + (x * self.t_cases) + (self.t_cases // 2)
        center_y = self.yt + (y * self.t_cases) + (self.t_cases // 2)

        pygame.draw.circle(self.screen, BONUS_COLOR, (center_x, center_y), self.t_robot // 2)

    def reset(self):
        self.gain = 0
        self.dessiner_robot()

    def step(self):
        pass
        
    


        


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
    
        grille.affichage()
        grille.clock.tick(15)
        