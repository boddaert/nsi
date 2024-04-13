# Annexes

## Annexe 1

Programme python, dilemme de l'exploration - exploitation selon une probabilité epsilon

```{#dilemme_exploration_exploitation  .python .numberLines}
import random
import matplotlib.pyplot as plt

def initialise_filons(n : int)->list:
    """
    :param n (int): Nombre d elements
    :return list: Renvoie une liste de nombres aleatoires de taille n
    """
    return [random.randint(1,20) for _ in range(n)]

def explore(filons_reels : list)->int:
    """
    :param filons_reels (list): Liste des filons existant
    :return int: Renvoie un indice aleatoire de la liste filons_reels
    """
    return random.randint(0, len(filons_reels)-1)

def exploite(filons_connus : list)->int:
    """
    :param filons_connus (list): Liste des filons que l'on connait
    :return int: Renvoie l'indice du maximum de la liste filons_connus
    """
    ind_max = 0
    for i in range(len(filons_connus)):
        if filons_connus[i] > filons_connus[ind_max] :
            ind_max = i
    return ind_max

def dilemme_exploration_exploitation(n : int,epsilon : float)->float:
    """
    :param n (int): Nombre de filons
    :param epsilon (float): probabilite epsilon
    :return float: Renvoie la moyenne des recompenses selon une probabilite epsilon d'explorer ou d'exploiter
    """
    filons_reels = initialise_filons(n)
    filons_connus = [0 for _ in range(n)]
    recompense_ieme = 0
    list_recompenses = []
    moyenne = []
    for _ in range(500):
        if random.uniform(0,1) <= epsilon :
            ind = explore(filons_reels)
            filons_connus[ind] = filons_reels[ind]
        else :
            ind = exploite(filons_connus)
        recompense_ieme = filons_connus[ind]
        list_recompenses.append(recompense_ieme)
        moyenne.append(sum(list_recompenses)/len(list_recompenses))
    return moyenne

def stats():
    """
    Creation d'un graphique representant la moyenne des recompenses pour 3 probabilites epsilon
    """
    n = 20
    eps_001 = dilemme_exploration_exploitation(n, 0.01)
    eps_01 = dilemme_exploration_exploitation(n, 0.1)
    eps_03 = dilemme_exploration_exploitation(n, 0.3)

    plt.plot(eps_001, label="0.01")
    plt.plot(eps_01 , label="0.1")
    plt.plot(eps_03 , label="0.3")

    plt.title("Moyenne des recompenses en fonction d'epsilon")
    plt.legend()
    plt.ylabel("Moyenne des recompenses")
    plt.xlabel("Nombres d'iterations")
    #plt.savefig("../img/moy_exploration_exploitation.png")
    plt.show()
```

## Annexe 2

Programme Python, dilemme de l'exploration - exploitation, selon une probabilité epsilon et utilisant la méthode d'estimation d'actions

```{#exploration_exploitation_estimations  .python .numberLines}
import random
import matplotlib.pyplot as plt

def initialise_filons(n : int)->list:
    """
    :param n (int): Nombre d'elements
    :return list: Renvoie une liste de nombres aleatoires de taille n
    """
    return [random.randint(1,100) for _ in range(n)]

def initialise_estimations(filons : list)->list:
    """
    :param filons (list): Une liste representant les filons reels
    :return list: Renvoie une liste d'estimations aleatoires des filons reels
    """
    return [random.randint(1,100) for i in range(len(filons))]

def converge(estimations : list, filons : list, i : int)->float:
    """
    :param estimations (list): Liste representant les estimations des filons
    :param filons (list): Liste representant les filons reels
    :param i (int): Un indice i
    :return float: Renvoie une nouvelle valeur d'estimations a l'indice i qui converge vers la valeur reelle du filon 
    """
    v = filons[i] - estimations[i]
    return estimations[i] + (v/2)

def explore(filons : list)->int:
    """
    :param filons (list): Liste representant les filons reels
    :return int: Renvoie un indice aleatoire
    """
    return random.randint(0, len(filons)-1)

def exploite(estimations : list)->int:
    """
    :param estimations (list): Liste representant les estimations
    :return int: Renvoie l'indice de la plus haute estimation
    """
    ind_max = 0
    for i in range(len(estimations)):
        if estimations[i] > estimations[ind_max] :
            ind_max = i
    return ind_max

def exploration_exploitation_estimations(filons : list, estimations : list, epsilon : float)->float:
    """
    :param filons (list): Liste representant les filons reels
    :param estimations (list): Liste representant les estimations
    :param epsilon (float): Probabilite espilon
    :return float: Renvoie une moyenne des recompenses selon la methode d'estimation d'actions
    """
    recompense_ieme = 0
    list_recompenses = []
    moyenne = []
    for _ in range(1000):
        if random.uniform(0,1) <= epsilon :
            ind = explore(filons)
            estimations[ind] = converge(estimations, filons, ind)
        else :
            ind = exploite(estimations)
        recompense_ieme = filons[ind]
        list_recompenses.append(recompense_ieme)
        moyenne.append(sum(list_recompenses)/len(list_recompenses))
    return moyenne

def stats():
    """
    Creation d'un graphique representant les courbes des moyennes des recompenses
    """
    n = 10
    filons = initialise_filons(n)
    estimations = initialise_estimations(filons)
    eps_0 = exploration_exploitation_estimations(filons, estimations, 0)
    eps_01 = exploration_exploitation_estimations(filons, estimations, 0.1)

    plt.plot(eps_0, label="0")
    plt.plot(eps_01 , label="0.1")

    plt.title("Moyenne des recompenses en fonction d'epsilon")
    plt.legend()
    plt.ylabel("Moyenne de la recompense")
    plt.xlabel("Nombres d'iterations")
    #plt.savefig("../img/moy_methode_estimation_action.png")
    plt.show()
```

## Annexe 3

Programme Python modelisant l'algorithme des Colonies de fourmis

```{#colonies_fourmis .python .numberLines}
# author : Boddaert Theo
# title: L'apprentissage par renforcement
# date: Annee scolaire 22/23

import random
import matplotlib.pyplot as plt

l_aretes = [('Colonie','B',2),('Colonie','C',3),('Colonie','D',4),
            ('B','E',3),('B','F',3),
            ('C','A',4),('D','A',5),
            ('A','Nourriture',5),('E','Nourriture',2),('F','Nourriture',8)]
nb_fourmis_activite = 50
nb_fourmis_demo = 500
t_evaporation = 8
chemin_gagnant = ['Colonie','B','E','Nourriture']


#------Classe Graphe---------

class Graph:
    def __init__(self):
        """
        Constructeur : Initialise un graphe vide sous forme de liste d'adjacence
        """
        self.adj = {}

    def ajoute_sommet(self,s : str):
        """
        :param s (str): un sommet
        Ajoute au graphe le sommet s
        """
        self.adj[s] = []

    def ajoute_arete(self,arete : list,pheromones=1):
        """
        :param arete (list): une liste representant une arete, elle comprend une source, une arrivee et un nombre de case
        :param pheromones (int): une pheromone initialisee a 1
        Ajoute au graphe une arete
        """
        source = arete[0]
        arrivee = arete[1]
        nb_cases = arete[2]
        if source not in self.adj :
            self.ajoute_sommet(source)
        if arrivee not in self.adj :
            self.ajoute_sommet(arrivee)
        self.adj[source].append({"arrivee" : arrivee, "nombre de case" : nb_cases, "pheromones" : pheromones})
        self.adj[arrivee].append({"arrivee" : source, "nombre de case" : nb_cases, "pheromones" : pheromones})

    def voisins(self,s : str)->list:
        """
        :param s (str): un sommet
        :return list: la liste des voisins de s
        """
        return self.adj[s]

    def get_indice_voisin(self,source : str, arrivee : str)->int:
        """
        :param source (str): le sommet source
        :param arrivee (str): le sommet d'arrivee
        :return int: l'indice du sommet d'arrivee dans la liste des voisins du sommet source
        """
        for i in range (len(self.voisins(source))):
            if self.adj[source][i]["arrivee"] == arrivee :
                return i

    def __str__(self):
        """
        :return str: Affiche le graphe
        """
        res = ""
        for k,val in self.adj.items():
            res = res + str(k) +" : \n"
            for a in val:
                res = res + "   " + str(a)+"\n"
        return res

#------Classe Fourmi----------

class Fourmi:
    def __init__(self,numero : int,s_de_depart : str):
        """
        Constructeur : Initialise une fourmi a partir d'un numero de fourmi et d'un sommet de depart
        """
        self.numero = numero
        self.chemin = [s_de_depart]
        self.nb_cases = 0
        self.nb_cases_retour = 0
        self.retour = False

    def avancer(self):
        """
        Avance d'une case la fourmi
        """
        self.nb_cases -= 1

    def revenir(self):
        """
        Avance d'une case la fourmi lorsqu'elle revient a la colonie
        """
        self.nb_cases_retour -= 1

    def est_sur_sommet(self)->bool:
        """
        :return booleen: Renvoie True si la fourmi est sur un sommet, False sinon
        """
        return self.nb_cases == 0

    def est_sur_nourriture(self)->bool:
        """
        :return booleen: Renvoie True si la fourmi est sur le sommet de nourriture, False sinon
        """
        return self.chemin[-1] == 'Nourriture'

    def est_revenue(self):
        """
        :return booleen: Renvoie True si la fourmi est revenue a la colonie, False sinon
        """
        return self.nb_cases_retour == 0

    def __str__(self):
        """
        :return str: Affiche la fourmi
        """
        return str(self.numero) + " : "+ str(self.chemin)+ str(self.nb_cases)

#-------Initialisation du model ----------

def initialise_model(l_aretes : list)->dict:
    """
    :param l_aretes (list): Liste d'aretes
    :return dict: Construit un graphe selon l_aretes
    """
    model = Graph()
    for a in l_aretes :
        model.ajoute_arete(a)
    return model

def affiche_model(l_aretes : list):
    """
    :param l_aretes (list): Liste d'aretes
    Affiche ou enregistre une representation du graphe
    """
    g = nx.Graph()
    g.add_weighted_edges_from(l_aretes)
    pos = nx.planar_layout(g)
    nx.draw(g, with_labels=True, node_color='skyblue', edge_cmap=plt.cm.Blues, pos = pos)
    edge_labels = dict([((u,v,),d['weight'])
        for u,v,d in g.edges(data=True)])
    nx.draw_networkx_edge_labels(g,pos,edge_labels=edge_labels,label_pos = 0.5, font_color='red', rotate = True)
    #plt.savefig("../img/visualisation_graph.png")
    plt.show()

#-----Colonies de fourmis---------

def choix_voisin(model : dict,sommet_courant : str)->str:
    """
    :param model (dict): Graphe G represente par une liste d'adjacence
    :param sommet_courant (str): Un sommet u de G
    :return str: un sommet aleatoire voisin de u
    """
    voisins = model.voisins(sommet_courant)
    voisins_nom = [v["arrivee"] for v in voisins]
    voisins_pheromones = [v["pheromones"] for v in voisins]
    return random.choices(voisins_nom, weights=voisins_pheromones, k=len(voisins_pheromones))[0]

def renforcer_chemin(model : dict,chemin : list):
    """
    :param model (dict): Graphe G represente par une liste d'adjacence
    :param chemin (list): Liste contenant tous les sommets que la fourmi a traverse
    """
    for i in range(0,len(chemin)-1):
        iv = model.get_indice_voisin(chemin[i],chemin[i+1])
        model.adj[chemin[i]][iv]["pheromones"] += 1

def calcul_retour(model : dict,chemin : list)->int:
    """
    :param model (dict): Graphe G represente par une liste d'adjacence
    :param chemin (list): Liste contenant tous les sommets que la fourmi a traverse
    :return int: La somme du nombre des cases du chemin
    """
    nb_cases_retour = 0
    for i in range(len(chemin)-1):
        nb_cases_retour += model.adj[chemin[i]][model.get_indice_voisin(chemin[i],chemin[i+1])]["nombre de case"]
    return nb_cases_retour

def evaporation(model : dict):
    """
    :param model (dict): Graphe G represente par une liste d'adjacence
    Enleve une pheromone sur chaques sommets du graphe G
    """
    for k in model.adj :
        for i in range(len(model.adj[k])):
            if model.adj[k][i]["pheromones"] > 1:
                model.adj[k][i]["pheromones"] -= 1

def colonie_de_fourmis(model : dict, t_evaporation : int, nb_fourmis : int)->list:
    """
    :param model (dict): Graphe G represente par une liste d'adjacence
    :param t_evaporation (int): Frequence d'evaporation initialise a 8
    :param nb_fourmis (int): Le nombre de fourmis deployees
    :return list: Effectue l'algorithme des colonies de fourmis et renvoie la liste des chemins empruntes par les fourmis
    """
    chemins_pour_chaques_fourmis = []
    fourmilliere = 'Colonie'
    nourriture = 'Nourriture'
    liste_fourmis = []
    for i in range(nb_fourmis):
        liste_fourmis.append(Fourmi(i,fourmilliere))
        for f in liste_fourmis :
            if f.retour :
                f.revenir()
                if f.est_revenue():
                    renforcer_chemin(model,f.chemin)
                    chemins_pour_chaques_fourmis.append(f.chemin)
                    liste_fourmis.remove(f)
            if f.est_sur_sommet():
                if f.est_sur_nourriture() and not f.retour :
                    f.retour = True
                    f.nb_cases_retour = calcul_retour(model,f.chemin)
                else :
                    sommet_suivant = choix_voisin(model,f.chemin[-1])
                    ind_sommet_suivant = model.get_indice_voisin(f.chemin[-1],sommet_suivant)
                    f.nb_cases = model.adj[f.chemin[-1]][ind_sommet_suivant]["nombre de case"]
                    if sommet_suivant in f.chemin :
                        ind = f.chemin.index(sommet_suivant)
                        f.chemin = f.chemin[:ind]
                    f.chemin.append(sommet_suivant)  
            f.avancer()          
        if i%t_evaporation == 0:
            evaporation(model)
    return chemins_pour_chaques_fourmis

#------Optimisation des parametres---------

def reussite_par_parties_fourmis():
    """
    Creation d'un graphique representant le nombre de parties gagnees en fonction du nombre de fourmis
    """
    tab_reussite, tab_echec = [], []
    for test_fourmis in range(50,650,50):
        reussite, echec = 0, 0
        for _ in range(1000):
            chemins_pour_chaques_fourmis = colonie_de_fourmis(initialise_model(l_aretes),t_evaporation, test_fourmis)
            nb_f_md = chemins_pour_chaques_fourmis.count(chemin_gagnant)
            if nb_f_md > len(chemins_pour_chaques_fourmis) - nb_f_md :
                reussite += 1
            else :
                echec += 1
        tab_reussite.append(reussite)
        tab_echec.append(echec)
    barWidth = 0.4
    r1 = range(len(tab_reussite))
    r2 = [x + barWidth for x in r1]
    plt.title("Nombres de parties gagnees et echouees en fonction du nombre de fourmis")
    plt.ylabel("Nombre de parties")
    plt.xlabel("Nombre de fourmis utilisees")
    plt.bar(r1, tab_reussite, width = barWidth, label = "Reussite")
    plt.bar(r2, tab_echec, width = barWidth, label = "Echec")
    plt.xticks([r + barWidth / 2 for r in range(len(tab_reussite))], [nb for nb in range(50,650,50)])
    plt.legend()
    #plt.savefig("../img/optimisation_parametres/nb_parties_fourmis.png")
    plt.show()

def reussite_par_parties_evaporation():
    """
    Graphique representant le nombre de parties gagnees en fonction de la frequence d'evaporation
    """
    tab_reussite, tab_echec = [], []
    for test_evaporation in range(2,15,2):
        reussite, echec = 0, 0
        for _ in range(1000):
            chemins_pour_chaques_fourmis = colonie_de_fourmis(initialise_model(l_aretes),test_evaporation,nb_fourmis_demo)
            nb_f_md = chemins_pour_chaques_fourmis.count(chemin_gagnant)
            if nb_f_md > len(chemins_pour_chaques_fourmis) - nb_f_md :
                reussite += 1
            else :
                echec += 1
        tab_reussite.append(reussite)
        tab_echec.append(echec)
    barWidth = 0.4
    r1 = range(len(tab_reussite))
    r2 = [x + barWidth for x in r1]
    plt.title("Nombres de parties gagnees et echouees en fonction de l'evaporation")
    plt.ylabel("Nombre de parties")
    plt.xlabel("Evaporation tous les x tours")
    plt.bar(r1, tab_reussite, width = barWidth, label = "Reussite")
    plt.bar(r2, tab_echec, width = barWidth, label = "Echec")
    plt.xticks([r + barWidth / 2 for r in range(len(tab_reussite))], [eva for eva in range(2,15,2)])
    plt.legend()
    #plt.savefig("../img/optimisation_parametres/nb_parties_evaporation.png")
    plt.show()

#-------Statistiques--------

def pour_reussite():
    """
    Graphique representant le pourcentage de parties gagnees pour 10 experiences
    """
    tab_pour = []
    for _ in range(10):
        reussite, total = 0, 0
        for _ in range(500):
            chemins_pour_chaques_fourmis = colonie_de_fourmis(initialise_model(l_aretes),t_evaporation,nb_fourmis_demo)
            nb_f_md = chemins_pour_chaques_fourmis.count(chemin_gagnant)
            if nb_f_md > len(chemins_pour_chaques_fourmis) - nb_f_md :
                reussite += 1
            total += 1
        tab_pour.append(int((reussite * 100) / total))
    plt.title("Pourcentage de parties gagnees sur 10 experiences")
    plt.bar(range(len(tab_pour)), tab_pour)
    plt.ylim(top = 100)
    for index,data in enumerate(tab_pour):
        plt.text(x=index , y =data+1 , s=f"{data}% " , fontdict=dict(fontsize=10))
    plt.tight_layout()
    plt.xticks([r for r in range(len(tab_pour))], ["Exp " + str(par) for par in range(0,10)])
    #plt.savefig("../img/statistiques/pourcentage_reussite.png")
    plt.show()

def repartition_fourmis():
    """
    Graphique representant la repartition des fourmis
    """
    nb_f_mc , nb_f_n_mc , nb_f_ni = 0,0,0
    for _ in range(1000) :
        chemins_pour_chaques_fourmis = colonie_de_fourmis(initialise_model(l_aretes),t_evaporation, nb_fourmis_demo)
        nb_f_mc += chemins_pour_chaques_fourmis.count(chemin_gagnant)
        nb_f_n_mc += len(chemins_pour_chaques_fourmis) - chemins_pour_chaques_fourmis.count(chemin_gagnant)
        nb_f_ni += nb_fourmis_demo - len(chemins_pour_chaques_fourmis)
    plt.title("Repartition des fourmis en pourcentage sur 1000 parties")
    plt.pie([nb_f_mc , nb_f_n_mc , nb_f_ni],
            normalize = True,
            autopct = lambda x: str(round(x, 2)) + '%')
    plt.legend(["Fourmis ayant trouve le meilleur chemin", "Fourmis ayant trouve la nourriture mais pas le meilleur chemin" , "Fourmis n'ayant pas trouve la nourriture"])
    #plt.savefig("../img/statistiques/repartition_fourmis.png")
    plt.show()

def moyenne_cumulee():
    """
    Graphique representant la moyenne cumulee du pourcentage de parties gagnee
    """
    pourcentages_reussite = []
    moyennes_reussite = []
    moyenne_cumulee = []
    for _ in range(100):
        for _ in range(100) :
            chemins_pour_chaques_fourmis = colonie_de_fourmis(initialise_model(l_aretes),t_evaporation, nb_fourmis_demo)
            nb_f_md = chemins_pour_chaques_fourmis.count(chemin_gagnant)
            pourcentages_reussite.append(nb_f_md * 100 / len(chemins_pour_chaques_fourmis))

        moyennes_reussite.append(sum(pourcentages_reussite) / len(pourcentages_reussite))
        moyenne_cumulee.append(sum(moyennes_reussite)/len(moyennes_reussite))
        pourcentages_reussite = []
    plt.plot(moyenne_cumulee)
    plt.ylabel("Moyenne des pourcentages de reussite sur 10 parties")
    plt.xlabel("Nombre d'experience")
    plt.title('Moyenne cumulee sur 100 experiences')
    #plt.savefig("../img/statistiques/moy_cumul.png")
    plt.show()

if __name__ == '__main__' :
    #affiche_model(l_aretes)
    model = initialise_model(l_aretes)
    colonie_de_fourmis(model, t_evaporation, nb_fourmis_demo)
    print(model)
```

## Annexe 4

\label{sec:annexe4}Scénario pédagogique :

\includepdf[pages=-]{./img/strategie/cours_magistral/scenario_pedagogique.pdf}

## Annexe 5
\label{sec:annexe5}Diaporama de présentation sur l'intelligence artificielle :

\includepdf[pages=-]{./img/strategie/cours_magistral/presentation_ia.pdf}

## Annexe 6
\label{sec:annexe6}Notice de jeu Colonie de Fourmis :

\includepdf[pages=1]{./img/strategie/activite/Notice_Jeu_des_Colonies_de_fourmis.pdf}
\includepdf[pages=2]{./img/strategie/activite/Notice_Jeu_des_Colonies_de_fourmis.pdf}\includepdf[pages=3]{./img/strategie/activite/Notice_Jeu_des_Colonies_de_fourmis.pdf}
\includepdf[pages=4]{./img/strategie/activite/Notice_Jeu_des_Colonies_de_fourmis.pdf}

## Annexe 7

\label{sec:annexe7}Questionnaire soumis aux élèves :

\includepdf[page=1]{./img/strategie/activite/Questionnaire_Intelligence_Artificielle.pdf}
\includepdf[page=2]{./img/strategie/activite/Questionnaire_Intelligence_Artificielle.pdf}

## Annexe 8

\label{sec:annexe8}Corrigé du questionnaire :

\includepdf[page=1]{./img/strategie/activite/Corrige_Questionnaire_Intelligence_Artificielle.pdf}
\includepdf[page=2]{./img/strategie/activite/Corrige_Questionnaire_Intelligence_Artificielle.pdf}