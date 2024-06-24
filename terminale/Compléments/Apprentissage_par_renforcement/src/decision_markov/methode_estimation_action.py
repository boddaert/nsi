import random
import matplotlib.pyplot as plt

def initialise_filons(n : int)->list:
    """
    :param n (int): Nombre d'éléments
    :return list: Renvoie une liste de nombres aléatoires de taille n
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
    
    plt.title("Moyenne des récompenses en fonction d'epsilon")
    plt.legend()
    plt.ylabel("Moyenne de la récompense")
    plt.xlabel("Nombres d'itérations")
    #plt.savefig("../img/moy_methode_estimation_action.png")
    plt.show()