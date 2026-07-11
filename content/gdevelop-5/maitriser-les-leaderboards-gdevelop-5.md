---
title: "Maîtriser les Leaderboards dans GDevelop 5 : Guide complet"
date: 2026-06-17
categories: ['Tutoriels']
tags: ['GDevelop', 'Leaderboard', 'GD.games', 'GameDev']
---

Les classements (leaderboards) sont un excellent moyen d'augmenter la rétention de vos joueurs en ajoutant une dimension compétitive à vos créations. Grâce à l'intégration native de **GD.games**, GDevelop 5 permet de mettre en place un système de score en ligne robuste sans avoir à gérer de base de données complexe.

{{< youtube-rgpd "ZJg9goTl4bs" >}}

### Résumé du processus
*   **Préparation de la scène :** Création d'une interface simple avec un champ de saisie (pour les joueurs non connectés) et un bouton d'envoi.
*   **Configuration sur GD.games :** Enregistrement du projet sur le tableau de bord, création du leaderboard et paramétrage des options (ordre des scores, limites, visibilité).
*   **Logique d'événements :** 
    *   Vérification de l'authentification du joueur (`Player is authenticated`).
    *   Envoi du score via l'action `Save player score`.
    *   Gestion de l'affichage avec une scène dédiée pour le classement.
*   **Gestion des tricheurs :** Possibilité de supprimer des entrées spécifiques ou de réinitialiser totalement le classement depuis le dashboard.

### Ce qui reste d'actualité aujourd'hui
Bien que les interfaces de GDevelop évoluent, les principes fondamentaux présentés ici restent la norme pour tout développeur utilisant l'écosystème GD.games :
1.  **L'authentification hybride :** Le système permet toujours de gérer à la fois les utilisateurs connectés à GD.games et les joueurs "invités" (via un pseudo temporaire), ce qui est crucial pour ne pas freiner l'engagement.
2.  **La gestion des scores :** L'utilisation des variables de scène pour stocker le score avant l'envoi reste la méthode la plus propre et la plus efficace.
3.  **La modularité :** La séparation entre la scène de jeu et la scène d'affichage du classement (via `Pause and start a new scene`) demeure la meilleure pratique pour éviter les conflits d'interface et garantir une expérience utilisateur fluide.
4.  **Le Dashboard :** L'outil de gestion en ligne (accessible via le menu "File" > "Games Dashboard") reste le centre névralgique pour modérer vos classements et ajuster les paramètres visuels sans toucher au code de votre jeu.

{{< footer >}}