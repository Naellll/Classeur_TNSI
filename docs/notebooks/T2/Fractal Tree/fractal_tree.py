def background(couleur : str = 'black') :
    '''
    Rafraichit la scène avec un fond de la couleur
    'couleur' passée en paramètre et fixée sur `black` par défaut
    Préconditions :
    - couleur (str) : une chaine de caractères définissant une couleur HTML valide
    '''
    c.fill_style = couleur
    c.fill_rect(0, 0, 800, 600)
    display(c)