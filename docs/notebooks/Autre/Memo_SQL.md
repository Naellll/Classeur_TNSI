# Mémo pour le SQL :

### Liens utiles :
- [Tutoriel](https://fr.khanacademy.org/computing/computer-programming/sql?ref=resume_learning#sql-basics) pour les bases du SQL
-


## 1- Bases :

- Mettre des ";" à chaque fin d'instruction
- Écrire en majuscules les commandes SQL comme "CREATE" ou "INSERT"
- Comme pour Python écrire le texte entre "**guillemets**"


## 2- **Créer** une table :

### • Fonctionnement :

- CREATE TABLE *ma_table* (

    x **INTEGER** PRIMARY KEY (utile pour les ID),

    y **TEXT** (texte divers, STR), 

    z **INTEGER** (nombres, INT et FLOAT), 
    
    ...)**;**

##### Ainsi une table nommée *ma_table* est crée prenant pour paramètres **x**, **y**, **z**, ...

### • Exemple de rendu :

|*ma_table*|*0 rows*|
|----------|--------|
|  x (PK)  |  INTEGER  |
|  y  |  TEXT  |
|  z  |  INTEGER  |

### • Commande :

- "CREATE TABLE table(...);"


## 3- **Insérer** des données dans ma table :

### • Fonctionnement :

- INSERT INTO customers VALUES (

    **1** (valeur attribuée à x), 

    **"*test*"** (valeur attribuée à y),

    **18** (valeur attribuée à z),
    
    ...)**;**

##### Les valeurs 1, test, 18, ... sont ajoutées à la table *ma_table*, chaque valeur est liée à un paramètre : 1 avec x, test avec y etc.

### • Exemple de rendu (*si SELECT utilisé*) :

|*X*|*Y*|*Z*|
|---|---|---|
| 1 | test | 18 |
| 2 | toto | 22 |
| 3 | titi | 12 |
| 4 | tutu | 18 |
| 5 | ... | ... |

### • Commande :

- "INSERT INTO table(...);"

## 4 - **Interroger** les données de ma table :

### • Fonctionnement :

- SELECT **x** FROM *ma_table*;

##### Les valeurs correspondants à **x** de *ma_table* seront affichées, x peut être remplacé par :
- "*" : affiche tout les éléments de *ma_table*
- "Y" : affiche une colonne en particulier (ou plusieurs avec ",")

##### Il existe également la commande "**WHERE**" qui permet d'ajouter une condition à ce qui est affiché :
- SELECT **x** FROM *ma_table* WHERE **y**

##### **y** peut être remplacé par diverses conditions qui peuvent être acumulées avec **AND** :
- "z **>=**/**<=**/**=** *10*" : affiche tout les éléments dont le z est supérieur/inférieur/égal à *10* ("**=**" fonctionne également avec le texte)
- "y **IN** ("test", "testt", ...) : affiche tout les éléments dont y contient "test" ou "testt"

#### Enfin on peut ajouter une dernière commande à SELECT, "**ORDER BY** *z*" ou z peut être remplacer par la façon dont la liste sera rangée :
- "x" : la liste sera rangée par ordre croissant de la colonne x (on peut également ajouter **ASC** \ DESC)
- "x" **DESC** : la liste sera rangée par ordre décroissant de la colonne x

### • Exemples d'utilisations des ces commandes :

SELECT *Y*, *Z* FROM *ma_table*;
|*Y*|*Z*|
|---|---|
| test | 18 |
| toto | 22 |
| titi | 12 |
| tutu | 18 |
| ... | ... |

SELECT * FROM *ma_table* ORDER BY Z DESC;
|*X*|*Y*|*Z*|
|---|---|---|
| 2 | toto | 22 |
| 4 | tutu | 18 |
| 1 | test | 18 |
| 3 | titi | 12 |
| 5 | ... | ... |

SELECT * FROM *ma_table* WHERE Z < 20 AND Z > 15 ORDER BY Z;
|*X*|*Y*|*Z*|
|---|---|---|
| 1 | test | 18 |
| 4 | tutu | 18 |
| 5 | ... | ... |

### • Commande :

- SELECT *élément(s)* WHERE *condition* ORDER BY *ordre*

## 5 - **Agréger** les données d'une table :

### • Fonctionnement :

- SELECT **x** FROM *ma_table*

##### Les valeurs **x** de *ma_table* seront affichées, x peut être remplacé par :
- MAX(*colonne*) : affiche le maximum d'une colonne
- AVG(*colonne*) : affiche la moyenne d'une colonne
- SUM(*colonne*) : affiche le total d'une colonne

##### On peut également ajouter la commande **AS** pour identifier ce nouvel élément dans une nouvelle table :
- SELECT **x** AS **test** FROM *ma_table*

##### Il est également possible de coupler cette fonction à la commande **WHERE** avec **COUNT** :
- SELECT COUNT(*colonne*) FROM *ma_table* WHERE *condition* : compte le nombre d'élément présent dans une colonne respectant la condition
- SELECT COUNT(**DISTINCT** *colonne*) FROM *ma_table* WHERE *condition* : compte le nombre d'élément différent dans une colonne respectant la condition

##### Enfin, la commande **GROUP BY** permet de regrouper les valeurs :
SELECT **x**, **COUNT(*)** FROM *ma_table* GROUP BY **z**

### • Exemples d'utilisations des ces commandes :

SELECT Y, MAX(Z) AS maximum_z FROM *ma_table*;
| *Y*  |*maximum_z*|
|------|-----------|
| toto |    22     |

SELECT COUNT(*) FROM *ma_table* GROUP BY Z;
| *Z* | COUNT(*) |
|-----|----------|
| 22  |    1     |
| 18  |    2     |
| 12  |    1     |