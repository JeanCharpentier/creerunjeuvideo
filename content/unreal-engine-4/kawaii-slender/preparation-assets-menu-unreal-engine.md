---
title: "19. Préparation des assets graphiques pour votre Menu"
weight: 19
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['UI', 'Menu', 'Graphisme', 'Tutoriel', 'Asset']
---

Dans cet épisode, nous faisons une petite pause technique sur Unreal Engine 4 pour nous concentrer sur la partie artistique. Avant de plonger dans le système de Widget Blueprint, il est essentiel de préparer vos assets graphiques. Un menu propre commence par une bonne préparation de vos images de fond et de vos boutons.

{{< youtube-rgpd "LkOTYxSQlgU" >}}

### Résumé du tutoriel
*   **Création du fond d'écran :** Utilisation d'un logiciel de retouche (Paint.net) pour créer une image en 1920x1080 (Full HD). Utilisation des dégradés et des modes de fusion pour un rendu moderne.
*   **Gestion des formats :** Importance d'enregistrer vos fonds en `.png` ou `.jpg` dans un dossier dédié `Resources/Menu` au sein de votre projet.
*   **Conception des boutons :** Création de boutons avec des états distincts (Normal, Survolé/Hover).
*   **Transparence :** Utilisation obligatoire du format `.png` pour les boutons afin de conserver la transparence du fond.
*   **Liste des assets nécessaires :**
    *   Fond d'écran.
    *   Boutons principaux : "Jouer", "Options", "Quitter".
    *   Boutons secondaires (Menu Options) : Résolutions (640x480, 1280x720, 1920x1080) et bouton "Retour".

### Ce qui reste d'actualité aujourd'hui
Bien que les versions d'Unreal Engine aient évolué (passant de la 4 à la 5), les principes fondamentaux de l'UI restent identiques :
1.  **La préparation externe :** Il est toujours préférable de préparer ses assets (boutons, icônes, fonds) dans des logiciels spécialisés (Photoshop, GIMP, Paint.net, Figma) avant de les importer dans le moteur.
2.  **L'importance des états :** Le concept de "Hover" (survol) et "Pressed" (cliqué) est toujours la base de l'interactivité dans les `User Widgets` d'Unreal.
3.  **Gestion des résolutions :** Travailler en Full HD (1920x1080) reste le standard minimal pour garantir une bonne qualité visuelle sur la majorité des écrans.
4.  **Organisation des dossiers :** Garder une structure de projet propre (dossier `Resources` ou `UI`) est une bonne pratique indispensable pour ne pas perdre ses fichiers lors de la montée en charge du projet.

{{< footer >}}