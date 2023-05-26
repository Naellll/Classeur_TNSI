import pyxel

class Jeu:

    def __init__(self):
        
        pyxel.init(320, 240, title="np")

        self.vitesse_creation_ennemis = 50
        self.vitesse_tir = 10
        self.max_munition = 8
        self.munition = 8
        self.vide = False
        self.vitesse_recharge = 10
        self.degat = 0
        self.degat_souris = 3
        self.vitesse_ennemi = 1
        self.ennemi_selection = False
        self.ennemi_select = None
        self.liste_ennemi = []
        self.coin = 0
        self.menu = False

        pyxel.mouse(visible = True)
        pyxel.load("npedit.pyxres")
        pyxel.run(self.update, self.draw)


    def creation_ennemi(self):
        # création des ennemis avec une liste X, Y, et TYPE
        if (pyxel.frame_count % self.vitesse_creation_ennemis == 0):
            self.liste_ennemi.append({"id": (pyxel.frame_count-(pyxel.frame_count//10000)*10000),"X": -5, "Y": pyxel.rndi(40, 235),"vie": 5, "type": 0})

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

    def toucher_ennemi(self):
        if not self.vide:
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                self.munition -= 1
                for ennemi in self.liste_ennemi:
                    if ennemi["X"] < pyxel.mouse_x+7 and ennemi["X"]+7 > pyxel.mouse_x and ennemi["Y"] < pyxel.mouse_y+7 and ennemi["Y"]+7 > pyxel.mouse_y:
                            ennemi["vie"] -= self.degat_souris

    def recharger(self):
        if self.munition <= 0 or pyxel.btnp(pyxel.KEY_R):
            self.vide = True
        if self.vide and self.munition < self.max_munition and (pyxel.frame_count % self.vitesse_recharge == 0):
            self.munition += 1
        if self.munition == self.max_munition:
            self.vide = False


    def ennemi_mort(self):
        for ennemi in self.liste_ennemi:
            if ennemi["vie"] <= 0:
                self.liste_ennemi.remove(ennemi)
                self.ennemi_selection = False
                self.coin += 5

    def ouvrir_menu(self):
        if pyxel.mouse_x <= 185 and pyxel.mouse_x >= 125 and pyxel.mouse_y <= 20 and pyxel.mouse_y >= 5:
            if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
                self.menu = True
        if self.menu:
            if pyxel.mouse_x <= 255 and pyxel.mouse_x >= 245 and pyxel.mouse_y <= 55 and pyxel.mouse_y >= 45:
                if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
                    self.menu = False

    def update(self):
        self.ouvrir_menu()
        if not self.menu:
            self.recharger()
            self.creation_ennemi()
            self.deplacement_ennemi()
            self.viser_ennemi_front()
            self.toucher_ennemi()
            self.ennemi_mort()
    


    def draw(self):
        pyxel.cls(0)
        pyxel.bltm(0, 0, 0, 0, 0, 320, 240)

        for ennemi in self.liste_ennemi:
            pyxel.circ(ennemi["X"], ennemi["Y"], 5, 7)
            pyxel.rect(ennemi["X"]-5, ennemi["Y"]-10, 2*5, 3, 8)
            pyxel.rect(ennemi["X"]-5, ennemi["Y"]-10, 2*ennemi["vie"], 3, 11)

        pyxel.rect(130, 5, 60, 15, 4)
        pyxel.text(145, 10, "Upgrades", 10)

        pyxel.rect(5, 5, 120, 20, 5)
        for i in range(8):
            if self.munition > i:
                pyxel.blt(5+i*12, 7, 0, 0, 32, 16, 16, 1)
            else:
                pyxel.blt(5+i*12, 7, 0, 16, 32, 16, 16, 1)
        pyxel.blt(105, 8, 0, 32, 32, 16, 16, 1)
        if self.munition >= 8:
            pyxel.text(107, 13.5, f"+{self.munition-8}", 7)
        else:
            pyxel.text(107, 13.5, "+0", 7)

        pyxel.rect(270, 5, 45, 20, 5)
        pyxel.blt(272, 7, 0, 0, 16, 16, 16, 0)
        pyxel.text(290, 12, f"x{self.coin}", 7)

        if self.menu:
            pyxel.rect(60, 40, 200, 150, 4)
            pyxel.rect(245, 45, 10, 10, 8)
            pyxel.text(249, 48, "X", 7)

Jeu()