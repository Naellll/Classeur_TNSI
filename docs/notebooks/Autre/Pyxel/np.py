import pyxel

class Jeu:

    def __init__(self):
        
        pyxel.init(320, 240, title="np")

        self.souris_X = 

        self.vitesse_creation_ennemis = 20
        self.vitesse_tir = 10
        self.degat = 1
        self.vitesse_ennemi = 1
        self.ennemi_selection = False
        self.ennemi_select = None
        self.liste_ennemi = []

        pyxel.load("npedit.pyxres")
        pyxel.run(self.update, self.draw)


    def creation_ennemi(self):
        # création des ennemis avec une liste X, Y, et TYPE
        if (pyxel.frame_count % self.vitesse_creation_ennemis == 0):
            self.liste_ennemi.append({"id": (pyxel.frame_count-(pyxel.frame_count//10000)*10000),"X": -5, "Y": pyxel.rndi(0, 240),"vie": 5, "type": 0})

    def deplacement_ennemi(self):
        # permet le déplacement vers la droite des ennemis avec X += self.vitesse_ennemi
        for ennemi in self.liste_ennemi:
            if ennemi["X"] < 200:
                ennemi["X"] += self.vitesse_ennemi

    def ennemi_front(self):
        front = 0
        id = self.liste_ennemi[0]["id"]
        for ennemi in self.liste_ennemi:
            if ennemi["X"] >= front:
                front = ennemi["X"]
                id = ennemi["id"]
        return id
    
    def viser_ennemi_front(self):
        if (pyxel.frame_count % self.vitesse_tir == 0):
            if self.ennemi_selection == False:
                for ennemi in self.liste_ennemi:
                    if ennemi["id"] == self.ennemi_front():
                        ennemi["vie"] -= self.degat
                        self.ennemi_select = ennemi["id"]
                        self.ennemi_selection = True
            else:
                for ennemi in self.liste_ennemi:
                    if ennemi["id"] == self.ennemi_select:
                        ennemi["vie"] -= self.degat

    def ennemi_mort(self):
        for ennemi in self.liste_ennemi:
            if ennemi["vie"] <= 0:
                self.liste_ennemi.remove(ennemi)
                self.ennemi_selection = False


    def update(self):
        self.creation_ennemi()
        self.deplacement_ennemi()
        self.viser_ennemi_front()
        self.ennemi_mort()
    


    def draw(self):
        pyxel.cls(0)
        pyxel.bltm(0, 0, 0, 0, 0, 320, 240)

        for ennemi in self.liste_ennemi:
            pyxel.circ(ennemi["X"], ennemi["Y"], 5, 7)
            pyxel.rect(ennemi["X"]-5, ennemi["Y"]-10, 2*5, 3, 8)
            pyxel.rect(ennemi["X"]-5, ennemi["Y"]-10, 2*ennemi["vie"], 3, 11)

        pyxel.blt(160, 10, 0, 0, 16, 16, 8, 0)


Jeu()