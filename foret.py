import random
import pygame
import sys
from dragonnet import Dragonnet
from humain import Humain
from loup import Loup
from nain import Nain
from orque import Orque

class Foret:
    def __init__(self):
        self.heros = []
        self.monstres = []
        self.taille_case = 50
        self.largeur = 800
        self.hauteur = 600
        pygame.init()
        self.ecran = pygame.display.set_mode((self.largeur, self.hauteur))
        pygame.display.set_caption("Forêt de Shorewood")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 24)

    def ajouter_hero(self, hero):
        self.heros.append(hero)
        hero.x = random.randint(0, self.largeur // self.taille_case - 1) * self.taille_case
        hero.y = random.randint(0, self.hauteur // self.taille_case - 1) * self.taille_case

    def ajouter_monstre(self, monstre):
        self.monstres.append(monstre)
        monstre.x = random.randint(0, self.largeur // self.taille_case - 1) * self.taille_case
        monstre.y = random.randint(0, self.hauteur // self.taille_case - 1) * self.taille_case

    def dessiner(self):
        self.ecran.fill((34, 139, 34))  
        for hero in self.heros:
            pygame.draw.rect(self.ecran, (0, 0, 255), (hero.x, hero.y, self.taille_case, self.taille_case))
            texte = self.font.render(f"PV: {hero._Personnage__pv}", True, (255, 255, 255))
            self.ecran.blit(texte, (hero.x, hero.y - 20))
        for monstre in self.monstres:
            pygame.draw.rect(self.ecran, (255, 0, 0), (monstre.x, monstre.y, self.taille_case, self.taille_case))
            texte = self.font.render(f"PV: {monstre._Personnage__pv}", True, (255, 255, 255))
            self.ecran.blit(texte, (monstre.x, monstre.y - 20))
        pygame.display.flip()

    def deplacer_hero(self, hero, dx, dy):
        nouvelle_x = hero.x + dx * self.taille_case
        nouvelle_y = hero.y + dy * self.taille_case
        if 0 <= nouvelle_x < self.largeur and 0 <= nouvelle_y < self.hauteur:
            hero.x = nouvelle_x
            hero.y = nouvelle_y

    def trouver_monstre_a_position(self, x, y):
        for monstre in self.monstres:
            if monstre.x == x and monstre.y == y:
                return monstre
        return None

    def combat(self):
        tour_hero = 0
        while self.heros and self.monstres:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    hero = self.heros[tour_hero]
                    if event.key == pygame.K_UP:
                        self.deplacer_hero(hero, 0, -1)
                    elif event.key == pygame.K_DOWN:
                        self.deplacer_hero(hero, 0, 1)
                    elif event.key == pygame.K_LEFT:
                        self.deplacer_hero(hero, -1, 0)
                    elif event.key == pygame.K_RIGHT:
                        self.deplacer_hero(hero, 1, 0)
                    elif event.key == pygame.K_SPACE:
                        monstre = self.trouver_monstre_a_position(hero.x, hero.y)
                        if monstre:
                            hero.frappe(monstre)
                            if monstre.est_mort():
                                hero.depouiller(monstre)
                                self.monstres.remove(monstre)
                            else:
                                monstre.frappe(hero)
                                if hero.est_mort():
                                    self.heros.remove(hero)
                    elif event.key == pygame.K_h:
                        hero.se_soigner()
                    
                    tour_hero = (tour_hero + 1) % len(self.heros)

            self.dessiner()
            self.clock.tick(60)

        self.afficher_resultats()

    def afficher_resultats(self):
        self.ecran.fill((0, 0, 0))
        font = pygame.font.Font(None, 36)
        if self.heros:
            for i, hero in enumerate(self.heros):
                texte = font.render(f"Héros {i+1}: {hero.or_possede} or, {hero.cuir_possede} cuir", True, (255, 255, 255))
                self.ecran.blit(texte, (10, 10 + i * 40))
        else:
            texte = font.render("Tous les héros sont morts.", True, (255, 255, 255))
            self.ecran.blit(texte, (10, 10))
        
        pygame.display.flip()
        
        attente = True
        while attente:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    attente = False
                if event.type == pygame.KEYDOWN:
                    attente = False
        
        pygame.quit()