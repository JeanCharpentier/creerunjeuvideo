---
title: "Implémenter un Dash Vertical et des effets Niagara dans Unreal Engine 5"
date: 2026-06-17
categories: ['Développement de jeux']
tags: ['Unreal Engine 5', 'Blueprints', 'Niagara', 'GameDev']
images: ["https://img.youtube.com/vi/f59H_Hs3WMM/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/f59H_Hs3WMM/maxresdefault.jpg"]
---

Le "Game Feel" est ce qui sépare un prototype fonctionnel d'une expérience de jeu mémorable. Dans ce tutoriel, nous allons voir comment ajouter un **Dash vertical** (vers le bas) à votre personnage, couplé à un système de particules **Niagara** dynamique pour renforcer l'impact visuel de l'action.

{{< youtube-rgpd "f59H_Hs3WMM" >}}

### Résumé du processus
*   **Logique de mouvement :** Utilisation de `IsMovingOnGround` pour vérifier l'état du joueur et déclencher le dash uniquement en l'air.
*   **Physique :** Application d'une impulsion (`Add Impulse`) sur le `CharacterMovementComponent` avec une valeur négative sur l'axe Z.
*   **Compatibilité :** Encapsulation du système dans une fonction pour supporter à la fois les contrôles clavier et les inputs tactiles (mobile).
*   **Effets visuels :** Création d'un système Niagara utilisant le `Skeletal Mesh` du joueur comme émetteur pour créer une traînée stylisée.
*   **Gestion des états :** Activation/Désactivation automatique du système de particules via les événements `OnLanded` et l'input de saut.

### Ce qui reste d'actualité aujourd'hui
Bien que les versions d'Unreal Engine évoluent, les fondamentaux abordés ici restent des piliers du développement :
1.  **Le Character Movement Component :** C'est toujours la méthode la plus robuste pour gérer les déplacements complexes sans réinventer la physique.
2.  **Niagara :** Le système de particules d'Unreal est devenu le standard industriel. La méthode consistant à utiliser des *User Parameters* pour lier les données du personnage aux particules est une pratique propre qui garantit une optimisation maximale.
3.  **Modularité :** L'utilisation de fonctions pour encapsuler des mécaniques (comme le saut ou le dash) est essentielle pour maintenir un projet propre, surtout lors du passage d'un projet PC vers une plateforme mobile.
4.  **Game Feel :** L'ajout de feedback visuel (particules) lors d'une action physique est une règle d'or du game design qui ne se démodera jamais.

{{< footer >}}