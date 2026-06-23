---
title: "Série: Création d'un Slender-like (Kawaii Slender) sur Unreal Engine 5"
date: 2026-06-12
layout: "chapter-home"
description: "Retrouvez le guide complet et le résumé des 16 vidéos de la série consacrée à la création de A à Z d'un jeu d'horreur de type Slender-like sous Unreal Engine 5."

prev_url: ""
next_url: ""
---

Bienvenue dans l'index de la série de cours **Kawaii Slender**. Ce chapitre complet vous guide pas à pas à travers l'apprentissage d'Unreal Engine 5 en prenant pour cas d'usage pratique la création d'un jeu de survie/horreur complet. De l'installation des outils de développement à la compilation finale de votre jeu exécutable, découvrez le résumé des compétences clés acquises tout au long des 16 vidéos de la formation.

---

## 🗺️ Vue d'ensemble du programme (16 Épisodes)

Pour faciliter votre progression, l'apprentissage a été segmenté en trois grandes phases de développement :

### Phase 1 : Fondations du Gameplay & IA (Épisodes 1 à 6)
* **Configuration initiale :** Prise en main de l'interface d'Unreal Engine 5, gestion des dossiers de projet et intégration de la caméra à la première personne (*First Person*).
* **Mécaniques de ramassage :** Création des objets clés à collecter (les pages/peluches) via des systèmes de collisions (*Trigger Boxes*) et incrémentation de variables.
* **Interface Utilisateur (UI/UMG) :** Conception d'un compteur dynamique à l'écran pour afficher la progression des objets ramassés et gestion des conditions de victoire.
* **Intelligence Artificielle du Monstre :** Configuration du *NavMesh* et programmation du comportement de traque du Slender, configuré pour chasser le joueur sans relâche à travers la carte.

### Phase 2 : Univers, Level Design & Ambiance (Épisodes 7 à 12)
* **Création de la carte (Landscape) :** Modelage du terrain en 3D (bosses, creux, sentiers) et création de textures de sols réalistes (boue, herbe, roche).
* **Végétation et Feuillage :** Utilisation de l'outil *Foliage* pour peindre rapidement une forêt dense et naturelle (arbres, buissons, fougères) tout en gérant les options de performance (LODs).
* **Narration environnementale :** Habillage de la forêt avec des structures et des obstacles en basse résolution (cabanes, barrières, ruines) pour guider subtilement l'exploration du joueur et rompre la monotonie visuelle.
* **Atmosphère nocturne & Éclairage :** Configuration d'un cycle de nuit profonde, ajustement du brouillard de distance (*Exponential Height Fog*) et création de la lampe torche du joueur.

### Phase 3 : Polish, Effets et Exportation Finale (Épisodes 13 à 16)
* **Matériaux émissifs & Shader de lanterne :** Création de sources de lumière locales (lanternes) dotées d'un script de vacillement aléatoire (*Flickering Light*) pour simuler une flamme réaliste.
* **Systèmes de particules (Niagara) :** Ajout de micro-effets atmosphériques (lucioles et moucherons) attirés par les sources de chaleur et de lumière.
* **Écrans techniques de transition :** Création des menus de défaite (*Game Over*), de victoire, et intégration d'un **Menu Principal complet** (`LVL_MainMenu`) isolé avec les fonctions *Jouer* (chargement de niveau par référence d'objet) et *Quitter*.
* **Compilation du jeu (Packaging) :** Configuration des dépendances systèmes obligatoires (**Visual Studio Community**) et export complet du projet en mode **Shipping** pour obtenir un dossier de jeu optimisé et un exécutable autonome (`.exe`) distribuable.

---

## 🛠️ Les piliers techniques maîtrisés

Au terme de ce chapitre, vous aurez acquis des compétences solides réutilisables sur n'importe quel autre prototype de jeu sous Unreal Engine 5 :

| Outil / Système | Rôle clé dans le projet |
| :--- | :--- |
| **Blueprints Événementiels** | Programmation visuelle de toute la logique : boutons, cycles logiques de ramassage, conditions de fin de partie. |
| **UMG (Unreal Motion Graphics)** | Création des interfaces (HUD de jeu, menus contextuels, menus principaux). |
| **GameMode & Level Blueprints** | Gestion globale des règles de la partie et configuration technique spécifique des cartes (ex: forcer l'affichage du curseur de la souris sur le menu). |
| **Mode Shipping / Export** | Nettoyage des commandes de débogage et compilation propre pour le joueur final. |

---

## ⚠️ Rappels de sécurité importants pour les développeurs

> 🗄️ **Sauvegardes et Backups :** Pensez à réaliser très régulièrement des copies de sécurité de votre dossier de projet avant de procéder aux phases de nettoyage d'assets ou de packaging lourd.
>
> 🛑 **Conflits de compilation :** Lors de l'exportation finale de votre jeu (*Package Project*), veillez à désactiver ou mettre en pause temporairement vos logiciels de synchronisation en arrière-plan (NAS, Dropbox, Nextcloud, OneDrive, etc.). Unreal Engine effectue des milliers de lectures/écritures rapides de fichiers qui peuvent se faire corrompre par une synchronisation simultanée, provoquant des erreurs de compilation inconnues.

---

## 🚀 Prêt à commencer ?

Naviguez à travers les différents sous-articles de ce chapitre en utilisant la barre de navigation latérale pour visionner les tutoriels détaillés, récupérer la logique des scripts en Blueprints et finaliser votre propre version du **Kawaii Slender** !

{{< footer >}}