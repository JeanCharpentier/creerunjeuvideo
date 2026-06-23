---
title: "18. Maîtriser les variables et le système de score dans Unreal Engine 4"
weight: 18
date: 2026-06-17
categories: ['Tutoriels Unreal Engine']
tags: ['Unreal Engine 4', 'Blueprints', 'Variables', 'GameDev']
---

Dans ce chapitre, nous abordons un pilier fondamental du développement de jeux vidéo : la gestion des données. Qu'il s'agisse de points de vie, d'inventaire ou de score, tout repose sur l'utilisation des variables. Nous allons voir comment créer, configurer et rendre accessible une variable de type "Integer" au sein de votre personnage dans Unreal Engine 4.

{{< youtube-rgpd "Oq3zs0DTRDY" >}}

### Résumé du chapitre
*   **Qu'est-ce qu'une variable ?** Une boîte de stockage pour vos données (texte, nombres, états logiques).
*   **Les types de variables :** Distinction entre les *Integers* (nombres entiers) pour les scores et les *Floats* (nombres à virgule) pour les mesures précises.
*   **Création dans le Blueprint :** Utilisation du panneau "Variables" dans le `ThirdPersonCharacter`.
*   **Compilation :** Étape indispensable pour initialiser la variable et définir sa valeur par défaut.
*   **Accessibilité :** L'importance de l'icône "œil" (Editable) pour permettre aux autres acteurs du jeu de modifier votre score.

### Ce qui reste d'actualité aujourd'hui
Bien que les versions d'Unreal Engine aient évolué (passant de la 4 à la 5), les concepts fondamentaux présentés ici restent strictement identiques :
*   **La logique des types :** La distinction entre `Integer`, `Float`, `Boolean` et `String` est universelle en programmation et au sein de l'Unreal Engine.
*   **Le workflow Blueprint :** La création de variables via le panneau "My Blueprint" et la nécessité de compiler pour appliquer les changements sont toujours les bases du développement visuel.
*   **L'encapsulation :** Le concept de rendre une variable "Editable" (ou "Public" dans d'autres contextes) pour permettre une communication entre différents Blueprints reste la méthode standard pour gérer les interactions entre objets (ex: un objet à ramasser qui modifie le score du joueur).
*   **La structure de données :** Stocker le score sur le `Character` est une pratique courante pour les jeux simples, bien que pour des projets plus complexes, on puisse s'orienter vers des `GameInstance` ou des `PlayerState` pour une meilleure persistance.

{{< footer >}}