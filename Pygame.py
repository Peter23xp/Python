import  pygame
pygame.init()

#generer la fenetre de notre jeu
pygame.display.set_caption("comet fall Game")
pygame.display.set_mode((500,300))

# impoter de charger l'arriere plan de notre jeu
background = pygame.image.load('asset/pelouse.jpg')

running = True

#boucle tant que cette condition est vrai
while running:

      # applique l'arriere plan de notre jeu
       screen.blit(pelouse, (0,0))

      # mettre a jour l'ecran
      pygame.display.flip()

      # si le joueur ferme cette fenetre
      for event in pygame.event.get():
        # que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
           running = False
           pygame.quit()
           print("ferture du jeu")


