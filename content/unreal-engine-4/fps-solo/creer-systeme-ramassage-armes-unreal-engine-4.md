---
title: "12. Créer un système de ramassage d''armes (Pickup)"
weight: 12
date: 2026-06-17
categories: ['Tutoriels Unreal Engine']
tags: ['Unreal Engine 4', 'Blueprints', 'GameDev', 'FPS', 'Système de ramassage']
---

Dans cet épisode, nous abordons une mécanique essentielle pour tout FPS : le système de ramassage d'armes (ou "Pickup"). Nous allons apprendre à créer un acteur modulaire capable de faire apparaître une arme, de l'attacher au personnage via un Socket, et de gérer un temps de réapparition (respawn) configurable.

{{< youtube-rgpd "8sBfROhEkqE" >}}

### Résumé du tutoriel
*   **Création des classes de base** : Mise en place de `BP_Arme_Base` (l'objet arme) et `BP_Arme_Pickup_Base` (la zone de détection).
*   **Utilisation des Sockets** : Configuration du `Socket_Arm` sur le squelette du personnage pour que l'arme suive parfaitement les animations.
*   **Gestion des collisions** : Utilisation de `Box Collision` avec l'événement `OnComponentBeginOverlap` pour déclencher le ramassage.
*   **Logique de Respawn** : Désactivation temporaire des collisions et du rendu visuel (Set Hidden in Game) au lieu de détruire l'acteur, permettant une réapparition fluide après un délai configurable.
*   **Modularité** : Utilisation de variables "Instance Editable" pour définir la classe d'arme et le temps de respawn directement depuis l'éditeur.

### Ce qui reste d'actualité aujourd'hui
Bien que ce tutoriel utilise Unreal Engine 4, les concepts fondamentaux restent parfaitement transposables sur **Unreal Engine 5** :
1.  **Le système de Sockets** : La gestion des points d'attache sur les squelettes n'a pas changé ; c'est toujours la méthode recommandée pour attacher des objets aux mains des personnages.
2.  **La logique de "Hidden in Game"** : Désactiver la visibilité et les collisions d'un acteur est une pratique toujours très efficace pour optimiser les performances par rapport à la destruction et au ré-instanciation (Spawn/Destroy) d'objets.
3.  **Blueprints orientés objet** : L'utilisation de classes "Base" (Parent) pour créer des enfants est une bonne pratique de Game Design qui permet de gagner un temps précieux lors de l'ajout de nouvelles armes dans votre projet.
4.  **Modularité** : Rendre les variables éditables dans l'éditeur (l'œil ouvert dans le Blueprint) est la base pour créer des outils de design utilisables par des non-programmeurs.

{{< footer >}}