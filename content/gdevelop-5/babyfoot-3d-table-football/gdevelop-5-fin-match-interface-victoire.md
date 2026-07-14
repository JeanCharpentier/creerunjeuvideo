---
title: "6. Fin de match et gestion de l''interface de victoire"
weight: 6
date: 2023-10-27
categories: ['GDevelop 5']
tags: ['tutoriel', 'gamedev', 'interface', 'logique-jeu']
images: ["https://img.youtube.com/vi/b1HJihpcfcQ/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/b1HJihpcfcQ/maxresdefault.jpg"]
---

Dans cet épisode, nous finalisons la boucle de gameplay de notre jeu de baby-foot. Après avoir géré les déplacements et les scores, il est temps de définir les conditions de victoire pour conclure la partie et permettre au joueur de retourner au menu principal.

{{< youtube-rgpd "b1HJihpcfcQ" >}}

### Résumé des étapes clés
*   **Création de l'interface :** Ajout d'un objet texte pour afficher le résultat final et d'un bouton "Back" pour quitter la partie.
*   **Gestion de l'affichage :** Utilisation des actions "Cacher" et "Désactiver les interactions" au démarrage de la scène pour que l'interface de fin ne soit visible qu'au moment opportun.
*   **Logique de victoire :** Mise en place d'une condition vérifiant si le score d'un joueur atteint le score maximum (utilisation de "supérieur ou égal à" pour plus de sécurité).
*   **Contrôle du temps :** Utilisation de l'échelle de temps globale mise à 0 pour figer le jeu lors de l'affichage de l'écran de victoire.
*   **Optimisation :** Regroupement des objets dans un groupe de scène pour simplifier le code et éviter la duplication d'actions lors de la vérification des scores.

### Ce qui reste d'actualité aujourd'hui
*   **La gestion des interfaces :** La méthode consistant à cacher les objets UI et à désactiver leurs interactions est toujours la norme pour éviter les clics fantômes.
*   **L'échelle de temps :** Modifier l'échelle de temps globale (`TimeScale`) reste la manière la plus propre de mettre un jeu en pause dans GDevelop sans arrêter le moteur de rendu.
*   **La factorisation du code :** L'utilisation de groupes d'événements pour éviter de dupliquer la logique (comme le test de victoire pour le joueur 1 et 2) est une bonne pratique essentielle pour maintenir un projet propre et évolutif.
*   **Sécurité des conditions :** Privilégier les opérateurs "supérieur ou égal" plutôt que "égal" est un conseil d'expert qui évite bien des bugs si le score venait à être incrémenté deux fois par erreur lors d'une collision.

{{< footer >}}