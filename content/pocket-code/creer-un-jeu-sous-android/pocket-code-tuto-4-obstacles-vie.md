---
titre: "4. Gestion des obstacles et système de vie"
date: 2026-06-17
categories: ['Tutoriels']
tags: ['Pocket Code', 'GameDev', 'Mobile', 'Programmation']
images: ["https://img.youtube.com/vi/VQLdOn4PKII/maxresdefault.jpg"]
---

Dans ce quatrième volet de notre série sur Pocket Code, nous passons aux choses sérieuses : la création d'obstacles dynamiques et la gestion de la difficulté. Nous allons apprendre à faire défiler nos boîtes, à les faire réapparaître aléatoirement et à implémenter un système de collision pour gérer les points de vie de notre oiseau.

{{< youtube-rgpd "VQLdOn4PKII" >}}

### Résumé des étapes clés
*   **Déplacement horizontal :** Utilisation d'une boucle `forever` pour modifier la position X de l'objet "boîte" à chaque itération.
*   **Réapparition aléatoire :** Utilisation de la fonction `random` pour positionner les boîtes hors écran à droite et varier leur hauteur (Y).
*   **Gestion des limites :** Mise en place d'une condition `if` pour détecter quand une boîte sort de l'écran à gauche et la replacer à droite.
*   **Détection de collision :** Création d'une logique complexe comparant les coordonnées X et Y de l'oiseau avec celles des boîtes.
*   **Système de vie :** Utilisation de variables et de messages (`broadcast`) pour compter les impacts et déclencher un écran "Game Over" après trois collisions.
*   **Optimisation :** Copie des objets pour multiplier les obstacles et rendre le jeu plus dynamique.

### Ce qui reste d'actualité aujourd'hui
Bien que les interfaces de Pocket Code évoluent, les concepts fondamentaux abordés ici restent le socle de tout développement de jeu mobile :
1.  **La logique de boucle de jeu :** Le principe du `forever` pour mettre à jour les positions est universel, que vous soyez sur Pocket Code, Unity ou Godot.
2.  **La gestion des collisions AABB :** La méthode utilisée ici (vérifier si les coordonnées d'un objet sont dans la zone d'un autre) est la base de la détection de collision "Axis-Aligned Bounding Box".
3.  **La communication par messages :** Le système de `broadcast` est une excellente manière de découpler vos scripts pour éviter un code spaghetti, une pratique essentielle en programmation orientée objet.
4.  **L'importance du "Game Feel" :** Ajuster les valeurs de vitesse et de probabilité (random) est ce qui transforme un simple prototype en un jeu réellement amusant.

{{< footer >}}