---
title: "10. Intégration du son et effets audio"
date: 2026-06-13
weight: 13
categories: ["Archive"]
tags: ["Construct 2", "Game Dev", "Tutoriel", "Audio", "Sound Design"]
prev_url: "/construct-2/tuto-jeu-plateforme/9-systeme-codes-niveaux"
next_url: "/construct-2/tuto-jeu-plateforme/11-finalisation-deploiement-web"
images: ["https://img.youtube.com/vi/ckEkRpp3NLM/maxresdefault.jpg"]
---

Cette page est une archive pédagogique du dixième épisode de ma série consacrée à la création d'un jeu de plateforme avec Construct 2.

{{< youtube-rgpd "ckEkRpp3NLM" >}}

### Notions clés abordées

* **Gestion de l'objet Audio :** Ajout de l'objet système `Audio` pour gérer la lecture des sons dans l'ensemble du projet.
* **Importation de ressources :** Importation de fichiers au format OGG (format natif recommandé) depuis des plateformes comme OpenGameArt.
* **Organisation des sons :** Renommage et catégorisation des fichiers dans l'arborescence du projet (Sounds vs Musiques).
* **Déclenchement événementiel :** Utilisation de l'action `Audio > Play` dans la feuille d'événements pour déclencher des sons lors d'actions précises (saut, mort, collecte).
* **Optimisation du chargement :** Utilisation de l'action `Preload` pour éviter les latences de lecture sur les connexions internet lentes.

### Ce qui reste d'actualité aujourd'hui

Bien que Construct 2 soit un moteur désormais ancien, les principes de gestion audio présentés ici restent des fondamentaux du développement de jeux web :

* **Format OGG :** Il demeure le format de prédilection pour le web en raison de son excellent ratio qualité/poids et de sa prise en charge native par tous les navigateurs modernes.
* **Gestion du Preload :** La nécessité de précharger les assets audio pour garantir une expérience fluide est toujours d'actualité, particulièrement pour les jeux mobiles et les applications web.
* **Séparation des responsabilités :** La logique de déclenchement audio basée sur des événements (collision, saut) est un standard que l'on retrouve dans n'importe quel moteur moderne comme Godot, Unity ou Unreal Engine.
* **Gestion des effets :** La découverte des effets avancés (compresseur, réverbération, délai) reste une excellente introduction à la manipulation sonore, même si les outils ont évolué en termes d'interface.

{{< footer >}}