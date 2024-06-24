# Scénario pédagogique 22/05

### Structuration de l'apprentissage

- Rituel d'entrée

- PLAN "Ce matin, nous allons revenir sur l'activité sur laquelle vous avez travailler mercredi dernier. Nous parlerons ensuite d'intelligence artificielle. Enfin, je vous redistribuerai le questionnaire que vous avez rempli il y a trois semaines afin de constater si vous vous êtes améliorés."

- DIAPO OBJECTIF "Rappelez-vous, l'objectif de l'activité était de trouver quel était l'avantage qu'obtenait la colonie si ses fourmis respectaient les règles de la partie. Qui peut me redonner cet avantage ?"

- DIAPO IDEE ALGO -> "C'est dans les années 1990 que les chercheurs ont découvert l'idée de l'algorithme des colonies de fourmis" LIRE "Mais comment font-elles pour trouver de manière systématique le chemin le plut court ?"

- DIAPO RETOUR SUR ACTIVITE  -> LIRE + démonstration

- DIAPO NOMBRE DE FOURMIS "Pourtant, en observant vos plateaux, il y en a peu parmi vous qui ont découvert le chemin le plus court. C'est notamment parce que vous ne pouviez utiliser que 30 fourmis ! Le nombre de fourmis déployées est l'un des paramètre de réussite. Voici par exemple un graphique représentant le nombre de parties gagnée et échouées en fonction du nombre de fourmis utilisées, on dit qu'une partie est gagnée si on a trouvé le chemin le plus court. On remarque que plus j'utilise de fourmis, plus je trouve le chemin le plus court."

- DIAPO EVAPORATION "On m'a également fais la remarque suivante : Mais monsieur, les fourmis qui empruntent un chemin plus long, elles aussi vont déposer des phéromones et donc certaines fourmis vont se tromper de chemin. C'est pourquoi il existe un autre paramètre de réussite : l'évaporation. Comme dans la nature, les phéromones finissent par disparaître avec le temps, cela permet d'éffacer les chemins qui sont moins fréquentés, autrement dit de faire effacer les chemins longs"

- VIDEO SIMULATION 
  
  - "Comme sur le plateau, on remarque une colonie de fourmis et des sources de nourriture. Sauf que sur le plateau il n'existait qu'un nombre de chemin limité, ici il y en a beaucoup plus !"
  
  - "Comme dans l'activité, les fourmis sont lâchées de manière aléatoire. Sur le plateau on avait le choix entre le chemin rouge, violet et jaune."
  
  - "Ici les phéromones bleues ne sont pas les phéromones d'attirance, ce sont juste des phéromones pour indiquer qu'elles sont passées par là. Ce ne sont pas ces phéromones qui nous interresse"
  
  - "Donc elles parcourt au hasard leur environnement jusqu'à ce que certaines d'entre elles trouvent de la nourriture, elles reviennent alors à la colonie en déposant des phéromones d'attirance, les points rouges"
  
  - "Ici, on voit que les fourmis qui trouvent la piste rouge vont à leur tour aller chercher la nourriture et revenir à la colonie tout en renforcçant la piste de leurs phéromones."
  
  - "Une fois qu'il n'y a plus de nourriture, la piste s'efface, c'est l'évaporation et les fourmis reparcourent à nouveau leur environnement de manière aléatoire."
  
  - "Ici, on voit que les fourmis n'empruntent pas un chemin plus court, mais après quelque temps, quelques fourmis empruntent un raccourci, comme elles reviennent plus vite à la colonie, cette piste là est alors renforcée, puis la seconde disparaît"

- DIAPO UTILISATIONS CONCRETES "Alors qu'a permis de faire cet algorithme dans la vie de tous les jours ? De manière générale, il répond à tous les problemes de recherche de plus court chemin dans un graphe. Par exemple, dans le réseau internet, on cherche quel est le chemin le plus court et donc le plus rapide entre deux ordinateurs. On a aussi le problème de recherche d'un intinéraire efficace lors du ramassage des déchets ou encore la recherche d'un itinéraire efficace pour la livraison de colis ou de la livraison de repas à domicile."

- DIAPO APPRENTISSAGE "Cet algorithme est en fait ce qu'on appelle un algorithme d'apprentissage par renforcement et est en fait de l'intelligence artificielle"

----------------

### Présentation de l'intelligence artificielle

- PLAN "Alors maintenant, je vais tenter de vous faire découvrir l'intelligence artificielle. Je vais tout d'abord vous faire une présentation générale autour de l'IA où nous allons essayer de définir les termes "Intelligence artificielle", puis de voir précisément ce que veut dire du "machine learning" ou "apprentissage automatique" en français."

- DIAPO IMAGES CONSIGNE "Sur les diapos qui vont suivre, vous allez lever la pancarte verte si vous pensez que l'image a un rapport avec l'intelligence artificielle, rouge sinon".
  
  - Image du robot : "Il faut faire attention à bien dissocier la robotique de l'intelligence artificielle : les robots des chaînes de montage n'ont pas d'IA et les outils d'IA comme ChatGPT ne sont pas des robots. Pour réussir à savoir s'il s'agit d'IA ou non, on peut se poser la question suivante : le robot effectue t-il les tâches mécaniquement ou en prenant une décision ?"

- DIAPO DEFINITION "Pour tenter de définir ce que veut dire Intelligence Artificielle, nous allons d'abord essayer de définir les mots Intelligence et Artificielle séparément"
  
  "Si nous partons du principe que nous sommes les seuls animaux intelligents, le mot intelligence décrit en fait l'intelligence humaine et tout ce qu'on est capable de faire"
  
  "Le mot artificielle indique l'emploi uniquement de choses non-vivantes comme les outils electroniques"
  
  CONSIGNE "Sur votre feuille, écrivez une petite phrase avec vos propres mots une définition de l'intelligence artificielle"

- DIAPO ORIGINES "C'est en 1950 que l'idée d'IA a été imaginée pour la première fois par Alan Turing lorsqu'il se demandait si des machines pouvaient avoir une conscience. Mais c'est surtout en 1956 que John McCarthy et son équipe qui ont énoncé pour la première fois de l'histoire les mots Intelligence artificielle lors d'une conférence aux Etats-Unis. Puis avec le progrès toujours plus conséquent, c'est en 1997 que le champion du monde Gary Kasparov perd aux échecs contre l'IA Deep Blue et c'est à ce moment que l'on s'est rendu compte de la puissance de l'IA"

- DIAPO APPRENTISSAGE AUTOMATIQUE "L'IA est un domaine de recherche qui peut être découpée en plusieurs parties, par exemple, on peut parler d'éthique ou de juridique mais on va surtout parler aujourd'hui d'apprentissage automatique"

- DIAPO PHASES "Les algorithmes d'apprentissage automatique possèdent deux phases : une phase d'apprentissage où l'algorithme va apprendre et une phase de décision où l'algorithme va décider. De manière générale, ces algorithmes vont appliquer un très grand nombre de fois des règles simples."

- DIAPO CHIENS CHATS "Imaginons que l'on confie à une IA des milliers d'images de chiens et de chats son objectif est de retrouver s'il s'agit d'un chat ou un chien sur une nouvelle image. Lors de la phase d'apprentissage, l'algorithme se rend compte que sur les images de chiens, les pixels de la truffe est plutôt noire tandis que sur celles des chats, elle est rose."

- DIAPO CHIENS CHATS "Avec ce qu'il a appris, l'algorithme va pouvoir décider s'il s'agit d'un chien ou d'un chat sur la nouvelle image en regardant la couleur des pixels de la truffe"

- DIAPO PAR RENFORCEMENT "L'idée de ce genre d'algorithmes est basé sur une manière naturelle d'apprendre, celle de l'essai-erreur. En effet, l'agent IA va effectuer une action sur son environnement et on va lui donner une récompense selon si l'action est satisfaisante ou non. L'objectif de l'agent est de maximiser les récompenses."

- DIAPO CHIEN RENFORCEMENT "On peut comparer l'idée de ces algorithmes avec le dressage d'un chien : Imaginons que l'on veuille que le chien donne la patte lorsque l'on lui dit. Le chien ne comprenant pas le français, il ne vas pas tout de suite donner la patte mais lorsqu'il le fera, on lui donnera une récompense comme un biscuit. Avec le temps, le chien associera l'ordre qu'on lui donne avec le geste."
