---
title: "3. Créer un menu, gérer le score et les variables dans GDevelop 5"
weight: 3
date: 2024-05-23
categories: ['Tutoriels GDevelop']
tags: ['GDevelop', 'GameDev', 'Débutant', 'Variables', 'Menu']
---

Dans ce nouveau volet de notre série de découverte, nous allons finaliser notre jeu de plateforme en ajoutant deux éléments essentiels : un système de score persistant et un écran de menu fonctionnel. Vous apprendrez à manipuler les variables globales et à faire communiquer vos différentes scènes entre elles.

{{< youtube-rgpd "VV_ltHBAOLM" >}}

### Ce que vous allez apprendre dans ce tutoriel :
*   **Ajout d'éléments de décor :** Utilisation de fonds (backgrounds) et gestion de la profondeur (Z-order) pour superposer correctement vos objets.
*   **Système de ramassage :** Créer des objets "pièces" et les supprimer lors de la collision avec le joueur.
*   **Les variables globales :** Comprendre le concept de "boîte de stockage" pour conserver votre score tout au long de la partie, même en changeant de scène.
*   **Affichage dynamique :** Convertir des nombres en texte (`ToString`) pour mettre à jour votre score à l'écran en temps réel.
*   **Création d'un menu :** Utiliser des boutons (`Panel Sprite`) pour naviguer entre votre menu principal et votre niveau de jeu.
*   **Objets globaux :** Apprendre à rendre un objet (comme le score) persistant sur toutes les scènes du projet.

### Ce qui reste d'actualité aujourd'hui
Bien que GDevelop évolue régulièrement, les concepts abordés ici restent les piliers fondamentaux du développement de jeux :
*   **La logique des variables :** La distinction entre variables globales, de scène et d'objet est toujours la base pour gérer les états de jeu (score, vie, inventaire).
*   **La gestion des scènes :** Le passage d'un menu vers un niveau de jeu via des événements reste la méthode standard pour structurer un projet.
*   **L'optimisation :** L'utilisation du débogueur pour surveiller le nombre d'instances est une pratique indispensable pour éviter les fuites de mémoire et les ralentissements sur mobile ou navigateur.
*   **La concaténation :** La manipulation des chaînes de caractères pour afficher du texte dynamique (ex: "Score : 10") est une compétence clé que vous réutiliserez dans tous vos futurs projets.

{{< footer >}}