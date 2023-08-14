# IMPORTATIONS
from random import *

# UN EXEMPLE DE CLASSE
class Voiture :
    def __init__(self, marque : str, annee : int, carburant : str) :
        self.__vitesse = 0
        self.__marque = marque
        self.__annee = annee
        self.__carburant = carburant

    def get_vitesse(self) :
        return self.__vitesse
    
    def get_marque(self) :
        return self.__marque
    
    def get_annee(self) :
        return self.__annee
    
    def get_carburant(self) :
        return self.__carburant
    
    def accelere(self) :
        self.__vitesse += 20
    
# FEUILLE D'EXERCICES
# ...................
# EXERCICES 1 & 2
class Boite :
    def __init__(self, longueur : int, largeur : int, hauteur : int) :
        self.__longueur = longueur
        self.__largeur = largeur
        self.__hauteur = hauteur
    
    def get_longueur(self) : 
        return self.__longueur
    
    def get_largeur(self) :
        return self.__largeur
    
    def get_hauteur(self) :
        return self.__hauteur
    
    def volume(self) :
        return self.__longueur * self.__largeur * self.__hauteur
    
    def infos(self) :
        return str(self.__longueur) + 'x' + str(self.__largeur) + 'x' + str(self.__hauteur)
    
    def __str__(self):
        return str(self.__longueur) + 'x' + str(self.__largeur) + 'x' + str(self.__hauteur)
# ...................
# EXERCICE 2
def maxi(b1 : Boite, b2 : Boite) -> Boite :
    if b1.volume() > b2.volume() :
        return b1
    else :
        return b2
# ...................
# EXERCICE 3
def creer_liste_boites(n : int) -> list :
    liste = []
    for i in range(0, n) :
        longueur, largeur, hauteur = randint(1, 50), randint(1, 50), randint(1, 50)
        boite = Boite(longueur, largeur, hauteur)
        liste.append(boite)
    return liste

def maxi_liste_boites(liste_boites : list) -> Boite :
    res = Boite(0, 0, 0)
    for boite in liste_boites :
        res = maxi(res, boite)
    return res

## LECON
class Pokemon :
    def __init__(self, nom : str) :
        self.__nom = nom
        self.__points_de_vie = randint(800, 1000)
        self.__attaque = randint(100, 200)
        self.__defense = randint(100, 200)
        self.__vitesse = randint(100, 200)
        self.__ko = False

    def get_nom(self) :
        return self.__nom
    
    def get_points_de_vie(self) :
        return self.__points_de_vie
    
    def get_attaque(self) :
        return self.__attaque
    
    def get_defense(self) :
        return self.__defense
    
    def get_vitesse(self) :
        return self.__vitesse
    
    def get_ko(self) :
        return self.__ko
    
    def set_points_de_vie(self, new_points_de_vie : int) :
        self.__points_de_vie = new_points_de_vie
    
    def augmenter_attaque(self, bonus) :
        self.__attaque += bonus
    
    def augmenter_point_de_vie(self, bonus) :
        self.__points_de_vie += bonus
    
    def augmenter_vitesse(self, bonus) :
        self.__vitesse += bonus
    
    def attaque(self, pokemon_adverse) :
        difference = self.__attaque - pokemon_adverse.get_defense()
        if difference > 0:
            return difference
        else :
            return 0
    
    def set_ko(self) :
        if self.__points_de_vie <= 0 :
            self.__ko = True
    
    def afficher_statistiques(self) :
        print('Nom : ' + self.__nom)
        print('Points de vie : ' + str(self.__points_de_vie))
        print('Attaque : ' + str(self.__attaque))
        print('Défense : ' + str(self.__defense))
        print('Vitesse : ' + str(self.__vitesse))

# Fonctions supplémentaires
def joue_en_premier(pokemon_1 : Pokemon, pokemon_2 : Pokemon) :
    if pokemon_1.get_vitesse() > pokemon_2.get_vitesse() :
        return (pokemon_1, pokemon_2)
    else :
        return (pokemon_2, pokemon_1)

def choix_action(pokemon_1 : Pokemon, pokemon_2 : Pokemon) -> str:
    type_action = randint(1, 4)
    match type_action :
        case 1 :
            pokemon_1.augmenter_attaque(bonus)
            action = pokemon_1.get_nom() + ' augmente son attaque physique à ' + str(bonus) + '.'
        case 2 :
            pokemon_1.augmenter_point_de_vie(bonus)
            action = pokemon_1.get_nom() + ' augmente son attaque spéciale à ' + str(bonus) + '.'
        case 3 :
            pokemon_1.augmenter_vitesse(bonus)
            action = pokemon_1.get_nom() + ' augmente sa vitesse à ' + str(bonus) + '.'
        case 4 :
            degats = pokemon_1.attaque(pokemon_2)
            pokemon_2.set_points_de_vie(pokemon_2.get_points_de_vie() - degats)
            action = pokemon_1.get_nom() + ' attaque ' + pokemon_2.get_nom() + ' en faisant ' + str(degats) + " dégats."
    return action

def combat(pokemon_1 : Pokemon, pokemon_2 : Pokemon) :
    # Afficher les statistiques initiales de chaque Pokémon
    pokemon_1.afficher_statistiques()
    print('\n')
    pokemon_2.afficher_statistiques()
    print('\n')

    numero_tour = 0
    
    while not pokemon_1.get_ko() and not pokemon_2.get_ko() :
        
        numero_tour += 1
        print('Tour numéro n°' + str(numero_tour))
        
        premier, deuxieme = joue_en_premier(pokemon_1, pokemon_2)

        # Action du premier Pokémon
        print(premier.get_nom() + ' est plus rapide !')    
        action_premier = choix_action(premier, deuxieme)
        print(action_premier)

        # Action du deuxième Pokémon
        action_deuxieme = choix_action(deuxieme, premier)
        print(action_deuxieme)

        # Mise à jour du statut du Pokémon (KO ou non)
        premier.set_ko()
        deuxieme.set_ko()

        # Affichage des PV
        print('\n')
        print('PV de ' + premier.get_nom() + ' : ' + str(premier.get_points_de_vie()))
        print('PV de ' + deuxieme.get_nom() + ' : ' + str(deuxieme.get_points_de_vie()))
        print('\n')
    
    # Affichage des résultats
    if pokemon_1.get_ko():
        print(pokemon_1.get_nom()+ ' est KO !')
        print(pokemon_2.get_nom() + ' remporte le combat !')
    else :
        print(pokemon_2.get_nom()+ ' est KO !')
        print(pokemon_1.get_nom() + ' remporte le combat !')

# Test
bonus = 20
pokemon1 = Pokemon('Tiplouf')
pokemon2 = Pokemon('Canarticho')

combat(pokemon1, pokemon2)
