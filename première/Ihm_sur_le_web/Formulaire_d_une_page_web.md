# Formulaire d'une page web

## I. HTML

Le langage HTML (*HyperText Markup Language*) que nous pouvons traduire en Français par "langage de balisage hypertexte" est le langage utilisé pour structurer une page web et son contenu.

Nous pouvons par exemple organiser le contenu en un ensemble de paragraphes, une liste d'éléments, utiliser des images ou des tableaux.

### a) Syntaxe de balise

Les contenus sont encadrés de *balises* indiquant de quel type de contenu il s'agit et cela constitue un *élément HTML*.

Par exemple, l'élément suivant représente un paragraphe :

```html
<p>Ceci est un paragraphe</p>
```

Nous distingons les balises ouvrantes et fermantes.

### b) Imbrication de balise

Nous pouvons imbriquer les balises pour ajouter un type à un contenu.

Par exemple, l'élément suivant présente du contenu de type paragraphe et gras :

```html
<p>Ceci est un <b>paragraphe gras</b></p>
```

Il faut cependant faire attention à imbriquer correctement les balises.

### c) Structure d'un document HTML

Un document HTML est organisé d'une façon précise. 

Tous les éléments du document sont contenus dans une balise `html`.

Le document est divisé en deux parties :

- Il y a la tête, contenue dans une balise `head` comprenant les *métadonnées*, c'est-à-dire les données qui ne sont pas affichées à l'écran. Il y a par exemple, l'encodage des caractères utilisé et le titre de la page.

- Et le corps, contenu dans une balise `body` comprenant les éléments qui sont affichés sur la page web.

Voici ci-dessous, un exemple de squelette d'un document HTML :

```html
<!doctype html>
<html lang="fr">
  <head>
    <meta charset="utf-8" />
    <title>Ma page de test</title>
  </head>
  <body>
    ...
  </body>
</html>
```

### d) Mémo des balises HTML

| Nom de la balise | Syntaxe HTML | Aperçu |
| --- | --- | --- |
| Titre de taille cinq | `<h5>Titre</h5>` | <h5>Titre</h5> |
| Titre de taille quatre | `<h4>Titre</h4>` | <h4>Titre</h4> |
| Titre de taille trois| `<h3>Titre</h3>` | <h3>Titre</h3> |
| Titre de taille deux | `<h2>Titre</h2>` | <h2>Titre</h2> |
| Titre de taille un | `<h1>Titre</h1>` | <h1>Titre</h1> |
| Paragraphe | `<p>paragraphe</p>` | <p>paragraphe</p> |
| Lien hypertexte | `<a href="https://github.com/boddaert/snt">lien</a>` | <a href="https://github.com/boddaert/snt">lien</a> |
| Image | `<img src="https://urlr.me/3jLD4">` | <img src="https://urlr.me/3jLD4"> |
| Texte gras | `<b>Texte gras</b>` | <b>Texte gras</b> |
| Texte italique | `<i>Texte italique</i>` | <i>Texte italique</i> |
| Liste à puces numérotée | `<ol> <li>Premier</li> <li>Deuxième</li> </ol>` | <ol> <li>Premier</li> <li>Deuxième</li> </ol> |
| Liste à puces non numérotée | `<ul> <li>Premier</li> <li>Deuxième</li> </ul>` | <ul> <li>Premier</li> <li>Deuxième</li> </ul> |
| Tableau | `<table><tr><th>Première colonne</th><th>Deuxième colonne</th></tr><tr><td>Première ligne</td><td>Première ligne</td></tr><tr><td>Deuxième ligne</td><td>Deuxième ligne</td></tr></table>` | <table><tr><th>Première colonne</th><th>Deuxième colonne</th></tr><tr><td>Première ligne</td><td>Première ligne</td></tr><tr><td>Deuxième ligne</td><td>Deuxième ligne</td></tr></table> |

## II. CSS

Le langage CSS (*Cascading Style Sheets*) que nous pouvons traduire en Français par "feuille de style en cascade" est le langage utilisé pour mettre en forme du contenu HTML.

Il permet d'appliquer des styles sur différents éléments sélectionnés dans un document HTML.

### a) Syntaxe d'une règle CSS

Une règle CSS est une règle de style appliqué à un sélecteur encadré par des accolades.

Le *sélecteur* correspond à un élément HTML présent dans le document.

Par exemple, voici ci-dessous une règle CSS appliquant la couleur rouge à tous les éléments `p` dans le document :

```css
p {
    color : red;
}
```

`p` est alors le sélecteur et `color : red;` est la règle.

### b) Intégration d'une feuille CSS à un document HTML

Pour faire le lien entre le document HTML et la feuille de style CSS qui sont deux fichiers différents, il faut ajouter dans la balise `head` du document HTML le lien vers le fichier CSS.

Par exemple, si ma feuille de style se nomme `style.css` :

```html
<link href="style.css" rel="stylesheet" type="text/css" />
```

### c) Sélecteurs de classes et d'ID

Il est possible d'appliquer un style uniquement à certains éléments HTML en particulier en utilisant les sélecteurs spéciaux.

|| Sélecteur de classe | Sélecteur d'ID |
| --- | --- | --- |
| Description | Style appliqué à tous les éléments d'une page appartenant à la même classe. | Style appliqué à l'unique élément d'une page appartenant à l'identificateur. |
| Syntaxe dans le document HTML |  `<p class="menu">...</p>` | `<p id="2">...</p>` |
| Syntaxe dans la feuille de style CSS | `.menu { ... }` | `#2 { ... }` | 

### d) Mémo des règles CSS

| Nom de la règle | Syntaxe CSS |
| --- | --- |
| Alignement de texte centré | `p { text-align : center ;}` |
| Alignement de texte gauche | `p { text-align : left ;}` |
| Décoration de texte souligné | `p { text-decoration-line : underline ;}` |
| Décoration de texte barré | `p { text-decoration: line-through ;}` |
| Police de texte Times New Roman | `p { font-family: "Times New Roman" ;}` |
| Taille de la police 40 pixels | `p { font-size: 40px ;}` |
| Couleur de texte rouge | `p { color : red ;}` |
| Couleur d'arrière-plan du texte | `p { background-color : red ;}` |

## III. Formulaires

Nous avons vus dans la leçon précédente que le passage de paramètre pouvait se produire de deux façons différentes :

- La première via l'URL.

- La seconde lorsque l'utilisateur soumet lui-même des informations dans un formulaire.

### a) Écriture d'un formulaire

Écrire un formulaire en HTML se fait à l'aide de la balise `form` :

```html
<form action=... method= ...>
    ...
</form>
```

- L'attribut `action` définit l'emplacement (une URL) où doivent être envoyées les données collectées par le formulaire.

- L'attribut `method` définit la méthode HTTP utilisée pour envoyer les données (cela peut être « get » ou « post »).

### b) 

<!DOCTYPE html>
 <html>
 <head>
  <title> Formulaire en HTML </title>
</head>
 <body>
     <h2> Formulaire d'inscription </h2>
    <form>
     <fieldset>
        <legend> Informations personnelles de l'utilisateur </legend>
        <label> Entrez votre nom complet </label> <br>
        <input type = "text" name = "name"> <br>
         <label> Entrez votre email </label> <br>
         <input type = "email" name = "email"> <br>
         <label> Entrez votre mot de passe </label> <br>
         <input type = "password" name = "pass"> <br>
         <label> confirmez votre mot de passe </label> <br>
         <input type = "password" name = "pass"> <br>
         <br> <label> Entrez votre sexe </label> <br>
         <input type = "radio" id = "genre" name = "genre" value = "homme"/> Homme <br>
         <input type = "radio" id = "genre" name = "sexe" value = "femme"/> Femme <br/>
         <input type = "radio" id = "genre" name = "genre" value = "autres"/> autres <br/>
          <br> Entrez votre adresse: <br>
         <textarea> </textarea> <br>
         <type d'entrée = "submit" value = "inscription">
     </fieldset>
  </form>
 </body>
</html>

_____________

[Sommaire](./../README.md)