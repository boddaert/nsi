# Le sujet

## Introduction

L'intelligence artificielle est un domaine informatique et est aujourd'hui très présente dans énormément de secteurs d'activités tels que l'automobile, l'énergie, l'industrie, la santé, la recherche et même l'art comme cela est indiqué sur le site officiel du [Parlement Européen](https://www.europarl.europa.eu/news/fr/headlines/society/20200827STO85804/intelligence-artificielle-definition-et-utilisation).

Aucun secteur n'est épargné. Pour certains, elle devient indispensable.

Son développement et son utilisation est désormais un sujet d'actualité. On parle dans les médias de voitures autonomes, de robots, de reconnaissance faciale, de services de navigation, ou encore d'assistants intelligents intégrés.

Récemment, le système informatique Chat GPT (*Generative Pre-trained Transformer*) est disponible en ligne. Tirant parti de l'intelligence artificielle, il entre en conversation avec l'utilisateur humain et répond à ses questions.

Lorsque l'on en prend conscience, on se rend compte que nous utilisons l'intelligence artificielle au quotidien plusieurs fois à travers différents objets connectés.

Pourtant, nous ne savons pas comment cela fonctionne concrètement.

## Présentation du sujet

Ce mémoire traite de plusieurs objectifs dont le point commun est l'étude de l'apprentissage par renforcement, un domaine de l'intelligence artificielle.

Le mémoire est constitué d'un état de l'art des connaissances et des travaux sur l'apprentissage par renforcement.

Dans une seconde partie didactique, il s'agit de concevoir une stratégie et une méthodologie afin d'expérimenter avec les élèves l'apprentissage par renforcement.

### Origines de l'intelligence artificielle

​L'idée de l'intelligence artificielle semble apparaître dans les années 1950 lorsqu'Alan Turing se demande si une machine peut "penser" comme un être humain.

Mais c'est surtout grâce John McCarthy et son équipe en 1956 lors d'une conférence intitulée *Dartmouth Summer Research Project on Artificial Intelligence* que l'intelligence artificielle devient un domaine de recherche international.

Dans les années 1980, l'apprentissage automatique se développe. L'ordinateur commence à déduire des "règles à suivre" en analysant des données.

Puis, en 1997, l'ordinateur doté de l'intelligence artificielle *Deep Blue* bat le champion du monde Garry Kasparov aux échecs lors d'un match à six parties.

Depuis, de nouvelles puissances et infrastructures de calcul permettent de repousser toujours plus loin les limites de l'intelligence artificielle. Elle cherche maintenant à relever plusieurs défis dont la perception visuelle, la compréhension du langage naturel ou la prise de décision autonome.

### Définition de l'intelligence artificielle

L'intelligence artificielle est une étude de l'informatique cherchant à confectionner des machines capables de simuler l'intelligence humaine.

Elle repose sur des données et des programmes informatiques. Le terme "artificiel" désigne donc l'usage d'ordinateurs et d'électronique.

L'intelligence artificielle permet de compléter des tâches de manière plus satisfaisante que si elles étaient effectuées par les humains. Ces tâches demandent généralement une grosse puissance de calcul, c'est pourquoi il est plus performant de les faire par des machines. Le terme "intelligence" de "intelligence artificielle" traduit alors le but d'imiter le comportement humain.

L'intelligence artificielle se décline en plusieurs branches dont une est appelée "apprentissage automatique".

L'apprentissage automatique (ou *machine learning*) se fonde sur des approches mathématiques et statistiques pour donner aux machines la capacité de prendre des décisions à partir de données.

Cela consiste à entraîner des modèles de manière spécifique à l'algorithme d'apprentissage.

On distingue deux algorithmes d'apprentissage automatique : l'apprentissage supervisé et l'apprentissage non-supervisé.

### Apprentissage supervisé

L'apprentissage supervisé consiste à prendre une décision selon un jeu de données.

Le jeu de données est étiqueté, c'est-à-dire que ces données sont déjà classifiées.

A partir de données étiquetées, l'algorithme s'entraîne et connaît désormais ce qu'il doit chercher : un ou plusieurs éléments caractéristiques.

A la fin de la phase d'entraînement, l'algorithme est capable de classifier une donnée non étiquetée à partir de ses caractéristiques.

On peut classifier de deux façons :

- Attribuer une classe à un objet (Algorithme de classification)

- Attribuer une probabilité (Algorithme de régression)

Prenons par exemple le problème de la classification d'images de chiens et de chats.

Considérons un jeu de données comportant des milliers d'images de chiens ou de chats et étant déjà classifiées sur l'ordinateur.

Au cours de l'apprentissage, le programme parcourt le jeu de données et se rend compte que sur les images de chiens, la truffe est noire tandis que sur celles des chats, la truffe est rose.

A la fin de l'apprentissage et pour une nouvelle image, le programme sera capable de déterminer à quelle classe appartient l'image ou les probabilités selon laquelle l'image est un chien ou un chat d'après la couleur des pixels représentant la truffe de l'animal.

### Apprentissage non-supervisé

L'apprentissage non-supervisé consiste également à prendre une décision selon un jeu de données, mais cette fois, les données ne sont pas étiquetées.

L'algorithme parcourt les données sans indice et tente d'y découvrir des motifs ou des tendances récurrents.

Cette approche est notamment utilisée dans la cybersécurité.

### Apprentissage par renforcement

Les algorithmes d'apprentissage par renforcement (ou *reinforcement learning*) sont des algorithmes d'apprentissage non-supervisé, puisqu'ils ne travaillent pas avec un jeu de données étiqueté.

En apprentissage par renforcement, l'algorithme apprend en essayant encore et encore jusqu'à atteindre un objectif précis. Il pourra essayer toutes sortes de techniques pour y parvenir.

Pour appuyer le renforcement à chaque essai, l'agent, l'objet qui prend les décisions, est récompensé s'il approche du but, ou pénalisé s'il échoue.

De cette manière, il va éviter les mauvaises décisions, celles qui le pénalisent, et va priviligier les meilleures décisions.

En tentant d'obtenir le plus de récompenses possible, il s'améliore progressivement.

L'idée d'apprendre en essayant encore et encore est probablement la première idée qui nous vient à l'esprit lorsque nous pensons à la nature de l'apprentissage.

Pour comprendre le fonctionnement d'un algorithme d'apprentissage par renforcement, nous pouvons le comparer au dressage d'un animal de compagnie.

L'animal de compagnie ne comprend pas le langage humain, il est impossible de lui expliquer verbalement ce qu'il doit faire. Par contre, il est possible de provoquer une réaction de l'animal en créant une situation.

Si la réaction de l'animal est bonne, on peut le récompenser. Un chien qui donne la patte dans la situation où on lui a dit "donne la patte" peut recevoir un biscuit en récompense.

Grâce aux récompenses, l'animal de compagnie sera progressivement conditionné et pourra exécuter l'action lui permettant de recevoir un biscuit lorsqu'il sera confronté à la même situation.

Ainsi, sans même comprendre les mots, et cherchant à obtenir le plus de récompenses possible, un chien peut donner la patte quand on lui dira "donne la patte". De la même manière, on peut lui apprendre à ne pas faire de bêtises en le punissant.

## Contexte

Les algorithmes d'apprentissage par renforcement sont généralement utilisés lorsqu'il faut résoudre des problèmes d'optimisation, c'est-à-dire lorsqu'il est nécessaire de maximiser une fonction sur un ensemble discret sous une ou plusieurs contraintes.

En l'occurrence, les algorithmes d'apprentissage par renforcement cherchent à maximiser les récompenses.

### Dans les jeux

Les programmes informatiques basés sur un algorithme d'apprentissage par renforcement excellent dans les jeux de plateaux. Nous pouvons citer l'intelligence artificielle *DeepMind AlphaGo* qui est parvenue à surpasser Lee Sedol, le champion du monde de Go.

Par la suite, la nouvelle version *AlphaGo Zero* a appris le jeu de Go uniquement en jouant contre lui-même en continu durant 40 jours. Ce nouveau système a, depuis, triomphé de la première version d'*AlphaGo*.

### Dans les véhicules autonomes

Ce type d'apprentissage est également utilisé par les véhicules autonomes, ces véhicules devant apprendre à rester sur la route. Un exemple d'utilisation de ce type d'algorithme d'apprentissage sur les voitures autonomes sera détaillé dans le chapitre suivant.


### Dans la médecine

Dans le domaine de la médecine, les programmes écrits via l'apprentissage par renforcement peuvent apprendre à dispenser les traitements optimaux aux patients. Pour y parvenir, ils se basent sur les expériences de précédents patients afin d'automatiser le diagnostic.

L'apprentissage par renforcement permet une meilleure anticipation des effets secondaires sur le long terme.

## Apports dans le cadre de la formation et/ou du métier

L'écriture de ce mémoire a personnellement été une grande source de réflexion tant sur l'aspect informatique que sur l'aspect didactique et pédagogique.

La lecture de divers papiers scientifiques dans le cadre de ma recherche m'a donné un point de vue supplémentaire sur l'informatique. Cela m'a permis d'une part de comprendre précisément les rouages de l'intelligence artificielle, et d'autres parts de découvrir, comprendre plusieurs algorithmes d'apprentissage complexes, de pouvoir les écrire moi-même et de les exploiter à des fins didactiques.

Réfléchir à l'élaboration d'une stratégie et d'une méthodologie m'ont fait prendre conscience de tout l'effort nécessaire pour concevoir une activité parfaitement claire et encadrée. J'ai fixé à cette partie didactique et pédagogique l'objectif d'élever vers le haut les connaissances et compétences des élèves.

Ce mémoire est pour moi l'accomplissement et le projet de fin d'études de deux années en master MEEF Informatique.
