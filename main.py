from grille import Grille, BACKGROUND_COLOR
from robot import Robot

import pygame


if __name__ == "__main__":

    grille = Grille()
    robot = Robot()
    
    nb_essais = 1000
    game_over = False

    for essai in range(nb_essais):

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
            
            # if essai > nb_essais-10:
            grille.screen.fill(BACKGROUND_COLOR)
            grille.affichage(grille.coord_robot) 
            pygame.display.flip()

            # pygame.time.delay(500)
            grille.clock.tick(30)

            etat0 = grille.coord_robot
            action = robot.get_action(etat0)

            etat, rwd = grille.step(action)

            grille.gain.append(rwd)
            for i in grille.gain:
                Gain = robot.gamma**i * grille.gain[i]
            if Gain < -20:
                game_over = True

            
            robot.update_Q_table(etat0, action, rwd, etat, game_over)
            etat0 = etat
        print(f"partie {essai}/{nb_essais}. Gain total : {Gain}")
        grille.reset()

    pygame.quit()
        
