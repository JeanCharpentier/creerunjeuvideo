---
title: "8. Créer des Jump Pads configurables"
weight: 8
date: 2026-06-17
categories: ['Développement de jeux']
tags: ['Unreal Engine 4', 'Blueprints', 'Gameplay', 'Tutoriel']
---

Dans ce tutoriel, nous allons apprendre à concevoir un système de **Jump Pad (plateforme de saut)** dynamique et configurable pour Unreal Engine 4. L'objectif est de créer un acteur réutilisable dont vous pourrez ajuster la puissance horizontale, la puissance verticale et l'angle de projection directement depuis l'éditeur de niveau, sans avoir à modifier le code à chaque fois.

{{< youtube-rgpd "Iqh6_nGz1Nc" >}}

### Résumé du processus de création
*   **Configuration de l'acteur :** Création d'un Blueprint de type `Actor` composé d'un Static Mesh (le socle), d'une `Box Collision` (pour détecter le joueur) et d'un composant `Arrow` (pour définir la direction de projection).
*   **Variables éditables :** Création de trois variables (`Angle`, `H Force`, `V Force`) avec l'option *Instance Editable* activée pour permettre une personnalisation par pad dans la scène.
*   **Logique de construction :** Utilisation de l'événement `Construction Script` pour orienter la flèche de direction en fonction de l'angle défini.
*   **Logique de gameplay :** Utilisation de l'événement `OnComponentBeginOverlap` pour détecter le joueur et appliquer la fonction `Launch Character` avec les paramètres configurés.
*   **Overrides :** Activation des options `XY Override` et `Z Override` dans la fonction de lancement pour garantir une trajectoire précise et cohérente.

### Ce qui reste d'actualité aujourd'hui
Bien que cet article traite d'Unreal Engine 4, les concepts fondamentaux restent parfaitement applicables aux versions récentes (UE5) :
*   **Modularité :** L'utilisation de composants `Arrow` pour visualiser des vecteurs de direction dans le viewport est une pratique standard pour le level design.
*   **Instance Editable :** La puissance des Blueprints réside toujours dans cette capacité à exposer des variables pour permettre aux designers de modifier le gameplay sans toucher à la logique interne.
*   **Launch Character :** La fonction `Launch Character` reste l'outil privilégié pour manipuler les déplacements du personnage de manière fluide sans altérer directement sa vélocité de manière "brute".
*   **Construction Script :** C'est toujours l'endroit idéal pour mettre à jour les visuels ou les composants d'un acteur avant même de lancer le jeu (PIE).

{{< footer >}}