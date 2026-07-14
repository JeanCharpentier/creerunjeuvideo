---
title: "12. Conditions de victoire, de défaite et création des écrans de fin (Game Over / Victory)"
date: 2026-06-12
category: Archive
weight: 12
tags: [Unreal Engine 5, Kawaii Slender, Blueprint, Input System, Audio, Game Design]
prev_url: "/unreal-engine-5/jeu-horreur-kawaii/11-attaque-ennemie-ragdoll-physique-unreal"
next_url: "/unreal-engine-5/jeu-horreur-kawaii/13-terrain-editore-editeur-landscape-mode"
images: ["https://img.youtube.com/vi/_MQSnhg3LCA/maxresdefault.jpg"]
---

{{< youtube-rgpd "_MQSnhg3LCA" >}}

Dans ce douzième et dernier grand épisode de la série *Kawaii Slender*, nous bouclons la boucle de notre boucle de gameplay (*game loop*). Après avoir configuré la traque et la mort physique du personnage, nous programmons les deux états finaux indispensables à tout jeu vidéo : la condition de défaite (Game Over) et la condition de victoire (Victory), avec la création d'écrans dédiés et la gestion de la capture de la souris.

### Concepts clés abordés dans ce tutoriel

* **Création d'interfaces utilisateur conditionnelles :**
    * Conception de deux **Widget Blueprints** distincts sous UMG : `WBP_GameOver` (ambiance sombre et dramatique) et `WBP_Victory` (célébration et affichage du score final).
    * Intégration de boutons interactifs standards : "Rejouer" (*Retry*) pour relancer instantanément la partie et "Quitter" (*Quit*) pour fermer l'application.
* **Gestion du flux de jeu et rechargement de niveau :**
    * Utilisation du node **Open Level (by Object Reference)** ou *Open Level (by Name)* relié au bouton "Rejouer" pour recharger proprement la carte actuelle et réinitialiser l'ensemble des variables, des placements d'objets et de l'IA.
    * Implémentation du node **Quit Game** pour fermer proprement le build ou quitter l'éditeur de jeu.
* **Contrôle du curseur et du focus d'entrée (Input Modes) :**
    * Bascule indispensable du mode de saisie : utilisation du node **Set Input Mode UI Only** (ou *Game And UI*) dès que l'écran de fin apparaît pour empêcher le joueur de continuer à bouger la caméra à l'aveugle derrière l'interface.
    * Utilisation du node **Set Show Mouse Cursor** (coché à *True*) appliqué au *Player Controller* pour faire réapparaître le pointeur de la souris à l'écran et permettre le clic sur les boutons.
* **Validation de la condition de victoire :**
    * Script au sein du système de ramassage : vérification continue ou sur événement du nombre de burgers collectés par le joueur.
    * Utilisation d'un comparateur (ex: `BurgersRamassés == TotalBurgersDuNiveau`) pour déclencher l'affichage du widget de victoire dès que l'objectif chiffré est atteint.
* **Mise en pause et sécurité logique :**
    * Utilisation du node **Set Game Paused** pour figer le temps en arrière-plan (mouvements de l'IA, décharge des jauges) pendant que le joueur interagit avec les menus de fin, évitant que le poulet ne continue ses boucles d'attaque après coup.

### Ce qui reste d'actualité aujourd'hui

La gestion de la structure de fin de partie et le contrôle des entrées présentés ici restent des piliers immuables sous Unreal Engine 5 :

1. **La gestion rigoureuse du Player Controller et des Input Modes :** Oublier de repasser en mode UI ou de masquer/afficher le curseur de la souris (`Set Show Mouse Cursor`) est l'un des bugs les plus fréquents en gamedev. L'utilisation conjointe des nodes d'Input Mode et du ciblage du *Player Controller* reste la méthode officielle et obligatoire sous UE5.
2. **Le rechargement de niveau par référence d'objet :** Utiliser *Open Level (by Object Reference)* plutôt qu'une chaîne de caractères (String) brute évite les erreurs de frappe (typos) et garantit que le moteur maintient les liens internes intacts, même si vous renommez ou déplacez vos fichiers de cartes dans votre arborescence.
3. **L'architecture modulaire des widgets de fin :** Créer des écrans de fin autonomes qui gèrent eux-mêmes leur logique d'interaction (rejouer/quitter) plutôt que de tout surcharger dans le blueprint du personnage reste une excellente pratique pour conserver un projet propre, lisible et facilement transférable sur d'autres prototypes.

---
{{< footer >}}