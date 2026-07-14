---
title: "2. Création dynamique d''ennemis sur PICO-8"
weight: 2
date: 2023-10-27
categories: ['GameDev']
tags: ['pico-8', 'lua', 'tutoriel', 'programmation']
images: ["https://img.youtube.com/vi/eEjfqfYCkqE/maxresdefault.jpg"]
---

Dans ce deuxième épisode de notre série dédiée à la création d'un *Space Invaders* sur PICO-8, nous passons à la vitesse supérieure. Fini le placement manuel des ennemis ligne par ligne : nous allons apprendre à structurer notre code pour qu'il soit évolutif et professionnel.

{{< youtube-rgpd "eEjfqfYCkqE" >}}

### Résumé de l'épisode
*   **Abandon du code répétitif :** On supprime les lignes de code redondantes pour adopter une approche basée sur les données.
*   **Utilisation des tableaux (Tables) :** Introduction à la structure de données centrale en Lua pour stocker nos ennemis.
*   **Boucles `for` :** Automatisation de la création des ennemis pour rendre le jeu redimensionnable (passer de 4 à 40 ennemis en une ligne).
*   **Notions de POO simplifiée :** Création d'objets "ennemi" contenant leurs propres coordonnées (X, Y) et propriétés.
*   **Le Modulo (%) :** Utilisation de l'opérateur modulo pour gérer intelligemment le passage à la ligne des ennemis sur l'écran.
*   **Débogage :** Affichage dynamique du nombre d'ennemis présents dans notre tableau via la fonction `print`.

### Ce qui reste d'actualité aujourd'hui
*   **La puissance des tables :** En PICO-8, tout repose sur les tables. Maîtriser leur manipulation est indispensable pour gérer des projectiles, des particules ou des vagues d'ennemis.
*   **L'importance du `draw` épuré :** Une fois la boucle d'affichage (`for e in all(ennemis)`) mise en place, vous n'avez plus besoin de toucher à la fonction `_draw()`, quel que soit le nombre d'ennemis. C'est la clé d'un code propre.
*   **Le Modulo comme outil de mise en page :** Que ce soit pour créer une grille d'ennemis, un inventaire ou un menu, le modulo reste l'outil le plus efficace pour calculer des positions relatives sans multiplier les variables inutiles.
*   **La modularité :** En séparant la logique de création (dans `_init`) de la logique d'affichage (dans `_draw`), vous préparez votre projet à devenir un vrai jeu complet plutôt qu'un simple script de test.

{{< footer >}}