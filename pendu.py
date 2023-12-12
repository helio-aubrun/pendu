import pygame
import random
import sys
pygame.init()
largeur, hauteur = 800, 600
blanc = (255, 255, 255)
noir = (0, 0, 0)
police = pygame.font.Font(None, 36)
with open("mots.txt", "r") as fichier_mots:
    mots = fichier_mots.read().splitlines()

def choisir_mot():
    return random.choice(mots).upper()

def afficher_mot(mot, lettres_trouvees):
    affichage = ""
    for lettre in mot:
        if lettre in lettres_trouvees:
            affichage += lettre + " "
        else:
            affichage += "_ "
    return affichage.strip()

def dessiner_pendu(tentatives_restantes):
    if tentatives_restantes == 7:
        pass
    elif tentatives_restantes == 6 :
        image = pygame.image.load("pendu.image\Le-Pendu1.png").convert_alpha()
        fenetre.blit(image, (600, 0))
    elif tentatives_restantes == 5 :
        image = pygame.image.load("pendu.image\Le-Pendu2.png").convert_alpha()
        fenetre.blit(image, (600, 0))
    elif tentatives_restantes == 4 :
        image = pygame.image.load("pendu.image\Le-Pendu3.png").convert_alpha()
        fenetre.blit(image, (600, 0))
    elif tentatives_restantes == 3 :
        image = pygame.image.load("pendu.image\Le-Pendu4.png").convert_alpha()
        fenetre.blit(image, (600, 0))
    elif tentatives_restantes == 2 :
        image = pygame.image.load("pendu.image\Le-Pendu5.png").convert_alpha()
        fenetre.blit(image, (600, 0))
    elif tentatives_restantes == 1 :
        image = pygame.image.load("pendu.image\Le-Pendu6.png").convert_alpha()
        fenetre.blit(image, (600, 0))
    elif tentatives_restantes == 0 :
        image = pygame.image.load("pendu.image\Le-Pendu7.png").convert_alpha()
        fenetre.blit(image, (600, 0))
    pygame.display.flip()

def jouer():
    mot_a_deviner = choisir_mot()
    lettres_trouvees = set()
    lettres_incorrectes = set()
    tentatives_restantes = 7
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                lettre = pygame.key.name(event.key)
                if lettre.isalpha():
                    lettre = lettre.upper()
                    if lettre not in lettres_trouvees and lettre not in lettres_incorrectes:
                        if lettre in mot_a_deviner:
                            lettres_trouvees.add(lettre)
                        else:
                            lettres_incorrectes.add(lettre)
                            tentatives_restantes -= 1
        mot_affiche = afficher_mot(mot_a_deviner, lettres_trouvees)
        texte_mot = police.render(mot_affiche, True, noir)
        fenetre.fill(blanc)
        fenetre.blit(texte_mot, (50, 50))
        texte_incorrect = police.render("Lettres incorrectes: {}".format(' '.join(lettres_incorrectes)), True, noir)
        fenetre.blit(texte_incorrect, (50, 150))
        dessiner_pendu(tentatives_restantes)
        if set(mot_a_deviner) <= lettres_trouvees:
            texte_gagne = police.render("Félicitations, vous avez gagné !", True, noir)
            fenetre.blit(texte_gagne, (50, 100))
            pygame.display.flip()
            pygame.time.wait(3000)
            return True
        if tentatives_restantes == 0:
            texte_perdu = police.render("Désolé, vous avez perdu. Le mot était : {}".format(mot_a_deviner), True, noir)
            fenetre.blit(texte_perdu, (50, 100))
            pygame.display.flip()
            pygame.time.wait(3000)
            return False
        pygame.display.flip()

def inserer_mot():
    nouveau_mot = ""
    inserer = True
    while inserer:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    inserer = False
                elif event.key == pygame.K_BACKSPACE:
                    nouveau_mot = nouveau_mot[:-1]
                else:
                    lettre = pygame.key.name(event.key)
                    if lettre.isalpha():
                        nouveau_mot += lettre
        fenetre.fill(blanc)
        texte_saisie = police.render("Entrez un nouveau mot : " + nouveau_mot, True, noir)
        fenetre.blit(texte_saisie, (50, 50))
        pygame.display.flip()
    with open("mots.txt", "a") as fichier_mots:
        fichier_mots.write("\n" + nouveau_mot.lower())

def afficher_menu():
    fenetre.fill(blanc)
    texte_titre = police.render("Menu", True, noir)
    fenetre.blit(texte_titre, (350, 50))
    texte_jouer = police.render("1. Jouer", True, noir)
    texte_inserer = police.render("2. Insérer un mot dans le fichier 'mots.txt'", True, noir)
    texte_quitter = police.render("3. Quitter", True, noir)
    fenetre.blit(texte_jouer, (50, 150))
    fenetre.blit(texte_inserer, (50, 200))
    fenetre.blit(texte_quitter, (50, 250))
    pygame.display.flip()

fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Jeu du Pendu")
while True:
    afficher_menu()
    choix = None
    while choix is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    choix = 1
                elif event.key == pygame.K_2:
                    choix = 2
                elif event.key == pygame.K_3:
                    pygame.quit()
                    sys.exit()
    if choix == 1:
        jouer()
    elif choix == 2:
        inserer_mot()