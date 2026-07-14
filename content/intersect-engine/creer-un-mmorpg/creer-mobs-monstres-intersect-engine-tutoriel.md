---
title: "12. Créer des Mobs et peupler votre monde"
weight: 12
prev_url: "/intersect-engine/creer-un-mmorpg/creer-equiper-objets-depart-intersect-engine/"
next_url: "/intersect-engine/creer-un-mmorpg/creer-boutique-marchand-intersect-engine/"
date: 2023-10-27
categories: ['Archive']
tags: ['Intersect Engine', 'MMORPG', 'Game Development', 'Tutoriel']
images: ["https://img.youtube.com/vi/I3fjIxLcB3I/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/I3fjIxLcB3I/maxresdefault.jpg"]
---

Donner vie à votre MMORPG nécessite bien plus que de simples décors : il faut des créatures pour peupler vos zones et offrir des défis à vos joueurs. Dans ce guide, nous explorons comment configurer vos premiers "Mobs" (monstres) avec Intersect Engine.

{{< youtube-rgpd "I3fjIxLcB3I" >}}

### Notions clés pour la création de Mobs
La création de personnages non-joueurs (PNJ) hostiles repose sur plusieurs paramètres essentiels dans l'éditeur d'Intersect :

*   **Comportement (Behavior) :**
    *   *Attack on Sight :* Le monstre attaque dès qu'il détecte le joueur dans son champ de vision (*Sight Range*).
    *   *Attack when Attacked :* Le monstre reste passif tant que le joueur ne porte pas le premier coup. Idéal pour les zones de départ afin de ne pas frustrer les nouveaux joueurs.
*   **Gestion du Loot :** Vous pouvez configurer jusqu'à 10 types d'objets différents par monstre, avec une probabilité de drop personnalisable (ex: 50% de chance d'obtenir 5 pièces d'or).
*   **Équilibrage des Stats :** Il est crucial de comparer les statistiques de vos monstres avec celles de vos classes de départ (PV, Force, Armure) pour garantir que le jeu reste accessible.
*   **Spawn et Respawn :** Le *Spawn Duration* définit le temps nécessaire avant qu'un monstre ne réapparaisse après sa mort.
*   **Intégration sur la carte :** Utilisez l'onglet *Attributes* pour placer les points de spawn et définir des zones d'exclusion (*NPC Avoid*) si nécessaire.

### Ce qui reste d'actualité aujourd'hui
Bien que les versions d'Intersect Engine évoluent, la logique fondamentale présentée ici demeure le standard pour le développement de RPG 2D :

1.  **La hiérarchie des PNJ :** La distinction entre Mobs (ennemis), Gardes (protecteurs) et PNJ amicaux (marchands/donneurs de quêtes) est toujours la base de la structure narrative d'un MMO.
2.  **L'importance de l'équilibrage :** La méthode consistant à utiliser le *Class Editor* comme référence pour créer ses monstres reste la meilleure pratique pour éviter de créer des ennemis impossibles à vaincre ou trop faibles.
3.  **Le caractère aléatoire (RNG) :** Comprendre que le taux de drop est une probabilité indépendante à chaque mort du monstre est essentiel pour la gestion de l'économie de votre jeu.
4.  **Le dynamisme du monde :** L'utilisation de directions de spawn aléatoires pour les monstres est une astuce simple mais efficace pour rendre les zones de jeu moins répétitives et plus "vivantes".

{{< footer >}}