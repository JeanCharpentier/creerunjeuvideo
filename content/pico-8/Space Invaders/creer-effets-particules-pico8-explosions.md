---
title: "18. Créer des effets de particules pour vos explosions"
weight: 18
date: 2024-05-22
categories: ['PICO-8']
tags: ['gamedev', 'tutoriel', 'particules', 'lua']
images: ["https://img.youtube.com/vi/QtjNAaPgYT4/maxresdefault.jpg"]
---

Dans ce 18ème épisode de notre série sur la création d'un *Space Invaders* sur PICO-8, nous passons à l'étape supérieure : le "juice" (le dynamisme visuel). Fini les ennemis qui disparaissent simplement, nous allons ajouter des explosions dynamiques pour rendre le jeu plus vivant.

{{< youtube-rgpd "QtjNAaPgYT4" >}}

### Résumé de la mise en place
Pour implémenter ce système de particules, nous avons suivi ces étapes clés :

*   **Gestion des données :** Création d'un tableau `parts` pour stocker chaque particule individuellement.
*   **Fonction `explosion(origin)` :** 
    *   Utilisation d'une boucle `for` avec un nombre aléatoire de particules (entre 10 et 20).
    *   Initialisation des propriétés : position (centrée sur l'ennemi avec `+4`), vitesse aléatoire en X et Y, et durée de vie.
*   **Mise à jour (`update`) :** 
    *   Réduction de la durée de vie à chaque frame.
    *   Application de la vélocité à la position.
    *   Suppression automatique de la particule du tableau (`del`) une fois sa vie épuisée.
*   **Rendu (`draw`) :** Utilisation de `rectfill` pour dessiner des petits carrés de 1x1 pixel, avec une gestion dynamique des couleurs pour simuler une transition (ex: orange vers rouge).

### Ce qui reste d'actualité aujourd'hui
*   **La modularité :** Bien que nous ayons créé ce système pour des explosions, la structure est réutilisable pour n'importe quel effet (fumée, traînées de réacteur, bonus). Il suffit de changer les paramètres de couleur ou de vélocité.
*   **L'optimisation :** La gestion par tableau et la suppression via `del()` restent la méthode standard et efficace sur PICO-8 pour gérer un nombre modéré d'objets à l'écran.
*   **Le "Juice" :** Ajouter des effets visuels, même simples, est ce qui différencie un prototype technique d'un jeu fini et agréable à jouer. N'hésitez pas à jouer sur les couleurs (palette PICO-8) pour donner une identité visuelle unique à vos effets.

{{< footer >}}