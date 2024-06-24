# Exercices

## Exercice 1

Trouver toutes les erreurs de syntaxe dans le fichier CSV ci-dessous :

```
Titre,Auteur,Extrait,Année
Air Vif,Éluard,J'ai regardé devant moi,1951
Je vis...,Labé,J'ai chaud extrême en endurant froidure
Heureux...,du Bellay,Heureux qui comme Ulysse, à fait...,1552
"La voix,Baudelaire,Mon berceau s'adossait...",1857
```

## Exercice 2

Nous souhaitons stocker dans une table l'inventaire d'un magasin. Ce dernier vend des biens dont il possède une certaine quantité en stock.

Les produits peuvent être indisponibles (épuisés chez le fournisseur) et être en vente libre ou non. 

a) Proposer des noms d'attribut et leur type Python pour une telle table d'inventaire.

b) Écrire dans un fichier CSV `stock_magasin.csv` quelques exemples d'enregistrement en respectant les attributs donnés à la question précédente.

c) Écrire le script Python permettant d'importer sous forme de liste de dictionnaire le stock du magasin.

d) Écrire une fonction `valide_stock(stock : list)->list` qui prend en paramètre une liste de dictionnaires et renvoie cette même liste en vérifiant et validant les types des valeurs.

________________

[Sommaire](./../../README.md)