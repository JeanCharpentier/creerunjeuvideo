---
title: "8. Intelligence Artificielle (Behavior Tree, Blackboard & Configuration du Slender)"
date: 2026-06-12
category: Archive
weight: 8
tags: [Unreal Engine 5, Kawaii Slender, Blueprint, Input System, Audio, Game Design]
prev_url: "/unreal-engine-5/jeu-horreur-kawaii/7-ramassage-objet-score-points-compteur"
next_url: "/unreal-engine-5/jeu-horreur-kawaii/9-ai-perception-detection-vision-ecoute-suivre"
images: ["https://img.youtube.com/vi/Fu67Z4R3SPM/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/Fu67Z4R3SPM/maxresdefault.jpg"]
---

{{< youtube-rgpd "Fu67Z4R3SPM">}}

Dans ce huitième volet de la série *Kawaii Slender*, nous attaquons un gros morceau du développement sur Unreal Engine 5.6.1 : **l'Intelligence Artificielle (IA)**. C'est ici que notre jeu d'horreur mignon commence à prendre vie avec l'intégration de notre grand antagoniste : une poule de l'enfer géante qui va nous traquer sans relâche.

> **Note de montage :** Ce tutoriel aborde des notions architecturales d'IA assez denses. Pour éviter une vidéo d'une heure indigeste, le contenu a été scindé en deux parties. Dans cette première partie, nous préparons toute la structure logique (Behavior Tree, Blackboard, Tâches). Le comportement visuel concret et la traque seront pleinement effectifs à la fin de la seconde partie.

---

## 1. Création et configuration du personnage (BP_Slender)

Pour commencer, nous allons créer l'entité physique de notre ennemi. 

1. Dans le **Content Drawer**, créez un dossier `Slender` dans le répertoire des Blueprints.
2. Faites un clic droit -> **Blueprint Class** et choisissez la classe **Character**. *Pourquoi un Character ?* Parce qu'il s'agit d'un acteur doté d'un composant de déplacement natif (`Character Movement`), idéal pour être piloté par une IA. Nommez-le `BP_Slender`.
3. Ouvrez le Blueprint et sélectionnez le composant **Mesh**. Dans les détails, attribuez-lui le Skeletal Mesh `SKM_Chicken_001`.
4. **Ajustement de l'orientation et de la taille :**
   * Faites pivoter le mesh de **-90 degrés** sur l'axe Z pour qu'il pointe dans la direction de la flèche de l'acteur (le sens avant).
   * Pour en faire une menace digne de ce nom, activez le verrouillage des proportions dans **Scale** (Échelle) et appliquez un multiplicateur de **4.0**.
   * Ajustez sa hauteur dans la vue orthogonale (gauche ou droite) pour caler ses pattes au bas de la capsule de collision.

---

## 2. L'Architecture de l'IA : Arbre de comportement et Tableau noir

Pour créer une IA propre et facile à maintenir, Unreal Engine utilise un écosystème dédié distinct des Blueprints classiques. C'est une structure verticale beaucoup plus lisible qu'une suite de branches imbriquées.

* **Le Blackboard (Tableau noir) :** C'est le cerveau de stockage. Il ne contient aucune logique, il sert uniquement à mémoriser des variables (clés) que l'IA va interroger ou modifier.
* **Le Behavior Tree (Arbre de comportement) :** C'est le chef d'orchestre. Il structure l'ordre des actions à exécuter à la verticale, de gauche à droite, selon les données fournies par le Blackboard.

### Création des assets
Dans votre dossier `Slender`, faites un clic droit -> **Artificial Intelligence** :
1. Créez un **Behavior Tree** nommé `BT_Slender`.
2. Créez un **Blackboard** nommé `BB_Slender`.
3. Ouvrez `BT_Slender` et, dans le panneau *Details*, vérifiez que la ligne **Blackboard Asset** cible bien votre `BB_Slender`.

---

## 3. Structure du Behavior Tree

À partir du nœud **Root** (le point de départ de l'IA), nous allons tirer un câble pour créer un **Selector**. Le sélecteur agit comme un embranchement : il va lire ses enfants de gauche à droite et exécuter le premier bloc dont les conditions sont validées.

Sous ce Selector, nous créons deux **Sequences** :
1. La première séquence (à gauche) sera renommée `Recherche`.
2. La deuxième séquence (à droite) sera renommée `Poursuite`.

---

## 4. Programmation des tâches (Tasks)

Les séquences ont besoin d'actions concrètes. Nous allons programmer deux tâches personnalisées (BTT) : l'une pour la déambulation aléatoire et l'autre pour la traque du joueur.

### Tâche 1 : La Recherche Aléatoire (`BTT_Recherche`)
Cliquez sur **New Task** en haut du Behavior Tree et enregistrez-la sous le nom `BTT_Recherche` dans un sous-dossier `Tâches`.

Dans le graphe de la tâche :
1. overridez (substituez) la fonction **Receive Execute AI**. Cet événement s'active dès que l'arbre appelle la tâche.
2. Ajoutez un nœud **AI Move To**.
3. Reliez le paramètre **Controlled Pawn** directement à l'entrée **Pawn** de l'AI Move To (c'est notre poule).
4. Pour définir une destination aléatoire, tirez le *Controlled Pawn*, créez un **Get Actor Location**, puis reliez-le à un **Get Random Reachable Point In Radius**. Configurez un rayon (*Radius*) de `1000` unités.
5. Connectez le *Random Location* à la *Destination* de l'AI Move To.
6. **Crucial :** Sur la broche *On Success* du Move To, ajoutez le nœud **Finish Execute** et cochez la case **Success**. Sans ce nœud, l'arbre de comportement ne saurait jamais que la tâche est finie et resterait bloqué indéfiniment.
7. Ajustez l'**Acceptance Radius** à `100` pour donner une marge d'un mètre à l'IA pour valider son arrivée.

### Tâche 2 : La Poursuite (`BTT_Poursuite`)
Créez une seconde tâche nommée `BTT_Poursuite`. La logique est similaire mais plus directe :

1. Implémentez **Receive Execute AI** et préparez immédiatement le **Finish Execute** (avec *Success* coché) en sortie.
2. Ajoutez le nœud **AI Move To** lié au *Controlled Pawn*.
3. Au lieu d'un vecteur de destination, faites un clic droit et cherchez **Get Player Character**. Reliez-le directement à la broche **Target Actor** de l'AI Move To. Unreal convertira automatiquement l'entité en coordonnées dynamiques pour la suivre.
4. Configurez également l'**Acceptance Radius** à `100`.

---

## 5. Intégration et Décorateurs (Conditionnels)

Retournez sur `BT_Slender` pour assembler nos briques logiques :
* Sous la séquence `Recherche`, appelez votre tâche `BTT_Recherche`. À sa suite, ajoutez un nœud natif **Wait** configuré à `3.0` secondes avec une *Random Deviation* de `1.0`. Cela permet à l'IA de faire des pauses naturelles de durée variable (entre 2 et 4 secondes) entre ses déplacements.
* Sous la séquence `Poursuite`, appelez votre tâche `BTT_Poursuite`.

### L'aiguillage par le Blackboard
Pour l'instant, le Selector lira toujours la Recherche en premier et n'ira jamais à droite. Il faut lui donner une condition de switch via les **Decorators**.

1. Allez dans l'onglet **Blackboard** (en haut à droite) et ajoutez une clé de type **Boolean** que vous nommerez `VoitJoueur`.
2. De retour sur le Behavior Tree, faites un clic droit sur la séquence `Recherche` -> **Add Decorator** -> **Blackboard**. Faites de même pour `Poursuite`.
3. Sélectionnez le décorateur de la **Poursuite** :
   * Dans les détails, sous *Observer Aborts*, choisissez **Self** (pour interrompre l'exécution interne si la condition change).
   * Sous *Blackboard Key*, sélectionnez `VoitJoueur`.
   * Laissez la condition sur **Is Set** (Vrai).
4. Sélectionnez le décorateur de la **Recherche** :
   * Mettez également l'*Observer Aborts* sur **Self**.
   * Sélectionnez la clé `VoitJoueur`.
   * Changez le paramètre clé pour **Is Not Set** (Faux).

La structure de base de notre intelligence artificielle est désormais prête. L'IA sait que si `VoitJoueur` est faux, elle doit errer sur la carte, et si la variable devient vraie, elle doit basculer instantanément sur la tâche de poursuite. Dans le prochain épisode, nous verrons comment configurer les composants de perception sensorielle de notre Slender pour alimenter ce Blackboard de manière dynamique !

{{< footer >}}