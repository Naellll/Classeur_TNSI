# Fonctions avec la classe Pile :

class Pile:

    '''classe Pile création d’une instance Pile avec une liste'''
    
    def __init__(self):
        '''Initialise une pile vide'''
        self.liste = []
        
    def est_vide(self):
        '''Renvoie un booléen, True si la pile est vide et False sinon'''
        return len(self.liste) == 0

    def empiler(self, element):
        '''Empile element au sommet de pile'''
        self.liste.append(element)

    def depiler(self):
        '''Renvoie et enlève la valeur du sommet de pile'''
        return self.liste.pop()

    def __repr__(self):
        return repr(self.liste)



def sommet(self):
    ''' Renvoie la valeur au sommet de la pile mais sans la supprimer de la pile '''
    assert not self.est_vide(), "La pile est vide"
    return self.liste[-1]



def mettre_disques(self, n):
    '''met des disques de taille n à 1 sur la pile'''
    for i in range(n, 0, -1):
        self.empiler(n)
        n -= 1
    return self.liste



def creation_tours(n):
    ''' renvoie une liste de 3 piles,
    la première correspond à la pile des n disques,
    les autres étant vides.'''
    p0 = Pile()
    p1 = Pile()
    p2 = Pile()
    mettre_disques(p0, n)
    return [p0, p1, p2]



def deplacer(self, origine, cible):
    '''
    déplace la valeur au sommet de la pile d’indice origine vers le sommet de la pile d’indice cible.
    Si le déplacement n’est pas possible, parce qu’il ne respecte pas les règles du jeu, les piles ne sont pas modifiées.
    '''
    if self[cible].est_vide() and not self[origine].est_vide():
        self[cible].empiler(self[origine].depiler())
    elif sommet(self[origine]) < sommet(self[cible]) and not self[origine].est_vide():
        self[cible].empiler(self[origine].depiler())



def resoudre(self, n, origine, cible, interm):
    if n == 0:
        return None
    else:
        resoudre(self, n-1, origine, interm, cible)
        deplacer(self, origine, cible)
        resoudre(self, n-1, interm, cible, origine)





# Fonctions avec les listes Python :

def creer_pile_liste():
    '''Renvoie une pile vide'''
    return []

def est_vide_liste(pile):
    '''Renvoie un booléen, True si la pile est vide et False sinon'''
    return p == []

def empiler_liste(pile, element):
    '''Empile element au sommet de pile'''
    pile.append(element)
    
def depiler_liste(pile):
    '''Renvoie et enlève la valeur du sommet de pile'''
    assert not est_vide(pile), "Pile vide"
    return pile.pop()



def sommet_liste(pile):
    ''' Renvoie la valeur au sommet de la pile mais sans la supprimer de la pile '''
    assert not est_vide(pile), "La pile est vide"
    return pile[-1]



def mettre_disques_liste(pile, n):
    '''met des disques de taille n à 1 sur la pile'''
    for i in range(n, 0, -1):
        empiler(pile, n)
        n -= 1
    return pile



def creation_tours_liste(n):
    ''' renvoie une liste de 3 piles,
    la première correspond à la pile des n disques,
    les autres étant vides.'''
    p0 = creer_pile_liste()
    p1 = creer_pile_liste()
    p2 = creer_pile_liste()
    mettre_disques_liste(p0, n)
    return [p0, p1, p2]





# Bonus :

def nb_etapes(n):
    return 2**n - 1