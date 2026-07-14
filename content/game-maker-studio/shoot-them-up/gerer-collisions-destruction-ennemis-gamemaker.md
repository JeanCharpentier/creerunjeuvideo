---
title: "12. Gérer les collisions et la destruction des ennemis"
weight: 12
prev_url: "/game-maker-studio/shoot-them-up/creer-ennemi-tir-laser-gamemaker-studio/"
next_url: "/game-maker-studio/shoot-them-up/gerer-collisions-defaite-joueur-gamemaker/"
date: 2023-10-27
categories: ['Archive']
tags: ['GameMaker', 'Tutoriel', 'Developpement de jeux', 'Collision', 'Gamedev']
images: ["https://img.youtube.com/vi/THSQh_SlnmY/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/THSQh_SlnmY/maxresdefault.jpg"]
---

Apprenez à implémenter un système de collision efficace pour détruire vos ennemis lors de l'impact de vos projectiles dans GameMaker Studio.

{{< youtube-rgpd "THSQh_SlnmY" >}}

### Résumé des notions clés
*   **Événement de collision :** Utilisation de l'événement `Collision` dans l'objet `laser` pour détecter le contact avec les différents types d'ennemis.
*   **Ciblage précis :** Utilisation de la fonction `with (instance_place(x, y, objet))` pour identifier et cibler spécifiquement l'instance de l'ennemi touchée.
*   **Destruction d'objets :** Emploi de la fonction `instance_destroy()` pour supprimer à la fois l'ennemi touché et le projectile (le laser) après l'impact.
*   **Méthodologie :** Répétition du processus pour chaque type d'ennemi afin de garantir une cohérence dans le gameplay.

### Ce qui reste d'actualité aujourd'hui
Bien que les versions récentes de GameMaker aient évolué, les principes fondamentaux abordés ici restent le socle du développement 2D :
*   **La gestion des collisions :** L'utilisation de `instance_place` reste la méthode recommandée pour vérifier les collisions à des coordonnées précises sans déplacer l'instance actuelle.
*   **La portée du code (`with`) :** La structure `with` est toujours indispensable pour exécuter du code dans le contexte d'une autre instance, ce qui est crucial pour la communication entre objets (ex: le laser qui ordonne à l'ennemi de se détruire).
*   **La propreté du code :** L'importance de détruire les projectiles après impact est une règle d'or pour optimiser la gestion de la mémoire et éviter les fuites de ressources dans vos projets.

{{< footer >}}