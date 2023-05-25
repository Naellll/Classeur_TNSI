# Possibilités d'améliorations :
# - nuage / fond d'écran animé
# - ajout d'un deuxième joueur
# - ajout de bonus (par exemple extension du carré)
# - préciser les collisions

import pyxel

class Jeu:

    def __init__(self):
        
        pyxel.init(128, 128, title="NDC")

        self.score = 0
        self.taille = 0

        self.x = 66
        self.y = 112

        self.largeur = 8
        self.hauteur = 8

        self.liste_fruit = []

        self.liste_bombe = []

        self.liste_bonus = []

        pyxel.load("theme.pyxres")
        pyxel.run(self.update, self.draw)



    def deplacement(self):

        if pyxel.btn(pyxel.KEY_Q) and self.x > 3:
            self.x -= 3
        if pyxel.btn(pyxel.KEY_D) and self.x+self.largeur < 127:
            self.x += 3



    def creation_fruit(self):
        
        if pyxel.frame_count > 31:
            if (pyxel.frame_count % 30 == 0):
                self.liste_fruit.append([pyxel.rndi(5, 118), -10, pyxel.rndi(0, 5)])

    def deplacement_fruit(self):

        for fruit in self.liste_fruit:
            fruit[1] += 1

            if fruit[1] > 135:
                self.liste_fruit.remove(fruit)



    def creation_bombe(self):
        
        if pyxel.frame_count > 106:
            if (pyxel.frame_count % 105-10*self.taille == 0):
                self.liste_bombe.append([pyxel.rndi(5, 123), -10])

    def deplacement_bombe(self):

        for bombe in self.liste_bombe:
            bombe[1] += 1

            if bombe[1] > 135:
                self.liste_bombe.remove(bombe)



    def collision(self):

        for fruit in self.liste_fruit:
            if fruit[0] <= self.x+self.largeur and fruit[0]+8 >= self.x and fruit[1] >= self.y-self.hauteur and fruit[1]+8 <= self.y+self.hauteur:
                pyxel.play(0, 0)
                self.score += (1+self.taille)*5
                self.liste_fruit.remove(fruit)

        for bombe in self.liste_bombe:
            if bombe[0] <= self.x+self.largeur and bombe[0]+8 >= self.x and bombe[1] >= self.y-self.hauteur and bombe[1]+8 <= self.y+self.hauteur:
                pyxel.play(0, 1)
                self.score -= 10*(self.taille+1)
                self.liste_bombe.remove(bombe)



    def modif_score(self):
        if self.score >= 100:
            pyxel.play(0, 2)
            self.taille += 1
            self.largeur *= 1.3
            self.hauteur *= 1.3
            self.score -= 100
        
        if self.score < 0:
            pyxel.play(0, 3)
            self.largeur /= 1.3
            self.hauteur /= 1.3
            self.taille -= 1
            self.score += 100



    def update(self):

        if self.taille >= 0 and self.taille < 6:

            self.deplacement()

            self.creation_fruit()
            self.deplacement_fruit()

            self.creation_bombe()
            self.deplacement_bombe()

            self.modif_score()

            self.collision()



    def draw(self):
        pyxel.cls(0)

        if self.taille >= 0 :

            pyxel.bltm(0, 0, 0, 0, 0, 128, 128)

            if pyxel.frame_count < 100:
                pyxel.text(15, 80, "Use 'Q' and 'D' to move !", 0)
            
            for fruit in self.liste_fruit:
                if fruit[2] == 0:
                    pyxel.blt(fruit[0], fruit[1], 0, 8, 0, 8, 8, 0)
                elif fruit[2] == 1:
                    pyxel.blt(fruit[0], fruit[1], 0, 0, 8, 8, 8, 0)
                elif fruit[2] == 2:
                    pyxel.blt(fruit[0], fruit[1], 0, 8, 8, 8, 8, 0)
                elif fruit[2] == 3:
                    pyxel.blt(fruit[0], fruit[1], 0, 0, 16, 8, 8, 0)
                else:
                    pyxel.blt(fruit[0], fruit[1], 0, 8, 16, 8, 8, 0)

            for bombe in self.liste_bombe:
                pyxel.blt(bombe[0], bombe[1], 0, 0, 0, 8, 8, 0)

            pyxel.rect(10, 15, 100, 8, 1)
            pyxel.rect(10, 15, self.score, 8, 11)
            pyxel.text(30, 16.25, f"Score : {self.score} / 100", 7)

            pyxel.rect(self.x, self.y+8-self.hauteur, self.largeur, self.hauteur, 1)

            pyxel.text(40, 5, f"Taille : {self.taille}/5", 7)

            if self.taille == 6:
                pyxel.cls(0)
                pyxel.text(50, 60, "VICTOIRE !", 7)

        else:
            pyxel.text(50, 60, "GAME OVER", 7)

Jeu()