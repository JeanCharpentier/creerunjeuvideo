---
title: "21. Implémenter le système de ramassage et de score"
weight: 21
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Blueprints', 'Gameplay', 'GameDev', 'Tutoriel']
images: ["https://img.youtube.com/vi/ThVlNivcwf0/maxresdefault.jpg"]
---

Dans cet épisode, nous passons à l'étape cruciale de l'interaction : transformer notre objet statique en un élément de gameplay fonctionnel. Nous allons apprendre à détecter la collision entre le joueur et la pièce, mettre à jour une variable de score et supprimer l'objet de la scène.

{{< youtube-rgpd "ThVlNivcwf0" >}}

### Résumé des étapes clés
*   **Détection de collision :** Utilisation de l'événement `Event Actor Begin Overlap` dans le Blueprint de la pièce.
*   **Cast vers le personnage :** Utilisation du nœud `Cast To ThirdPersonCharacter` pour s'assurer que seule la collision avec le joueur déclenche l'action.
*   **Gestion du score :** 
    *   Récupération de la valeur actuelle via `Get Score`.
    *   Addition de la valeur (via `Integer + Integer`) pour permettre une flexibilité sur le gain de points.
    *   Mise à jour de la variable via `Set Score`.
*   **Feedback visuel :** Utilisation temporaire de `Print String` pour vérifier le bon fonctionnement du compteur.
*   **Nettoyage :** Utilisation de `Destroy Actor` pour supprimer la pièce de la scène une fois ramassée.
*   **Level Design :** Astuces pour dupliquer et disposer les pièces dans le niveau tout en conservant les propriétés de taille personnalisées.

### Ce qui reste d'actualité aujourd'hui

Bien que cet épisode utilise les bases d'Unreal Engine 4, les concepts abordés sont fondamentaux et toujours valides dans Unreal Engine 5 :

1.  **Le Casting :** Le `Cast To` reste la méthode la plus directe pour communiquer entre deux Blueprints, bien que pour des projets plus complexes, l'utilisation d'**Interfaces** soit recommandée pour éviter les dépendances directes.
2.  **La logique de ramassage :** Le pattern `Overlap -> Cast -> Modify Variable -> Destroy` est le standard de l'industrie pour les objets à collecter (pièces, munitions, items).
3.  **La gestion des variables :** La manipulation des variables d'instance (comme le score stocké dans le Character) est une pratique immuable.
4.  **Workflow de Level Design :** La duplication d'acteurs dans le viewport reste la méthode la plus efficace pour peupler un niveau rapidement tout en conservant les modifications apportées aux instances (comme l'échelle ou les paramètres spécifiques).

{{< footer >}}