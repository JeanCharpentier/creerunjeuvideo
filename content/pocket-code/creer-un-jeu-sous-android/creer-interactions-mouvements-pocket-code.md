---
title: "3. Créer des interactions et des mouvements dans Pocket Code"
weight: 3
date: 2026-06-17
categories: ['Développement Mobile']
tags: ['Pocket Code', 'Tutoriel', 'GameDev', 'Android', 'Débutant']
images: ["https://img.youtube.com/vi/l4tm1SJmSLQ/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/l4tm1SJmSLQ/maxresdefault.jpg"]
---

Bienvenue dans ce troisième volet de notre série dédiée à **Pocket Code** sur Android. Après avoir mis en place nos objets lors du premier épisode, il est temps de leur donner vie. Dans ce tutoriel, nous allons plonger dans la logique de programmation visuelle pour gérer la gravité, les sauts et les variables globales.

{{< youtube-rgpd "l4tm1SJmSLQ" >}}

### Ce que vous allez apprendre dans cet épisode :

*   **Initialisation des variables :** Créer des variables globales (vie, position X, position Y) pour que vos objets puissent communiquer entre eux.
*   **Gestion de la gravité :** Utiliser une boucle `Forever` pour simuler une chute constante de votre personnage.
*   **Système de saut :** Apprendre à utiliser les `Broadcast` (messages) pour déclencher une action de saut lorsque l'utilisateur touche l'écran.
*   **Contraintes d'écran :** Utiliser `If On Edge, Bounce` pour éviter que votre oiseau ne sorte de la zone de jeu.
*   **Interaction utilisateur :** Configurer l'événement `When Tapped` pour rendre votre jeu réactif.

### Ce qui reste d'actualité aujourd'hui

Bien que l'interface de Pocket Code ait pu évoluer visuellement depuis la sortie de cette vidéo, les concepts fondamentaux expliqués ici restent le socle de tout développement sur l'application :

1.  **La logique des variables :** Le concept de variables globales (accessibles par tous les objets) est toujours indispensable pour gérer le score, la santé ou les positions synchronisées.
2.  **La puissance du Broadcast :** Le système de messages reste la méthode la plus propre pour faire communiquer des objets indépendants sans créer de dépendances complexes.
3.  **La boucle de jeu (Game Loop) :** La structure `Forever` combinée à des modifications de coordonnées (X/Y) est toujours la base pour créer des mouvements fluides dans un moteur 2D.
4.  **Adaptabilité des résolutions :** Le conseil sur l'adaptation des valeurs numériques (pixels) en fonction de la résolution de votre appareil est une règle d'or en GameDev mobile. N'oubliez jamais de tester vos jeux sur différents formats d'écran !

{{< footer >}}