---
title: "10. Créer un système de détection d''objets avec Line Trace"
weight: 10
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Blueprint', 'LineTrace', 'Interaction', 'GameDev']
---

Dans ce 10ème tutoriel dédié à Unreal Engine 4, nous allons aborder une mécanique fondamentale pour tout jeu d'aventure ou de plateforme : **l'interaction avec les objets**. L'objectif est simple : permettre au joueur de "viser" des cookies dans le niveau et de les faire réagir (ici, en allumant une lumière) lorsqu'ils sont dans le champ de vision.

{{< youtube-rgpd "4lvUReuQHuY" >}}

### Au programme de ce tutoriel :
*   **Création d'un Blueprint dédié** : Transformer un simple *Static Mesh* en un acteur interactif (`BP_Cookie`).
*   **Gestion des composants** : Ajouter une `Point Light` dynamique pour visualiser l'état de l'objet.
*   **Programmation par événements** : Utiliser des *Custom Events* pour contrôler l'intensité lumineuse.
*   **Le Raycasting (Line Trace)** : Implémenter un `LineTraceByChannel` dans le *FirstPersonCharacter* pour détecter les objets situés devant la caméra.
*   **Le Casting** : Utiliser le `Cast to BP_Cookie` pour filtrer les interactions et ne cibler que les objets souhaités.

### Ce qui reste d'actualité aujourd'hui
Bien que ce tutoriel utilise les bases d'Unreal Engine 4, les concepts abordés sont toujours au cœur du développement sur **Unreal Engine 5** :
*   **Le Line Trace** : C'est la méthode standard pour gérer les interactions "point-and-click" ou les systèmes de tir.
*   **La modularité des Blueprints** : Créer des acteurs spécifiques (comme le cookie) plutôt que de coder dans le personnage est une bonne pratique pour garder un projet propre.
*   **Le Casting** : Indispensable pour communiquer entre différents types d'objets dans votre monde.
*   **Débogage visuel** : L'utilisation du `Draw Debug Type` (réglé sur *For One Frame*) reste l'outil numéro 1 pour vérifier si vos rayons de détection sont correctement orientés.

{{< footer >}}