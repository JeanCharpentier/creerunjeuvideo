---
title: "2. Personnage, Ambiance Creepy et Configuration Clavier"
date: 2026-06-12
category: Archive
weight: 2
tags: [Unreal Engine 5, Kawaii Slender, Blueprint, Input System, Audio, Game Design]
prev_url: "/unreal-engine-5/jeu-horreur-kawaii/1-unreal-engine-5-installation-configuration-projet"
next_url: "/unreal-engine-5/jeu-horreur-kawaii/3-creer-lampe-torche-blueprint-joueur"
images: ["https://img.youtube.com/vi/dWYgCUyoWiE/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/dWYgCUyoWiE/maxresdefault.jpg"]
---

{{< youtube-rgpd "dWYgCUyoWiE" >}}

---

## Résumé des notions clés

Dans ce deuxième volet de la série **Kawaii Slender**, nous plongeons directement dans l'ajustement de l'ambiance et la personnalisation de notre prototype. Ce tutoriel se concentre sur l'exploitation des fonctionnalités natives du template et l'immersion sensorielle :

*   **Gestion du "Play In Editor" (PIE) :**
    *   Lancement du jeu dans une nouvelle fenêtre de l'éditeur pour garantir un affichage natif et rigoureux au format $16:9$.
*   **Configuration du système d'Input (UE5 Enhanced Input System) :**
    *   Prise en main du fichier `IMC_Default` pour modifier le mapping des touches.
    *   Ajout d'une double compatibilité transparente pour les claviers **AZERTY (ZQSD)** et **QWERTY (WASD)** sans forcer le joueur à reconfigurer ses options.
    *   Utilisation de la fonction d'enregistrement direct via l'icône de clavier jaune dans l'éditeur.
*   **Personnalisation du Personnage (Blueprint Class) :**
    *   Exploration du Blueprint `BP_FirstPersonCharacter` et de ses trois onglets principaux : le **Graphique d'événement** (Event Graph) pour le code visuel, le **Construction Script** (initialisation à la création de l'objet) et le **Hublot** (Viewport de prévisualisation).
    *   Remplacement du modèle 3D par défaut par un *Skeletal Mesh* de faucheuse (`SK_Style_Z_Death`).
    *   Introduction théorique au principe du **Retarget Manager** qui permet de transférer facilement les os et animations d'un squelette à un autre sous Unreal Engine 5.
    *   Ajustement de la position de la caméra à la première personne et masquage des éléments visuels indésirables en jeu (cocher l'option `Hidden in Game` pour supprimer l'ancienne ombre portée).
*   **Mise en place d'une atmosphère d'horreur :**
    *   Manipulation de la *Directional Light* (la lumière globale du soleil) via l'outil de rotation pour faire basculer le niveau dans une nuit noire.
    *   Gestion de l'audio avec le format **Sound Cue** : intégration d'une boucle musicale infinie (`Looping`) gérée par un système de nodes sonores, puis implémentation par simple glisser-déposer (*Drag and Drop*) dans le niveau pour créer une ambiance sonore d'ambiance en continu.

---

## Ce qui reste d'actualité aujourd'hui

Les mécaniques de base présentées dans cette archive posent des fondations qui demeurent incontournables dans les versions récentes du moteur :

*   **L'Enhanced Input System d'Unreal Engine 5 :** Ce système modulaire basé sur des *Input Actions* et des *Input Mapping Contexts* reste le standard absolu d'Epic Games pour gérer les contrôles multiplateformes (clavier, souris et manette Xbox).
*   **La structure des Blueprints d'acteurs :** La sainte trinité *Viewport / Construction Script / Event Graph* est immuable. Comprendre comment et quand s'exécutent ces fenêtres est la clé de toute programmation visuelle propre.
*   **L'exploitation des Sound Cues :** Même si le moteur Audio s'enrichit constamment, l'utilisation de fichiers *Cue* pour lier, looper et injecter de la logique nodale simple dans vos pistes audio (comme l'application d'atténuations ou de variations) reste une méthode rapide et extrêmement efficace pour le prototypage sonore.

---
{{< footer >}}