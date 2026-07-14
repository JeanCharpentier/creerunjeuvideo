---
title: "13. Création de projectiles et passage à Unreal Engine 4.27"
weight: 13
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['FPS', 'Blueprint', 'GameDev', 'Tutoriel']
images: ["https://img.youtube.com/vi/NRpVW7ePYPg/maxresdefault.jpg"]
---

Dans cet épisode, nous franchissons une étape technique importante en mettant à jour notre projet vers la version 4.27.2 d'Unreal Engine 4. Une fois cette transition effectuée en toute sécurité, nous passons au cœur du sujet : l'implémentation du système de tir pour notre arme, incluant la création de projectiles dynamiques et la gestion des inputs.

{{< youtube-rgpd "NRpVW7ePYPg" >}}

### Résumé de l'épisode
*   **Migration de version :** Procédure pour passer de l'UE 4.26 à 4.27.2 en toute sécurité (sauvegarde, clonage, et utilisation de l'option "Switch Unreal Engine Version").
*   **Architecture des projectiles :** Création d'une classe parente `BPM_Projectile_Base` pour gérer les comportements communs (vitesse, gravité, durée de vie).
*   **Gestion des composants :** Utilisation du composant `ProjectileMovement` pour définir la physique des tirs.
*   **Système de tir :** Mise en place d'un `Custom Event` pour déclencher le `SpawnActor` au niveau du socket "MuzzleFlash" de l'arme.
*   **Inputs :** Configuration des `Action Mappings` dans les *Project Settings* pour lier le clic gauche au tir principal.
*   **Logique de jeu :** Liaison entre le personnage et l'arme équipée via une variable de référence d'acteur pour permettre le tir.

### Ce qui reste d'actualité aujourd'hui
Bien que le moteur ait évolué vers Unreal Engine 5, les concepts fondamentaux abordés ici restent parfaitement transposables :
*   **L'héritage en Blueprint :** La création de classes "Master" (parente) pour les projectiles et les armes est une pratique indispensable pour garder un projet propre et scalable.
*   **Gestion des sockets :** L'utilisation des sockets sur les meshes pour définir les points d'origine des tirs ou l'éjection des douilles est toujours la méthode standard.
*   **Input System :** Bien que l'Enhanced Input System soit désormais la norme dans l'UE5, la logique de vérification (`Cast`) et de déclenchement d'événements reste identique dans sa structure.
*   **Optimisation :** La gestion de la durée de vie des projectiles (`DestroyActor`) est une règle d'or pour éviter les fuites de mémoire et les problèmes de performance dans n'importe quel projet FPS.

{{< footer >}}