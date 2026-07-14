---
title: "4. Créer et intégrer des effets sonores dans GDevelop 5"
weight: 4
date: 2023-10-27
categories: ['Tutoriels']
tags: ['GDevelop', 'GameDev', 'Audio', 'Tutoriel', '3D']
images: ["https://img.youtube.com/vi/DgM7DPANOzw/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/DgM7DPANOzw/maxresdefault.jpg"]
---

Dans ce quatrième épisode de notre série dédiée à la création d'un jeu de plateforme 3D sur GDevelop 5, nous délaissons le visuel pour nous concentrer sur l'immersion sonore. Un jeu sans son est une expérience incomplète : aujourd'hui, nous allons apprendre à générer nos propres effets sonores gratuitement et à les intégrer intelligemment dans notre projet.

{{< youtube-rgpd "DgM7DPANOzw" >}}

### Au programme de ce tutoriel :
*   **Génération de sons :** Utilisation de l'outil en ligne [bfxr.net](https://www.bfxr.net/) pour créer des effets de saut, de ramassage de pièces et de bruits de pas.
*   **Organisation des ressources :** Comment structurer son dossier de projet pour séparer les assets du moteur des fichiers personnels.
*   **Programmation audio :**
    *   Jouer un son lors d'une collision (ex: ramasser une pièce).
    *   Gérer les sons en boucle (ex: bruits de pas) avec la condition "Déclencher une seule fois".
    *   Utilisation des **canaux audio** pour contrôler précisément le démarrage et l'arrêt des sons (notamment pour stopper le bruit de marche quand le joueur s'arrête).

### Ce qui reste d'actualité aujourd'hui
*   **La gestion des canaux :** L'utilisation des canaux (`Play a sound on a channel`) reste la méthode recommandée pour gérer les sons persistants ou répétitifs, car elle permet de stopper un son spécifique sans affecter les autres.
*   **L'importance du "Déclencher une seule fois" :** Cette condition est indispensable pour éviter que GDevelop ne relance le son à chaque frame (60 fois par seconde), ce qui créerait une saturation audio désagréable.
*   **Organisation des dossiers :** Garder une structure propre (`/assets`, `/sounds`, `/resources`) est toujours la meilleure pratique pour maintenir un projet sain, surtout à mesure qu'il grandit.
*   **Outils externes :** Bien que des logiciels plus avancés existent, `bfxr` reste un standard incontournable pour le prototypage rapide de jeux 2D/3D grâce à sa simplicité et son format de fichier léger.

{{< footer >}}