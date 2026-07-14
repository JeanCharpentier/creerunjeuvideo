---
title: "16. Création du menu principal, optimisation finale et export du jeu (Packaging)"
date: 2026-06-12
category: Archive
weight: 16
tags: [Unreal Engine 5, Kawaii Slender, Blueprint, Input System, Audio, Game Design]
prev_url: "/unreal-engine-5/jeu-horreur-kawaii/15-props-decor-lumiere-clignotte-lanterne-village"
next_url: ""
images: ["https://img.youtube.com/vi/TUdpY264w_U/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/TUdpY264w_U/maxresdefault.jpg"]
---

{{< youtube-rgpd "TUdpY264w_U" >}}

Nous y sommes ! Après quinze épisodes passés à bâtir notre gameplay, façonner notre monstre, sculpter notre forêt et peaufiner l'ambiance sonore, il est temps de poser la dernière pierre à l'édifice. Dans cet épisode final de la série *Kawaii Slender*, nous créons l'écran de titre (Menu Principal) et passons à la compilation définitive (**Packaging**) de notre projet afin de générer un build autonome (exécutable `.exe`) prêt à être partagé et testé par vos proches.

### Concepts clés abordés dans ce tutoriel

* **Conception du Menu Principal (Main Menu UI) :**
    * Création d'un nouveau Widget Blueprint dédié (`WBP_MainMenu`) comprenant un titre stylisé et deux boutons interactifs principaux : **Jouer** et **Quitter**.
    * **Logique de programmation des boutons :**
        * Sur l'événement *On Clicked* du bouton "Jouer", appel du node **Open Level (by Object Reference)** pointant vers notre carte de jeu principale pour lancer la partie.
        * Sur l'événement *On Clicked* du bouton "Quitter", appel du node **Quit Game** pour fermer proprement l'application.
* **Mise en scène du menu dans un niveau dédié :**
    * Création d'une nouvelle carte totalement vide (`LVL_MainMenu`) faisant office d'antichambre technique.
    * Configuration du **Level Blueprint** de cette carte au *Begin Play* : création du widget du menu, ajout à l'écran (*Add to Viewport*), et configuration indispensable des nodes **Set Input Mode UI Only** et **Set Show Mouse Cursor** (coché sur *True*) via le *Player Controller* pour donner la main à la souris dès l'ouverture du jeu.
* **Préparation du projet avant l'export (Project Settings) :**
    * Configuration de la map de démarrage : rendez-vous dans les options du projet (*Maps & Modes*) pour définir notre nouvelle carte `LVL_MainMenu` comme le niveau par défaut chargé au lancement du jeu final (*Game Default Map*).
    * Nettoyage et vérification des assets inutilisés ou obsolètes pour alléger le poids final du build et éviter les erreurs de compilation croisée.
* **Le Packaging (Exportation finale) :**
    * Utilisation du menu **Platforms** -> **Windows** d'Unreal Engine 5.
    * Choix de la configuration de build : bascule du mode *Development* (qui conserve les consoles de commandes et les outils de débug) vers le mode **Shipping** pour optimiser le code et les textures pour le joueur final.
    * Lancement de la compilation (*Package Project*) et décryptage des logs de sortie (*Output Log*) pour s'assurer du bon déroulement du build sans avertissement critique.

### Ce qui reste d'actualité aujourd'hui

Ce processus de finalisation et d'export sous Unreal Engine 5 reste le standard absolu de l'industrie pour clore un prototype :

1. **L'étanchéité du flux Menu -> Jeu :** Séparer le menu principal dans un niveau technique léger (`LVL_MainMenu`) plutôt que de l'injecter de force par-dessus la carte de jeu reste la méthode la plus propre et sécurisée. Cela évite de charger inutilement en mémoire l'univers 3D, le NavMesh et l'Intelligence Artificielle du monstre avant même que le joueur n'ait cliqué sur "Jouer".
2. **Le piège des Maps & Modes :** Oublier de configurer la *Game Default Map* dans les paramètres du projet est l'erreur classique n°1 en développement. Unreal exporterait alors sa carte par défaut ou un écran noir. Configurer rigoureusement ses fenêtres de démarrage reste indispensable sur UE5.
3. **Le build en mode Shipping :** Compiler son projet en mode *Shipping* reste la seule méthode valide pour distribuer un jeu vidéo de manière professionnelle. Elle permet non seulement de gagner de précieux précieux FPS en désactivant le code de débogage sous-jacent, mais protège également votre projet contre la triche et l'injection de commandes par la console.

---

*C'est ici que se termine l'aventure Kawaii Slender sur Unreal Engine ! Merci à toutes et à tous d'avoir suivi cette série de découverte. Que ce soit sur ce moteur ou sur d'autres outils plus légers et terre-à-terre (comme GDevelop ou Pico-8), continuez de bricoler, d'expérimenter et de donner vie à vos projets de jeux vidéo !*

{{< footer >}}