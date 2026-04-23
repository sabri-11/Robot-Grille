from grille import Grille, BACKGROUND_COLOR
from robot import Robot

import pygame


if __name__ == "__main__":

    grille = Grille()
    robot = Robot()
    
    nb_essais = 10000
    nb_pas_max = 10
    game_over = False

    for essai in range(nb_essais):
        nb_pas = 0
        Gain = 0
        while not game_over:
            for event in pygame.event.get():
                # Permet de fermer la fenêtre avec la croix (si on n'est pas en plein écran)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                # ASTUCE : Permet de quitter le plein écran en appuyant sur Échap !
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()
            
            if essai > nb_essais-10:
                grille.affichage(grille.coord_robot)
                grille.clock.tick(3)

            # grille.affichage(grille.coord_robot)
            # grille.clock.tick(3)

            etat0 = grille.coord_robot
            action = robot.get_action(etat0)

            etat, rwd = grille.step(action)

            grille.gain.append(rwd)

            
            for i in range(len(grille.gain)):
                Gain += robot.gamma**i * grille.gain[i]
            if nb_pas > nb_pas_max:
                game_over = True

            
            robot.update_Q_table(etat0, action, rwd, etat, game_over)
            etat0 = etat
            nb_pas += 1

        print(f"partie {essai}/{nb_essais}. Gain total : {Gain}")
        grille.reset()
        if robot.epsilon > robot.epsilon_min:
            robot.epsilon -= robot.epsilon_minus
        game_over = False

    pygame.quit()
        
