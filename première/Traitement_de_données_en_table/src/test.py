import folium
import math
import random

def contenu_popup(dictionnaire : dict)->str:
    """
    :param (dict): dictionnaire
    :return: Etant donné un dictionnaire passé en argument retourne une chaîne de caractères 
    dont la spécification est l'objet d'une question de l'énoncé
    """
    code = "<p> <style> table, tr, td {border: 1px solid pink;} </style> <table>"
    for cle, valeur in dictionnaire.items():
        code = code + ("<tr><td>" + cle + "</td>" + "<td>" + valeur + "</td></tr>")
    code = code + "</table></p>"
    return code

def generer_popup(dictionnaire : dict):
    """
    :param (dict): dictionnaire
    :return: Un popup
    """
    contenu_de_la_popup = contenu_popup(dictionnaire)
    iframe = folium.IFrame(html = contenu_de_la_popup, width = 300, height = 200)
    popup = folium.Popup(iframe, max_width = 500)
    return popup

def ajouter_marqueur(carte, latitude : float, longitude : float, dictionnaire : dict, couleur : str)->None:
    """
    :param (object): carte de type folium.Map
    :param (float) :latitude
    :param (float): longitude
    :param (dict) :dictionnaire : de type dict avec clées et valeurs de type str
    :param (str) : couleur au format '#RRGGBB' où RR, GG, BB sont des entiers entre 0 et 255 en hexadécimal représentant les composant Rouge, Verte et Bleue de la couleur
    :return: None
    """
    radius = 4
    folium.CircleMarker(
        location = [latitude, longitude],
        radius = radius,
        popup = generer_popup(dictionnaire),
        color = couleur,
        fill = True
    ).add_to(carte)

#étape 1 : création de la carte  
ma_carte = folium.Map(location=(47.5, 1), zoom_start=7)

#étape 2 : ajout de quatre marqueurs
ajouter_marqueur(ma_carte, 47.90, 1.90, {'Ville' : 'ORLEANS',    'Pop.' : '114644'}, "#FF0000")
ajouter_marqueur(ma_carte, 47.39, 0.68, {'Ville' : 'TOURS',      'Pop.' : '136252'}, "#880000")
ajouter_marqueur(ma_carte, 48.73, 1.36, {'Ville' : 'DREUX',      'Pop.' : '30836'},  "#00FFFF")
ajouter_marqueur(ma_carte, 46.81, 1.69, {'Ville' : 'CHATEAUROUX','Pop.' : '43732'},  "#88BB88")

#étape 3 : affichage de la carte
ma_carte.save("airports_map.html")























# import csv
# 
# def enlever_doublons_liste(avec_doublons):
#     sans_doublons = []
#     for element in avec_doublons:
#         #à compléter pour répondre
#         if element not in sans_doublons : 
#             sans_doublons.append(element) 
#     return sans_doublons
# 
# airports = []
# with open('aéroports.csv', 'r', encoding='utf-8') as csvfile:
#     lecteur_dict = csv.DictReader(csvfile, delimiter=',')
#     for ligne in lecteur_dict :
#         airports.append(ligne)
#         
# airports2 = []
# cities = []
# for enregistrement in airports :
#     new_enregistrement = {}
#     new_enregistrement2 = {}
#     for cle, value in enregistrement.items():
#         
#         if cle == 'IATA' :
#             new_enregistrement[cle] = value
#             new_enregistrement2[cle] = value
#         if cle == 'Airport_ID':
#             new_enregistrement[cle] = value
#         if cle == 'Name' :
#             new_enregistrement[cle] = value
#         if cle == 'Type' :
#             new_enregistrement[cle] = value
#         if cle == 'Country_Code' :
#             new_enregistrement2[cle] = value
#         if cle == 'City' :
#             new_enregistrement2[cle] = value
#         if cle == 'Latitude' :
#             new_enregistrement2[cle] = value
#         if cle == 'Longitude' :
#             new_enregistrement2[cle] = value
#         if cle == 'Altitude' :
#             new_enregistrement2[cle] = value
#     cities.append(new_enregistrement2)
#     airports2.append(new_enregistrement)
#     
# airports2 = enlever_doublons_liste(airports2)
# cities = enlever_doublons_liste(cities)
# 
# sortie1 = open("airports.csv", "w")
# w = csv.DictWriter(sortie1, ["Airport_ID", "Name", "Type", "IATA"])
# w.writeheader()
# w.writerows(airports2)
# 
# sortie2 = open("cities.csv", "w")
# w = csv.DictWriter(sortie2, ["City", "Country_Code", "IATA", "Latitude", "Longitude", "Altitude"])
# w.writeheader()
# w.writerows(cities)
                   
    
