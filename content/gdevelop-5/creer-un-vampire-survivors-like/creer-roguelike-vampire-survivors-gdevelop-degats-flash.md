---
title: "3. Créer un Roguelike type Vampire Survivors : Gestion des dégâts et effets visuels"
weight: 3
date: 2023-10-27
categories: ['Tutoriels']
tags: ['GDevelop', 'Roguelike', 'GameDev', 'Tutoriel']
---

Bienvenue dans ce troisième volet de notre série dédiée à la création d'un jeu de type "Vampire Survivors" avec GDevelop 5. Après avoir mis en place les déplacements et les tirs, il est temps de donner un peu de répondant à nos ennemis. Dans cet épisode, nous allons apprendre à gérer les points de vie (HP), les dégâts des projectiles et surtout, à ajouter un feedback visuel indispensable : l'effet de "flash" blanc lors des impacts.

{{< youtube-rgpd "yZKXngC74og" >}}

### Au programme de cet épisode :
*   **Système de points de vie (HP) :** Utilisation des variables d'objet pour permettre une personnalisation individuelle des ennemis.
*   **Gestion des dégâts :** Création d'une variable de dégâts sur les projectiles pour une évolutivité future (système de montée en niveau, bonus, etc.).
*   **Feedback visuel :** Utilisation de l'effet "Ajustement TSL" pour créer un flash blanc lors des collisions.
*   **Logique de collision :** Optimisation des événements pour gérer la suppression des ennemis et des projectiles tout en évitant les bugs de calcul.
*   **Chronomètres :** Utilisation des timers pour gérer la durée de l'effet de flash de manière fluide.

### Ce qui reste d'actualité aujourd'hui
*   **Variables d'objet vs Groupes :** Il est toujours préférable de définir les variables (HP, dégâts) directement sur les objets pour éviter que tous les ennemis d'un même groupe ne partagent les mêmes statistiques.
*   **L'ordre des actions :** La règle d'or reste de soustraire les dégâts avant de supprimer le projectile, sous peine de perdre la valeur de la variable au moment du calcul.
*   **Gestion des nombres flottants :** Utilisez toujours des conditions de type "supérieur ou égal" ou "inférieur ou égal" plutôt qu'une égalité stricte (`==`), car le moteur de jeu peut sauter une valeur précise lors d'un calcul rapide.
*   **Optimisation :** N'oubliez jamais de supprimer les chronomètres inutilisés pour éviter une surcharge mémoire, surtout dans un jeu où le nombre d'entités à l'écran peut exploser.

{{< footer >}}