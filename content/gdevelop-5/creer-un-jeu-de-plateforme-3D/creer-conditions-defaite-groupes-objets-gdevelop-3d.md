---
title: "6. Créer des conditions de défaite et utiliser les groupes d''objets"
weight: 6
date: 2024-05-22
categories: ['Tutoriels GDevelop']
tags: ['GDevelop 5', '3D', 'GameDev', 'Débutant']
images: ["https://img.youtube.com/vi/fsi1yYoxSYo/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/fsi1yYoxSYo/maxresdefault.jpg"]
---

Dans ce nouvel épisode de notre série dédiée à la création d'un jeu de plateforme 3D sur GDevelop 5, nous allons nous attaquer à un élément crucial de tout jeu : la gestion de la défaite. Comment éviter que le joueur ne tombe à l'infini dans le vide ? Comment faire en sorte qu'il recommence le niveau s'il touche un ennemi ? C'est ce que nous allons voir, tout en découvrant une notion fondamentale pour optimiser votre code : les **groupes d'objets**.

{{< youtube-rgpd "fsi1yYoxSYo" >}}

### Au programme de ce tutoriel :
*   **Création d'une "Killzone"** : Mise en place d'un cube invisible sous le niveau pour détecter les chutes.
*   **Gestion des collisions** : Utilisation de l'action "Changer la scène" pour redémarrer le niveau instantanément.
*   **Optimisation avec les Groupes** : Apprendre à regrouper vos ennemis et pièges pour éviter de dupliquer vos lignes d'événements.
*   **Nettoyage visuel** : Masquer les objets utilitaires (comme la Killzone) au lancement de la scène.

### Ce qui reste d'actualité aujourd'hui
*   **La puissance des Groupes** : Cette notion est indispensable. Que vous ayez 2 ou 200 ennemis, utiliser un groupe vous permet de modifier la logique de défaite une seule fois pour tous les objets concernés.
*   **La structure des événements** : La logique de collision reste identique dans les versions récentes de GDevelop. L'utilisation d'un objet "invisible" pour délimiter les zones de mort est une technique standard et efficace.
*   **Gestion des scènes** : La fonction "Changer la scène" est toujours la méthode la plus directe pour réinitialiser un niveau, bien qu'elle puisse être couplée à des variables globales pour gérer les scores ou les vies dans des projets plus complexes.

{{< footer >}}