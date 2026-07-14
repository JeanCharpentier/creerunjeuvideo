---
title: "2. Création de votre chaîne de production : Du minerai à l''épée"
weight: 2
date: 2023-10-27
categories: ['Modding']
tags: ['Hytale', 'Tutoriel', 'Modding', 'GameDev']
images: ["https://img.youtube.com/vi/Wc_XISe1edE/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/Wc_XISe1edE/maxresdefault.jpg"]
---

Bienvenue dans ce deuxième volet de notre série dédiée au modding sur Hytale ! Après avoir modélisé et importé notre première épée, il est temps de passer aux choses sérieuses : intégrer cet objet dans l'économie réelle du jeu. Aujourd'hui, nous allons apprendre à créer un minerai, le transformer en lingot, et configurer toute la chaîne de production pour que votre création soit accessible via le gameplay.

{{< youtube-rgpd "Wc_XISe1edE" >}}

### Résumé du tutoriel
*   **Nettoyage du projet :** Comment supprimer proprement votre ancien modpack pour éviter les conflits lors de vos nouvelles itérations.
*   **Internationalisation (i18n) :** Mise en place d'un fichier `server.lang` pour gérer les noms et descriptions de vos objets proprement, en préparation des futures traductions.
*   **Extraction des assets :** Utilisation prudente du fichier `assets.zip` pour récupérer les textures de base (cuivre, fer, argent) afin de servir de modèles pour vos créations.
*   **Création du minerai :** Utilisation des outils créatifs pour définir un nouvel item, appliquer une texture personnalisée et configurer son comportement de minage.
*   **Gestion des drops :** Configuration des listes de butin (loot tables) pour que le bloc de roche libère bien votre nouveau minerai une fois cassé.

### Ce qui reste d'actualité aujourd'hui
*   **La structure des fichiers :** La hiérarchie `common/resources/materials` reste la norme pour organiser vos textures et modèles.
*   **L'importance du fichier .lang :** Même avec les mises à jour du moteur, l'utilisation de clés de traduction (`item.weapon.name`) est une bonne pratique indispensable pour maintenir un mod propre et compatible avec plusieurs langues.
*   **Le workflow de modification :** Le processus de "recolorisation" de textures existantes reste la méthode la plus efficace pour les débutants afin de garantir une cohérence visuelle avec le style artistique d'Hytale.
*   **La rigueur du développement :** N'oubliez jamais de tester vos modifications en mode "Adventure" après chaque étape pour vérifier que les interactions (minage, drop, nommage) fonctionnent comme prévu.

{{< footer >}}