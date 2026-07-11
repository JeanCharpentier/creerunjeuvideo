---
title: "6. Limiter les déplacements de votre vaisseau"
weight: 6
prev_url: "/game-maker-studio/shoot-them-up/debuter-game-maker-integrer-deplacer-vaisseau/"
next_url: "/game-maker-studio/shoot-them-up/maitriser-tir-automatique-gestion-instances-game-maker/"
date: 2023-10-27
categories: ['Archive']
tags: ['Game Maker', 'Tutoriel', 'Developpement de jeux', 'GML', 'Programmation']
images: ["https://img.youtube.com/vi/kJCl2lUzhyk/maxresdefault.jpg"]
---

Apprenez à restreindre les déplacements de votre vaisseau à l'intérieur de votre zone de jeu pour éviter qu'il ne disparaisse hors de l'écran grâce à la fonction clamp.

{{< youtube-rgpd "kJCl2lUzhyk" >}}

### Résumé des notions clés

*   **L'événement Step :** Comprendre que cet événement s'exécute à chaque image (60 fois par seconde selon la vitesse de votre room), ce qui est idéal pour les vérifications constantes de position.
*   **La fonction `clamp()` :** Utilisation de cette fonction intégrée à Game Maker pour contraindre une valeur entre un minimum et un maximum.
*   **Gestion de l'origine du sprite :** Importance de prendre en compte le point d'origine de votre sprite (souvent au centre) pour calculer correctement les limites de collision avec les bords de l'écran.
*   **Calcul des marges :** Ajustement des valeurs de `clamp` en fonction de la taille réelle de votre objet (hauteur/largeur) pour que le vaisseau reste entièrement visible à l'écran.

### Ce qui reste d'actualité aujourd'hui

Bien que les versions de Game Maker aient évolué, les principes fondamentaux abordés ici restent des piliers du développement 2D :

1.  **La logique de boucle de jeu :** L'événement `Step` demeure le cœur battant de toute logique de gameplay dans Game Maker. Maîtriser ce qui doit être calculé à chaque frame est essentiel pour la fluidité.
2.  **L'utilisation de fonctions utilitaires :** La fonction `clamp()` est un outil universel en programmation de jeux. Elle est toujours la méthode la plus propre et la plus performante pour limiter des coordonnées, des barres de vie ou des jauges d'énergie.
3.  **La rigueur mathématique :** Le souci du détail concernant l'origine des sprites et les dimensions des objets est une bonne pratique qui évite les bugs de collision frustrants. Comprendre comment le moteur interprète les coordonnées par rapport au centre de l'objet est une compétence indispensable pour tout développeur.

{{< footer >}}