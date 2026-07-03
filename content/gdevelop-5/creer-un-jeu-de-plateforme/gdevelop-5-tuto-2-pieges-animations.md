---
title: "2. GDevelop 5 : Ajouter des pièges et des animations à votre personnage"
weight: 2
date: 2024-05-23
categories: ['Tutoriels']
tags: ['GDevelop', 'GameDev', 'Débutant', 'Tutoriel']
---

Dans ce deuxième épisode de notre guide dédié à **GDevelop 5**, nous passons à la vitesse supérieure. Après avoir créé les bases de votre niveau, il est temps de rendre votre jeu plus vivant et plus dangereux. Nous allons apprendre à intégrer des pièges mortels, à gérer les collisions de manière précise et, surtout, à donner vie à votre personnage grâce aux animations.

{{< youtube-rgpd "Tp1WyyOKN98" >}}

### Au programme de ce tutoriel :
*   **Gestion des projets Cloud :** Comment retrouver et rouvrir vos projets enregistrés sur le cloud GDevelop.
*   **Ajout de pièges :** Utilisation du magasin de ressources pour intégrer des pics et paramétrage des collisions.
*   **Masques de collision :** Apprendre à ajuster les zones de collision (hitboxes) pour qu'elles soient précises et performantes (notion de polygone convexe).
*   **Animations :** Utilisation des animations intégrées (marche, repos) et bascule automatique selon l'état du joueur.
*   **Logique de mouvement :** Retourner le personnage horizontalement en fonction de sa vitesse pour une gestion fluide des déplacements.
*   **Optimisation :** Utilisation des sous-événements pour structurer votre code et le rendre plus lisible.

### Ce qui reste d'actualité aujourd'hui
Bien que GDevelop évolue constamment, les concepts abordés dans cette vidéo restent les piliers fondamentaux du moteur :
*   **La structure des événements :** L'utilisation des sous-événements est toujours la meilleure pratique pour garder un code propre et maintenable.
*   **La gestion des collisions :** La règle du "polygone convexe" est une contrainte technique universelle dans le développement de jeux 2D pour garantir la détection des collisions sans surcharger le processeur.
*   **La logique de mouvement :** Tester la vitesse horizontale (`VitesseX`) plutôt que les touches du clavier est une approche "pro" qui facilite grandement l'ajout futur de manettes ou de contrôles tactiles.
*   **Le flux de travail :** Le système de "Changer l'animation par son nom" est toujours la méthode la plus intuitive et recommandée pour éviter les erreurs liées aux index numériques.

{{< footer >}}