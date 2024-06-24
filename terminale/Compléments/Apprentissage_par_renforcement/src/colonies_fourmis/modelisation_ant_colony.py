# author : Boddaert Théo
# title: L'apprentissage par renforcement
# date: Année scolaire 22/23

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
        :param arete (list): une liste représentant une arete, elle comprend une source, une arrivée et un nombre de case
        :param pheromones (int): une phéromone initialisée à 1
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
        :param arrivee (str): le sommet d'arrivée
        :return int: l'indice du sommet d'arrivée dans la liste des voisins du sommet source
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
        Constructeur : Initialise une fourmi à partir d'un numéro de fourmi et d'un sommet de départ
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
        Avance d'une case la fourmi lorsqu'elle revient à la colonie
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
        :return booleen: Renvoie True si la fourmi est revenue à la colonie, False sinon
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
    Affiche ou enregistre une représentation du graphe
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
    :param model (dict): Graphe G représenté par une liste d'adjacence
    :param sommet_courant (str): Un sommet u de G
    :return str: un sommet aléatoire voisin de u
    """
    voisins = model.voisins(sommet_courant)
    voisins_nom = [v["arrivee"] for v in voisins]
    voisins_pheromones = [v["pheromones"] for v in voisins]
    return random.choices(voisins_nom, weights=voisins_pheromones, k=len(voisins_pheromones))[0]

def renforcer_chemin(model : dict,chemin : list):
    """
    :param model (dict): Graphe G représenté par une liste d'adjacence
    :param chemin (list): Liste contenant tous les sommets que la fourmi a traversé
    """
    for i in range(0,len(chemin)-1):
        iv = model.get_indice_voisin(chemin[i],chemin[i+1])
        model.adj[chemin[i]][iv]["pheromones"] += 1

def calcul_retour(model : dict,chemin : list)->int:
    """
    :param model (dict): Graphe G représenté par une liste d'adjacence
    :param chemin (list): Liste contenant tous les sommets que la fourmi a traversé
    :return int: La somme du nombre des cases du chemin
    """
    nb_cases_retour = 0
    for i in range(len(chemin)-1):
        nb_cases_retour += model.adj[chemin[i]][model.get_indice_voisin(chemin[i],chemin[i+1])]["nombre de case"]
    return nb_cases_retour

def evaporation(model : dict):
    """
    :param model (dict): Graphe G représenté par une liste d'adjacence
    Enlève une phéromone sur chaques sommets du graphe G
    """
    for k in model.adj :
        for i in range(len(model.adj[k])):
            if model.adj[k][i]["pheromones"] > 1:
                model.adj[k][i]["pheromones"] -= 1
                
def colonie_de_fourmis(model : dict, t_evaporation : int, nb_fourmis : int)->list:
    """
    :param model (dict): Graphe G représenté par une liste d'adjacence
    :param t_evaporation (int): Fréquence d'évaporation initialisé à 8
    :param nb_fourmis (int): Le nombre de fourmis déployées
    :return list: Effectue l'algorithme des colonies de fourmis et renvoie la liste des chemins empruntés par les fourmis
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
    
#------Optimisation des paramètres---------

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
    plt.title("Nombres de parties gagnées et échouées en fonction du nombre de fourmis")
    plt.ylabel("Nombre de parties")
    plt.xlabel("Nombre de fourmis utilisées")
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
    plt.title("Nombres de parties gagnées et échouées en fonction de l'évaporation")
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
    plt.title("Pourcentage de parties gagnées sur 10 expériences")
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
    plt.title("Répartition des fourmis en pourcentage sur 1000 parties")
    plt.pie([nb_f_mc , nb_f_n_mc , nb_f_ni],
            normalize = True,
            autopct = lambda x: str(round(x, 2)) + '%')
    plt.legend(["Fourmis ayant trouvé le meilleur chemin", "Fourmis ayant trouvé la nourriture mais pas le meilleur chemin" , "Fourmis n'ayant pas trouvé la nourriture"])
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
    plt.ylabel("Moyenne des pourcentages de réussite sur 10 parties")
    plt.xlabel("Nombre d'expérience")
    plt.title('Moyenne cumulée sur 100 expériences')
    #plt.savefig("../img/statistiques/moy_cumul.png")
    plt.show()
    
if __name__ == '__main__' :
    #affiche_model(l_aretes)
    model = initialise_model(l_aretes)
    colonie_de_fourmis(model, t_evaporation, nb_fourmis_demo)
    print(model)