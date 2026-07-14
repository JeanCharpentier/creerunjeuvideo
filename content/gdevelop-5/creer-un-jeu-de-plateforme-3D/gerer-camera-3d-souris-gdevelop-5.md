---
title: "8. Gérer la caméra 3D à la souris dans GDevelop 5"
weight: 8
date: 2023-10-27
categories: ['Tutoriels']
tags: ['GDevelop', '3D', 'Caméra', 'Souris', 'GameDev']
images: ["https://img.youtube.com/vi/79XRsPVCQ1U/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/79XRsPVCQ1U/maxresdefault.jpg"]
---

Bienvenue dans ce dernier volet de notre série dédiée à la création 3D sur GDevelop 5. Après avoir posé les bases, il est temps de passer à une étape cruciale pour l'immersion : la gestion fluide de la caméra à la souris. Nous allons voir comment verrouiller le curseur, créer des mouvements naturels et gérer les limites de rotation pour éviter les comportements erratiques.

{{< youtube-rgpd "79XRsPVCQ1U" >}}

### Résumé des étapes clés
*   **Organisation avec les groupes :** Utilisation des groupes d'événements pour structurer votre code et garder une lisibilité optimale.
*   **Verrouillage du pointeur :** Installation de l'extension "Verrouillage du pointeur de la souris" pour capturer le curseur dans la fenêtre de jeu.
*   **Comportement 3D :** Ajout du comportement "Caméra à la troisième personne" sur l'objet joueur.
*   **Calculs de rotation :** Utilisation des mouvements X et Y de la souris, multipliés par la largeur/hauteur de la scène pour une sensibilité constante.
*   **Fonction Clamp :** Limitation des angles de rotation (verticale et horizontale) pour éviter que la caméra ne tourne à 360° ou ne traverse le sol.
*   **Gestion de la défaite :** Déverrouillage automatique du curseur lors d'une collision avec un objet de défaite pour permettre au joueur d'interagir avec les menus.

### Ce qui reste d'actualité aujourd'hui
Bien que GDevelop évolue rapidement, les principes abordés ici restent fondamentaux :
*   **La structure du code :** L'utilisation des groupes d'événements est une bonne pratique indispensable pour tout projet de taille moyenne à grande.
*   **La gestion des entrées :** Le verrouillage du pointeur est toujours la méthode standard pour les jeux à la première ou troisième personne.
*   **La normalisation des sensibilités :** Diviser le mouvement de la souris par la résolution de la fenêtre est une technique robuste pour garantir une expérience de jeu identique sur tous les écrans.
*   **La fonction Clamp :** Elle reste l'outil mathématique privilégié pour restreindre les mouvements de caméra et éviter les bugs visuels (comme le retournement de l'image).

{{< footer >}}