# Importer les modules nécessaires
import pygame

# Initialiser pygame
pygame.init()

# Créer la fenêtre
pygame.display.set_caption("comet fall Game")
pygame.display.set_mode((1080, 720))

# insertion de l'arriere plan
ackground = pygame.image.load('bg.jpg')

# Boucle principale du jeu
running = True
while running:

    # Gérer les événement
    for event in pygame.event.get():
        # Ignorer les événements de type pygame.QUIT
        if event.type != pygame.QUIT:
            # Traiter les autres événements

    # Mettre à jour l'affichage
         pygame.display.update()

# Vérifier si l'utilisateur a cliqué sur le bouton de fermeture de la fenêtre
if pygame.event.get(pygame.QUIT):
    running = False

# Fermer la fenêtre
pygame.quit()
print("fermiture du jeu")


