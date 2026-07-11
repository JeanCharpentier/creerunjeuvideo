---
title: "12. Créer un système d''affichage (HUD) et compter les objets"
weight: 12
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Blueprint', 'HUD', 'Widget', 'GameDev', 'Tutoriel']
images: ["https://img.youtube.com/vi/mLqePveJ5C8/maxresdefault.jpg"]
---

Dans cet épisode de notre série sur *Kawaii Slender*, nous abordons une étape cruciale pour tout jeu : l'interface utilisateur (HUD - Heads-Up Display). Apprendre à afficher des informations dynamiques, comme le nombre de cookies ramassés, est la base pour créer des systèmes de score ou des conditions de victoire.

{{< youtube-rgpd "mLqePveJ5C8" >}}

### Résumé du tutoriel
*   **Création des Widgets :** Mise en place de deux *Widget Blueprints* (un HUD principal et un HUD dédié aux cookies) pour séparer les éléments graphiques.
*   **Configuration visuelle :** Utilisation des ancres (*Anchors*) pour fixer le texte en bas à gauche de l'écran, garantissant une position stable quelle que soit la résolution.
*   **Gestion des variables :** Création d'une variable entière `NB_Cookies` dans le *FirstPersonCharacter*, rendue publique (*Editable*) pour être accessible par d'autres Blueprints.
*   **Binding (Liaison) :** Utilisation de la fonction *Bind* sur le texte du Widget pour lier dynamiquement la valeur affichée à la variable du personnage via un *Cast*.
*   **Logique de jeu :** Utilisation du *Event Begin Play* pour afficher les widgets à l'écran et mise à jour de la variable `NB_Cookies` (incrémentation) lors de l'interaction avec l'objet.

### Ce qui reste d'actualité aujourd'hui
Bien que cet épisode utilise Unreal Engine 4, les concepts fondamentaux restent identiques dans Unreal Engine 5 :
*   **Le système UMG (Unreal Motion Graphics) :** La création de widgets via le *Designer* et le *Graph* est restée quasi inchangée.
*   **Le Casting :** Le *Cast to Character* reste une méthode standard pour communiquer entre les objets et le joueur, bien que dans des projets complexes, on privilégie désormais les *Interfaces* ou les *Components* pour éviter les dépendances trop lourdes.
*   **L'importance des Bindings :** La méthode de liaison est toujours fonctionnelle, bien qu'il soit recommandé pour les jeux gourmands de mettre à jour le texte via des événements (Event Dispatchers) plutôt que par un binding qui s'exécute à chaque frame.

{{< footer >}}