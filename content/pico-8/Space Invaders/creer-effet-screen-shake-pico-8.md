---
title: "21. Créer un effet de ''Screen Shake'' sur PICO-8"
weight: 21
date: 2024-05-22
categories: ['GameDev']
tags: ['pico-8', 'tutoriel', 'gamedev', 'lua']
images: ["https://img.youtube.com/vi/FWAUdglV_mc/maxresdefault.jpg"]
---

Dans ce dernier volet de notre série consacrée à la création d'un *space shooter* sur PICO-8, nous allons ajouter une touche de "Game Feel" indispensable : le **Screen Shake** (ou tremblement d'écran). Cet effet visuel, très prisé dans le style rétro, permet de donner de l'impact et de la profondeur à vos événements de jeu, comme la destruction d'un ennemi ou un dégât reçu.

{{< youtube-rgpd "FWAUdglV_mc" >}}

### Résumé de l'implémentation
Pour réaliser cet effet, nous avons structuré notre code autour de quelques concepts clés :

*   **L'objet `shake`** : Une structure contenant les coordonnées (`x`, `y`), le `timer` (durée de l'effet) et l'intensité du tremblement.
*   **La fonction `screen_shake(duree)`** : Elle initialise le `timer` pour déclencher la vibration.
*   **La fonction `cam_pose()`** : Le cœur du système. Elle génère des décalages aléatoires (entre -1 et 1 multipliés par l'intensité) tant que le `timer` est actif, puis réinitialise la caméra à `(0,0)` une fois le temps écoulé.
*   **Intégration dans la boucle principale** : Appel de `cam_pose()` dans la fonction `_draw()` juste après le nettoyage de l'écran (`cls()`) pour appliquer le décalage à tout le rendu.
*   **Utilisation de `camera(x, y)`** : La fonction native de PICO-8 qui déplace la vue globale du jeu.

### Ce qui reste d'actualité aujourd'hui
*   **Le Game Feel est roi** : Même dans des projets minimalistes, le feedback visuel (shake, particules, flash) est ce qui transforme un prototype technique en une expérience de jeu gratifiante.
*   **La gestion des états** : L'utilisation d'un `timer` pour gérer des effets temporaires est une pratique standard en développement de jeux, facile à adapter pour d'autres effets (invincibilité, ralentissement, etc.).
*   **Modularité** : En passant l'intensité en paramètre, vous pouvez facilement différencier un petit tremblement pour un tir classique d'un gros séisme lors d'une explosion de boss.

{{< footer >}}