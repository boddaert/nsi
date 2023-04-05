# author : Boddaert Théo


def verif_decoupe(l : list, l1 : list, l2 : list) -> bool:
    """
    :param l: une liste l initiale
    :param l1: une liste représentant une moitié de la liste l
    :param l2: une liste représentant une moitié de la liste l
    :return: Vrai si l1 et l2 sont deux listes découpés à partir de l, faux sinon
    Vérifie si, tous les éléments de l1 et l2 sont présents dans l uniquement
    """
    res = True
    if not len(l) == len(l1) + len(l2):
        print("La taille de "+ str(l1) +" + la taille de "+ str(l2) +" n'est pas égale à la taille de "+str(l))
        res = False
    if not all(e in l for e in l1) and not all(e in l for e in l2):
        print("Un élément de " +str(l1)+ " ou un élément de "+ str(l2)+" n'est pas présent dans "+str(l))
        res = False
    return res

def est_triee(l : list) -> bool :
    """
    :param l: une liste
    :return: Vrai si l est triée, faux sinon
    """
    return l == sorted(l)

def verif_fusion(l : list, l1 : list, l2 : list) -> bool :
    """
    :param l: une liste fusionnée à partir des listes l1 et l2
    :param l1: une liste
    :param l2: une liste
    :return: vrai si l est une fusion de l1 et l2, faux sinon
    Vérifie si, tous les éléments de l sont présents dans l1 et l2 uniquement et si l est triée
    """
    return verif_decoupe(l,l1,l2) and est_triee(l)
