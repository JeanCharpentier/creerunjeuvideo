---
title: "Mise à niveau Unreal Engine 5 : Adapter son Projet au Nouveau Système d'Enhanced Input"
date: 2026-06-12
category: Archive
tags:
  - Unreal Engine 5
  - Enhanced Input
  - Blueprints
  - Migration
  - Tutoriel

prev_url: ""
next_url: "/unreal-engine-5/systeme-construction/cours-1/"
images: ["https://img.youtube.com/vi/VpMGqutsLSY/maxresdefault.jpg"]
---

Ce tutoriel est issu de mes archives  et est partagé pour son intérêt conceptuel.

{{< youtube-rgpd "VpMGqutsLSY" >}}

Dans cet épisode de transition indispensable pour la reprise de notre mini-série, nous découvrons comment moderniser la gestion des entrées utilisateur. L'ancien système d'Inputs d'Unreal Engine 4 (*Action/Axis Mappings*) étant obsolète, nous apprenons à configurer le puissant framework *Enhanced Input* d'Unreal Engine 5.

### Concepts clés abordés dans ce tutoriel

* **Dépréciation de l'ancien système (Legacy Inputs) :** Constat des messages d'avertissement d'UE5 indiquant que les anciennes configurations d'inputs dans les paramètres du projet (*Project Settings*) sont désormais désuètes et destinées à disparaître.
* **Création des Input Actions (IA) :**
    * Compréhension du concept d'objet d'entrée individuel : création d'un fichier dédié pour chaque action du joueur (ex: `IA_BuildMode` pour la touche **B**, `IA_Validate` pour le clic gauche).
    * Configuration du type de valeur attendue (Value Type), notamment le type *Digital (booléen)* pour les boutons de type On/Off.
* **Mise en place de l'Input Mapping Context (IMC) :**
    * Création du fichier de contexte (`IMC_Default`) qui sert de dictionnaire pour lier les *Input Actions* à des touches physiques du clavier ou de la souris.
    * Flexibilité du système permettant d'activer ou de désactiver des contextes entiers à la volée selon les situations de jeu (ex: mode conduite, mode construction, mode exploration).
* **Injection du Contexte dans le Character :**
    * Utilisation des nœuds d'initialisation dans le Blueprint du personnage principal (`Begin Play`).
    * Récupération du contrôleur du joueur (`Get Player Controller`), conversion vers le sous-système local (`Get Enhanced Input Local Player Subsystem`), puis appel du nœud `Add Mapping Context`.
* **Exploitation des événements d'entrée (Triggered vs Started) :**
    * Remplacement des anciens nœuds d'inputs rouges par les nouveaux nœuds *Enhanced Action Events*.
    * Manipulation des broches d'exécution spécifiques : utilisation de l'état `Started` (appelé une seule fois à la pression de la touche) pour reproduire fidèlement le comportement de l'ancienne broche `Pressed`.

### Ce qui reste d'actualité aujourd'hui

Ce tutoriel de transition est plus que jamais crucial, car l'architecture introduite est devenue le standard absolu de l'industrie :

1. **L'Enhanced Input comme norme standard :** Sur les versions récentes d'Unreal Engine 5, l'ancien système d'input a été complètement retiré du code source. Maîtriser les *Input Actions* et les *Mapping Contexts* n'est plus une option, c'est la seule méthode officielle pour faire bouger un personnage ou interagir avec le monde.
2. **L'architecture par contextes interchangeables :** Concevoir ses jeux en séparant les contrôles (un contexte pour les déplacements à pied, un contexte temporaire exclusif pour le mode construction) reste la façon la plus propre et la plus performante d'éviter les conflits de touches et de simplifier les machines à états (*State Machines*).
3. **La gestion fine des états d'activation :** Les broches `Started`, `Ongoing`, `Canceled`, `Triggered` et `Completed` offrent une précision chirurgicale pour gérer le gameplay (distinction naturelle entre un appui court, un appui long ou un maintien de touche), ce qui évite de surcharger l'architecture globale avec des variables et des chronomètres (*Timers*) manuels.

{{< footer >}}