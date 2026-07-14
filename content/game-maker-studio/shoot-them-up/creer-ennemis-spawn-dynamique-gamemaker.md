---
title: "8. Créer des ennemis et un système de spawn dynamique"
weight: 8
prev_url: "/game-maker-studio/shoot-them-up/maitriser-tir-automatique-gestion-instances-game-maker/"
next_url: "/game-maker-studio/shoot-them-up/optimiser-vagues-ennemis-game-maker-escadrilles/"
date: 2023-10-27
categories: ['Archive']
tags: ['GameMaker', 'Tutoriel', 'Game Development', 'GML']
images: ["https://img.youtube.com/vi/HwTww1W-ZDM/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/HwTww1W-ZDM/maxresdefault.jpg"]
---

Apprenez à donner vie à votre jeu en intégrant des ennemis mobiles et un système de génération automatique (spawner) pour dynamiser vos niveaux.

{{< youtube-rgpd "HwTww1W-ZDM" >}}

### Résumé des notions clés
*   **Initialisation du mouvement :** Utilisation de la variable `hspeed` (horizontal speed) avec une valeur négative pour déplacer un objet de la droite vers la gauche.
*   **Gestion des sprites :** Utilisation de l'outil "Mirror Flip" dans l'éditeur de sprite pour corriger l'orientation des ennemis sans modifier les ressources graphiques originales.
*   **Le concept de Spawner :** Création d'un objet invisible (sans sprite ou avec un sprite de repère) dont le rôle unique est de générer d'autres instances dans la room.
*   **Automatisation avec les Alarmes :** Utilisation de l'événement `Alarm` combiné à `instance_create` pour déclencher l'apparition d'ennemis à intervalles réguliers.
*   **Contrôle du rythme :** Ajustement de la fréquence d'apparition en utilisant `room_speed` (le nombre de frames par seconde du jeu) pour définir un timing précis en secondes.

### Ce qui reste d'actualité aujourd'hui
Bien que les versions récentes de GameMaker aient introduit des fonctionnalités comme les *Sequences* ou les *Pathfinding*, les principes abordés ici restent les fondations indispensables de tout développeur :

1.  **La logique de "Spawner" :** C'est une technique universelle. Que vous utilisiez des objets invisibles ou des systèmes de gestion de vagues (Wave Managers) plus complexes, le besoin de séparer la logique de génération de celle des entités elles-mêmes est crucial pour maintenir un code propre.
2.  **La gestion du temps :** Comprendre le lien entre `room_speed` et les alarmes est essentiel pour créer des jeux dont la difficulté est constante, quel que soit le taux de rafraîchissement de l'écran.
3.  **La manipulation des instances :** La fonction `instance_create` (ou ses variantes modernes `instance_create_layer`) demeure le cœur battant de la création dynamique d'objets en jeu. Maîtriser ces bases permet de passer facilement à des systèmes de génération procédurale plus avancés.

{{< footer >}}