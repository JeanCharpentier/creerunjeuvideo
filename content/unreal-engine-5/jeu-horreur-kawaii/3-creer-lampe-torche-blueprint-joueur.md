---
title: "3. Création d'une lampe-torche et système d'allumage"
date: 2026-06-12
category: Archive
weight: 3
tags: [Unreal Engine 5, Kawaii Slender, Blueprint, Input System, Audio, Game Design]
prev_url: "/unreal-engine-5/jeu-horreur-kawaii/2-integration-camera-premiere-personne-fps"
next_url: "/unreal-engine-5/jeu-horreur-kawaii/4-gestion-variables-batterie-lampe"
images: ["https://img.youtube.com/vi/AarebiZ0SM8/maxresdefault.jpg"]
---

{{< youtube-rgpd "AarebiZ0SM8" >}}

---

## Résumé des notions clés

Dans ce troisième volet de la série **Kawaii Slender**, nous passons à la vitesse supérieure en configurant l'accessoire indispensable de tout bon jeu d'horreur : la lampe-torche. Ce tutoriel détaille pas à pas l'intégration de la lumière et la logique d'allumage via les Blueprints :

*   **Intégration d'un composant de lumière :**
    *   Ouverture du Blueprint `BP_FirstPersonCharacter` dans l'onglet Hublot (*Viewport*).
    *   Ajout d'un composant de type **Spotlight** (nommé `lampe`), attaché et aligné directement sur la *First Person Camera* pour s'assurer que le faisceau lumineux suive précisément le regard du joueur.
*   **Configuration du système d'Input (UE5 Enhanced Input System) :**
    *   Création d'une nouvelle **Input Action** (`IA_Lampe`) configurée avec un type de valeur booléen (`Digital/Boolean`), idéale pour un comportement de type bouton pressé/relâché.
    *   Ajout d'un déclencheur (*Trigger*) de type **Pressed** pour capter l'instant précis où la touche est enfoncée.
    *   Enregistrement de la liaison dans le fichier de contexte de mapping (`IMC_Default`) en associant l'action `IA_Lampe` à la **touche F** du clavier.
*   **Logique de programmation visuelle (Event Graph) :**
    *   Utilisation du node de débogage **Print String** pour tester et valider l'appel de l'action en cours de jeu.
    *   Implémentation du node **FlipFlop** qui permet d'alterner cycliquement l'exécution du code entre deux sorties (A et B) à chaque pression de touche.
    *   Manipulation de l'intensité via la fonction **Set Intensity** sur le composant de la lampe, faisant basculer la valeur entre sa puissance maximale et $0$ (éteinte).
*   **Optimisation avec les Variables :**
    *   Introduction du concept de **Promote to Variable** pour extraire la valeur brute d'intensité (ex: $5000$) et la stocker dans une variable dédiée nommée `Intensité`.
    *   Cette méthode permet de centraliser le réglage de la puissance de la lampe sans modifier les nodes du script, ouvrant la voie à de futures configurations dans les options du jeu.
    *   Expérimentations secondaires présentées pour modifier d'autres paramètres à la volée, comme la couleur du faisceau (**Set Light Color**).

---

## Ce qui reste d'actualité aujourd'hui

Les mécaniques et les bonnes pratiques introduites dans cette archive restent de parfaits standards sur les versions modernes d'Unreal Engine 5 :

*   **L'attachement de composants à la caméra :** Lier des sources lumineuses ou des caméras secondaires au composant de vision principal reste la méthode la plus rapide et propre pour simuler une vue à la première personne réaliste.
*   **La modularité de l'Enhanced Input System :** La séparation stricte entre l'action logique (`Input Action`) et l'attribution matérielle (`Mapping Context`) est le fondement de la gestion moderne des contrôles multiplateformes.
*   **L'usage des variables de configuration :** Exposer des variables (comme `Intensité`) plutôt que d'écrire des valeurs brutes ("hardcodées") dans l'Event Graph est une règle d'or en gamedev. Cela fluidifie le game design et s'avère indispensable pour lier vos mécaniques à une interface utilisateur (UI).

---
{{< footer >}}