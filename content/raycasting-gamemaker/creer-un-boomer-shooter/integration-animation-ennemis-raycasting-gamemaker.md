---
title: "5. Intégration et animation des ennemis"
weight: 5
date: 2026-06-17
categories: ['Raycasting GameMaker']
tags: ['GameMaker', 'Raycasting', 'Tutoriel', 'GameDev', 'Sprites']
images: ["https://img.youtube.com/vi/rXK4CByW8mE/maxresdefault.jpg"]
---

Dans ce cinquième épisode de notre série dédiée au Raycasting sur GameMaker, nous passons à l'étape cruciale de l'immersion : l'intégration de vos propres ennemis. Après avoir travaillé sur les armes et les textures de murs, il est temps de donner vie à vos couloirs sombres en remplaçant les modèles par défaut par vos propres créations.

{{< youtube-rgpd "rXK4CByW8mE" >}}

### Au programme de cet épisode :
*   **Gestion des animations :** Comprendre la structure requise par le moteur (4 images pour la marche, 2 pour l'attaque, 5 pour la mort).
*   **Préparation graphique :** Utilisation de paint.net pour le détourage (fond noir obligatoire pour la transparence).
*   **Astuces d'animation :** Créer des variations de taille pour simuler le mouvement sans avoir une tonne d'assets.
*   **Configuration technique :** Réglage des statistiques (vitesse, endurance/PV, dégâts) dans le menu *Ennemy Setup*.
*   **Intégration :** Importation des sprites dans le panneau *Ennemy Animation* et tests en jeu.

### Ce qui reste d'actualité aujourd'hui
Bien que les outils de développement aient évolué, les principes fondamentaux du Raycasting présentés ici restent une excellente base pour comprendre le fonctionnement des moteurs 2.5D :
*   **La gestion des sprites 2D dans un environnement 3D :** La technique du "billboarding" (le sprite qui fait toujours face à la caméra) est toujours utilisée dans de nombreux jeux rétro-FPS modernes.
*   **L'optimisation des assets :** La méthode consistant à réutiliser des frames ou à jouer sur l'échelle pour créer des animations fluides avec peu d'images est une technique d'optimisation classique.
*   **La structure de données :** La séparation entre l'animation (visuel) et le setup (logique/statistiques) est une bonne pratique de Game Design qui facilite l'équilibrage de votre jeu.
*   **La transparence :** Le principe du détourage sur fond uni (souvent noir ou magenta) pour gérer le canal alpha reste une méthode simple et efficace pour les projets de petite envergure.

{{< footer >}}