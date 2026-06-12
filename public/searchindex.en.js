var relearn_searchindex = [
  {
    "breadcrumb": "Créer un jeu vidéo",
    "content": "This is a new chapter.",
    "description": "This is a new chapter.",
    "tags": [],
    "title": "Unreal Engine 5",
    "uri": "/unreal-engine-5/index.html"
  },
  {
    "breadcrumb": "Créer un jeu vidéo \u003e Unreal Engine 5",
    "content": "This is a new chapter.",
    "description": "This is a new chapter.",
    "tags": [],
    "title": "Créer un Système de Build pas à pas dans Unreal Engine",
    "uri": "/unreal-engine-5/systeme-construction/index.html"
  },
  {
    "breadcrumb": "",
    "content": "",
    "description": "",
    "tags": [],
    "title": "Créer un jeu vidéo",
    "uri": "/index.html"
  },
  {
    "breadcrumb": "Créer un jeu vidéo \u003e Unreal Engine 5",
    "content": "Introduction de la vidéo / de l’article Écris ton contenu ici en utilisant le format Markdown…\n1. Première étape 2. Deuxième étape 📺 Ma Chaîne YouTube Des tutoriels vidéo complémentaires pour aller plus loin.\nS'abonner à la chaîne 📦 Ressources 📂 Index des tutoriels 💻 Code source \u0026 Scripts 💾 Téléchargements 🌐 Communauté 🐦 Twitter / X 💼 LinkedIn 💬 Serveur Discord © 2026 - Créé avec ❤️ sous Hugo \u0026 Relearn. Mentions légales Confidentialité (RGPD)",
    "description": "Introduction de la vidéo / de l’article Écris ton contenu ici en utilisant le format Markdown…\n1. Première étape 2. Deuxième étape 📺 Ma Chaîne YouTube Des tutoriels vidéo complémentaires pour aller plus loin.",
    "tags": [],
    "title": "Input Mapping",
    "uri": "/unreal-engine-5/input-mapping/index.html"
  },
  {
    "breadcrumb": "Créer un jeu vidéo \u003e Tags",
    "content": "",
    "description": "",
    "tags": [],
    "title": "Tag :: Blueprints",
    "uri": "/tags/blueprints/index.html"
  },
  {
    "breadcrumb": "Créer un jeu vidéo \u003e Tags",
    "content": "",
    "description": "",
    "tags": [],
    "title": "Tag :: Game Design",
    "uri": "/tags/game-design/index.html"
  },
  {
    "breadcrumb": "Créer un jeu vidéo \u003e Unreal Engine 5 \u003e Créer un Système de Build pas à pas dans Unreal Engine",
    "content": "Ce tutoriel est issu de mes archives et est partagé pour son intérêt conceptuel.\nDans cette première partie d’une mini-série consacrée aux systèmes de construction (similaires à ceux des jeux de survie ou de Fortnite), nous posons les bases techniques indispensables pour permettre au joueur de prévisualiser et de poser des structures dans le monde.\nConcepts clés abordés dans ce tutoriel Mise en place de l’environnement : Utilisation du modèle First Person Template nettoyé et import de meshes spécifiques conçus pour s’empiler parfaitement (murs, sols, fenêtres, toits). Création du Master Material “Ghost” : * Configuration d’un matériau translucide vert servant de guide visuel avant le placement de l’objet. Utilisation de paramètres de type Vector (Color) et Scalar (Opacity) modifiables par la suite via des instances. Activation de l’option Two-Sided pour donner du relief et de la visibilité aux faces internes de la prévisualisation. Architecture Blueprint Parent-Enfant (POO) : Création d’un Blueprint Maître (MBP_BuildBlock) englobant la logique commune à toutes les structures. Génération d’un Blueprint Enfant (BP_BuildWall) qui hérite automatiquement des propriétés et des événements du parent. Logique de l’Event Graph pour le placement : Phase de prévisualisation : Sauvegarde du matériau d’origine dans une variable au chargement de l’acteur, application du matériau Ghost et désactivation complète des collisions pour éviter les conflits avec le décor. Phase de validation (Custom Event Placed) : Bascule d’une variable booléenne IsPlaced à True, réapplication du matériau d’origine et réactivation de collisions optimisées (Query Only) pour économiser les ressources. Configuration des Inputs : Création d’un nouveau mapping d’action (Build Mode) assigné par défaut à la touche B pour entrer ou sortir du mode construction. Ce qui reste d’actualité aujourd’hui Bien que ce tutoriel utilise une logique initialement pensée pour Unreal Engine 4, les mécaniques présentées forment les piliers immuables du gamedev moderne :\nLa programmation orientée objet (Parents/Enfants) : Structurer ses architectures avec un Blueprint maître reste la meilleure méthode sur Unreal Engine 5 pour concevoir un système de build évolutif sans jamais dupliquer son code. L’optimisation des matériaux : L’usage de Master Materials paramétriques destinés à être déclinés en Material Instances est toujours la norme absolue pour préserver les performances graphiques et la mémoire vidéo. La gestion fine des collisions : Passer par un état “No Collision” durant la prévisualisation, puis réactiver des profils légers comme le Query Only, reste la technique standard pour éviter les bugs physiques et les chutes de framerate lors de l’empilement d’objets. ⬅️ Vidéo Précédente Vidéo Suivante ➡️ 📺 Ma Chaîne YouTube Des tutoriels vidéo complémentaires pour aller plus loin.\nS'abonner à la chaîne 📦 Ressources 📂 Index des tutoriels 💻 Code source \u0026 Scripts 💾 Téléchargements 🌐 Communauté 🐦 Twitter / X 💼 LinkedIn 💬 Serveur Discord © 2026 - Créé avec ❤️ sous Hugo \u0026 Relearn. Mentions légales Confidentialité (RGPD)",
    "description": "Ce tutoriel est issu de mes archives et est partagé pour son intérêt conceptuel.\nDans cette première partie d’une mini-série consacrée aux systèmes de construction (similaires à ceux des jeux de survie ou de Fortnite), nous posons les bases techniques indispensables pour permettre au joueur de prévisualiser et de poser des structures dans le monde.",
    "tags": [
      "Unreal Engine",
      "Blueprints",
      "Game Design",
      "Tutoriel"
    ],
    "title": "Partie 1 : Les Fondations et le Ghost",
    "uri": "/unreal-engine-5/systeme-construction/cours-1/index.html"
  },
  {
    "breadcrumb": "Créer un jeu vidéo \u003e Unreal Engine 5 \u003e Créer un Système de Build pas à pas dans Unreal Engine",
    "content": "Ce tutoriel est issu de mes archives et est partagé pour son intérêt conceptuel.\nDans cette deuxième partie, nous passons à la vitesse supérieure en connectant le personnage à notre système de construction. L’objectif est de projeter la prévisualisation dans le monde via un tracé de ligne, d’autoriser la rotation du bloc et de valider sa pose finale.\nConcepts clés abordés dans ce tutoriel Gestion de la rotation du Ghost : Configuration de l’input de rotation (touche R) dans les paramètres du projet. Utilisation de l’événement Mouse Wheel combiné à une logique d’incrémentation d’angle (+90° ou -90°) pour faire pivoter le Blueprint de prévisualisation de manière fluide et précise avant la pose. Le Tracé de Ligne (Line Trace by Channel) : Récupération de la position et du vecteur de direction de la caméra du joueur (Get World Location et Get Forward Vector). Calcul de la portée maximale de construction en multipliant le vecteur de direction par une constante (ex: 1500 unités) pour obtenir le point d’arrivée du tracé dans l’espace 3D. Logique de Tick et Spawn Dynamique : À chaque frame (Event Tick), si le mode construction est actif, le système effectue le Line Trace. Si le tracé ne touche rien, le Ghost se positionne par défaut au bout de la ligne de portée. S’il y a un impact (Hit Result), l’emplacement du Ghost est immédiatement mis à jour sur le point d’impact. Instanciation et Transition (Spawn \u0026 Place) : Création d’une fonction pour faire apparaître proprement l’acteur de prévisualisation (Spawn Actor from Class) dès l’activation du mode build. Gestion de la validation avec le clic gauche de la souris : appel du Custom Event Placed (développé en partie 1) qui fige le bloc dans le monde, réactive ses collisions, puis instancie immédiatement un nouveau Ghost pour permettre au joueur de continuer à construire en continu. Ce qui reste d’actualité aujourd’hui Bien que les menus ou certains noms de nœuds aient légèrement évolué avec Unreal Engine 5, les concepts de Game Design Engineer présentés ici restent indispensables :\nLe Line Tracing pour l’interaction : Que ce soit sur UE4 ou UE5, l’utilisation d’un Line Trace (ou Raycast) basé sur la caméra reste la méthode standard et la plus optimisée pour savoir exactement ce que le joueur regarde et où il souhaite interagir avec le décor. Le découplage de la prévisualisation (Ghost vs Objet Physique) : Séparer la logique du “fantôme” temporaire et de l’objet solidifié dans le monde est le seul moyen propre de gérer les performances, évitant ainsi de charger des calculs physiques ou des scripts complexes tant que l’objet n’est pas officiellement posé. Le flux séquentiel des fonctions : Organiser ses scripts en vérifiant systématiquement la validité des pointeurs (les nœuds Is Valid) avant de manipuler un acteur en mémoire reste la règle d’or pour s’assurer qu’un jeu ne plante pas (Crash / Access Violation) en cours de partie. ⬅️ Vidéo Précédente Vidéo Suivante ➡️ 📺 Ma Chaîne YouTube Des tutoriels vidéo complémentaires pour aller plus loin.\nS'abonner à la chaîne 📦 Ressources 📂 Index des tutoriels 💻 Code source \u0026 Scripts 💾 Téléchargements 🌐 Communauté 🐦 Twitter / X 💼 LinkedIn 💬 Serveur Discord © 2026 - Créé avec ❤️ sous Hugo \u0026 Relearn. Mentions légales Confidentialité (RGPD)",
    "description": "Ce tutoriel est issu de mes archives et est partagé pour son intérêt conceptuel.\nDans cette deuxième partie, nous passons à la vitesse supérieure en connectant le personnage à notre système de construction. L’objectif est de projeter la prévisualisation dans le monde via un tracé de ligne, d’autoriser la rotation du bloc et de valider sa pose finale.",
    "tags": [
      "Unreal Engine",
      "Blueprints",
      "Game Design",
      "Tutoriel"
    ],
    "title": "Partie 2 : Rotation, Tracé de Ligne et Pose des Blocs",
    "uri": "/unreal-engine-5/systeme-construction/cours-2/index.html"
  },
  {
    "breadcrumb": "Créer un jeu vidéo \u003e Unreal Engine 5 \u003e Créer un Système de Build pas à pas dans Unreal Engine",
    "content": "Ce tutoriel est issu de mes archives et est partagé pour son intérêt conceptuel.\nDans cette troisième partie, nous abordons un aspect crucial du confort de jeu et de la robustesse technique : la gestion des collisions aberrantes. L’objectif est d’empêcher le joueur de tricher ou de casser l’immersion en superposant des structures les unes sur les autres, en mettant en place un retour visuel dynamique (vert/rouge).\nConcepts clés abordés dans ce tutoriel Détection des volumes superposés (Overlap) : Utilisation des événements On Component Begin Overlap et On Component End Overlap sur la boîte de collision (Box Collision) de notre Blueprint Maître. Filtrage des détections pour ignorer le joueur lui-même et s’assurer que le Ghost ne réagit qu’aux autres blocs de construction déjà solidifiés dans le monde. Gestion d’un compteur d’interférences : Création d’une variable entière Overlap Count pour suivre le nombre d’objets en collision avec le Ghost. Incrémentation (+1) lorsqu’un objet entre dans la zone et décrémentation (-1) lorsqu’il en sort, évitant ainsi les faux négatifs si le Ghost touche plusieurs structures simultanément. Changement dynamique de couleur du Ghost : Exploitation des Material Instances pour modifier à la volée les paramètres vectoriels du matériau translucide. Création d’une fonction de mise à jour visuelle : application d’une couleur verte si Overlap Count est égal à 0 (placement valide) et bascule sur une couleur rouge d’alerte dès que le compteur est supérieur à 0 (placement invalide). Conditionnalité de la validation (Le Booléen de contrôle) : Introduction d’une variable booléenne CanBuild mise à jour en temps réel selon l’état du compteur d’overlaps. Branchement d’un nœud de condition (Branch) sur l’action de clic gauche du joueur pour bloquer l’appel de l’événement Placed tant que la zone n’est pas totalement dégagée. Ce qui reste d’actualité aujourd’hui Les outils visuels d’Unreal Engine 5 ont été modernisés, mais la logique systémique sous-jacente reste inchangée pour tout développeur de jeux de survie ou de gestion :\nLa technique du compteur d’overlaps (Counter vs Boolean) : Utiliser un compteur d’objets plutôt qu’un simple booléen True/False lors des intersections reste la méthode standard en gamedev. Cela empêche le système de croire à tort que la voie est libre lorsqu’un premier objet quitte la zone alors qu’un deuxième s’y trouve encore. Le feedback visuel immédiat (Juiciness) : Changer la couleur d’un hologramme (vert/rouge) est une règle d’or d’UX (User Experience). Donner une réponse instantanée aux actions du joueur avant même qu’il ne clique est indispensable pour éviter la frustration. L’optimisation par événements plutôt qu’en Tick : Bien que la position du Ghost soit rafraîchie à chaque frame, la vérification de la validité du placement est entièrement gérée par des événements de collision (Begin/End Overlap). Cette approche événementielle est toujours indispensable aujourd’hui pour économiser du temps CPU. 📺 Ma Chaîne YouTube Des tutoriels vidéo complémentaires pour aller plus loin.\nS'abonner à la chaîne 📦 Ressources 📂 Index des tutoriels 💻 Code source \u0026 Scripts 💾 Téléchargements 🌐 Communauté 🐦 Twitter / X 💼 LinkedIn 💬 Serveur Discord © 2026 - Créé avec ❤️ sous Hugo \u0026 Relearn. Mentions légales Confidentialité (RGPD)",
    "description": "Ce tutoriel est issu de mes archives et est partagé pour son intérêt conceptuel.\nDans cette troisième partie, nous abordons un aspect crucial du confort de jeu et de la robustesse technique : la gestion des collisions aberrantes. L’objectif est d’empêcher le joueur de tricher ou de casser l’immersion en superposant des structures les unes sur les autres, en mettant en place un retour visuel dynamique (vert/rouge).",
    "tags": [
      "Unreal Engine",
      "Blueprints",
      "Game Design",
      "Tutoriel"
    ],
    "title": "Partie 3 : Gestion des Overlaps et Interdiction de Placement",
    "uri": "/unreal-engine-5/systeme-construction/cours-3/index.html"
  },
  {
    "breadcrumb": "Créer un jeu vidéo \u003e Unreal Engine 5 \u003e Créer un Système de Build pas à pas dans Unreal Engine",
    "content": "Ce tutoriel est issu de mes archives et est partagé pour son intérêt conceptuel.\nDans ce quatrième épisode, nous enrichissons l’expérience utilisateur en permettant au joueur de naviguer de manière fluide entre plusieurs types de structures (murs, sols, toits) à l’aide de la molette de la souris, tout en implémentant les bases d’un mode de destruction pour nettoyer ses chantiers.\nConcepts clés abordés dans ce tutoriel Gestion d’un inventaire de structures via Array : Création d’une variable de type Tableau (Array) contenant les classes de nos Blueprints enfants (BP_BuildWall, BP_BuildFloor, etc.). Utilisation d’une variable d’index entier (CurrentIndex) pour suivre le bloc actuellement sélectionné par le joueur. Logique de défilement cyclique (Scroll) : Interception des inputs de la molette de la souris (Mouse Scroll Up et Mouse Scroll Down). Implémentation d’un système de boucle mathématique : incrémentation ou décrémentation de l’index, avec réinitialisation automatique à 0 si l’on dépasse la taille maximale du tableau, ou bascule sur le dernier élément si l’on descend en dessous de zéro. Changement dynamique d’acteur en temps réel : Destruction instantanée du Ghost actuel dès qu’un changement de sélection est détecté. Réinitialisation de la fonction de Spawn pour faire apparaître immédiatement le nouveau modèle sélectionné, garantissant une transition visuelle transparente pour le joueur. Introduction du mode destruction (Demolish) : Configuration d’une touche dédiée (ex: X) pour basculer entre le mode “Pose” et le mode “Destruction”. Utilisation du tracé de ligne (Line Trace) existant : si le rayon touche un bloc de construction déjà posé dans le monde, l’appui sur le clic gauche déclenche la fonction Destroy Actor pour supprimer instantanément la structure visée. Ce qui reste d’actualité aujourd’hui Bien que l’architecture des entrées utilisateur ait évolué avec le système Enhanced Input d’Unreal Engine 5, la logique algorithmique demeure identique :\nLa puissance des tableaux (Arrays) de classes : Utiliser un tableau pour stocker des classes d’acteurs afin de les instancier dynamiquement est la méthode universelle pour créer des barres d’action, des inventaires ou des menus de sélection dans n’importe quel moteur de jeu. Le nettoyage des acteurs en mémoire : Penser à détruire proprement l’ancien Ghost (Destroy Actor) avant d’en recréer un nouveau à chaque coup de molette est un réflexe de programmation essentiel pour éviter les fuites de mémoire (Memory Leaks) et la multiplication d’objets invisibles. Le recyclage des tracés de rayons (Line Trace) : Utiliser la même logique de détection de visée (le Line Trace de la caméra) à la fois pour poser un bloc et pour le cibler en mode destruction est un excellent exemple de réutilisation de code propre (DRY - Don’t Repeat Yourself), optimisant ainsi les performances de scripts. 📺 Ma Chaîne YouTube Des tutoriels vidéo complémentaires pour aller plus loin.\nS'abonner à la chaîne 📦 Ressources 📂 Index des tutoriels 💻 Code source \u0026 Scripts 💾 Téléchargements 🌐 Communauté 🐦 Twitter / X 💼 LinkedIn 💬 Serveur Discord © 2026 - Créé avec ❤️ sous Hugo \u0026 Relearn. Mentions légales Confidentialité (RGPD)",
    "description": "Ce tutoriel est issu de mes archives et est partagé pour son intérêt conceptuel.\nDans ce quatrième épisode, nous enrichissons l’expérience utilisateur en permettant au joueur de naviguer de manière fluide entre plusieurs types de structures (murs, sols, toits) à l’aide de la molette de la souris, tout en implémentant les bases d’un mode de destruction pour nettoyer ses chantiers.",
    "tags": [
      "Unreal Engine",
      "Blueprints",
      "Game Design",
      "Tutoriel"
    ],
    "title": "Partie 4 : Sélection des Blocs à la Molette et Système de Destruction",
    "uri": "/unreal-engine-5/systeme-construction/cours-4/index.html"
  },
  {
    "breadcrumb": "Créer un jeu vidéo",
    "content": "",
    "description": "",
    "tags": [],
    "title": "Tags",
    "uri": "/tags/index.html"
  },
  {
    "breadcrumb": "Créer un jeu vidéo \u003e Tags",
    "content": "",
    "description": "",
    "tags": [],
    "title": "Tag :: Tutoriel",
    "uri": "/tags/tutoriel/index.html"
  },
  {
    "breadcrumb": "Créer un jeu vidéo \u003e Tags",
    "content": "",
    "description": "",
    "tags": [],
    "title": "Tag :: Unreal Engine",
    "uri": "/tags/unreal-engine/index.html"
  },
  {
    "breadcrumb": "Créer un jeu vidéo",
    "content": "",
    "description": "",
    "tags": [],
    "title": "Categories",
    "uri": "/categories/index.html"
  }
]
