---
title: "22. Afficher le score du joueur dans l'interface (HUD)"
weight: 22
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Blueprints', 'HUD', 'UI', 'Widget', 'GameDev']
images: ["https://img.youtube.com/vi/9-YZJwPYrrU/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/9-YZJwPYrrU/maxresdefault.jpg"]
---

Dans cet épisode, nous finalisons l'interface utilisateur de notre jeu en rendant le score dynamique. Jusqu'ici, bien que la logique de collecte des pièces fonctionne en arrière-plan, le joueur ne reçoit aucun retour visuel. Nous allons apprendre à utiliser les "Bindings" dans les Widget Blueprints pour lier la valeur de notre variable `Score` à un élément textuel de notre interface.

{{< youtube-rgpd "9-YZJwPYrrU" >}}

### Résumé de la mise en place
*   **Accès au Widget :** Ouverture du `HUD_Score` dans le dossier HUD.
*   **Création du Binding :** Utilisation du bouton "Bind" dans les détails du composant texte pour générer une fonction de mise à jour automatique.
*   **Logique de récupération :**
    *   Utilisation d'un `Cast To ThirdPersonCharacter` pour accéder aux données du joueur.
    *   Utilisation de `Get Player Character` pour définir l'objet source du cast.
    *   Récupération de la variable `Score` via un `Get`.
*   **Conversion automatique :** Unreal Engine gère nativement la conversion de l'entier (Integer) vers le format texte (Text) lors de la connexion au nœud `Return Value`.
*   **Test et itération :** Vérification en jeu de la mise à jour du score lors de la collecte et ajustement du level design pour encourager l'exploration.

### Ce qui reste d'actualité aujourd'hui
Bien que les versions récentes d'Unreal Engine (UE5) aient introduit des systèmes comme les *Common UI* ou les *Data Bindings* plus avancés, la méthode présentée ici reste un pilier fondamental pour les débutants :

1.  **Le Binding simple :** C'est la méthode la plus rapide pour prototyper une interface. Elle est toujours parfaitement fonctionnelle pour des projets simples ou des besoins ponctuels.
2.  **La communication entre classes :** Le principe du `Cast` reste une notion incontournable pour faire dialoguer le HUD avec le Character, même si, pour des projets plus complexes, on privilégiera désormais les *Event Dispatchers* ou les *Interface* pour éviter les dépendances directes.
3.  **Le cycle de vie des Widgets :** Comprendre que le HUD interroge régulièrement les variables du joueur est essentiel pour optimiser les performances (attention toutefois à ne pas surcharger les bindings trop complexes dans des jeux gourmands).

{{< footer >}}