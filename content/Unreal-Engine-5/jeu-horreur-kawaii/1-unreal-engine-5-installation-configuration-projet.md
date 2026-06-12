---
title: "1. Introduction et Configuration d'Unreal Engine 5"
date: 2026-06-12
category: Archive
weight: 1
tags: [Unreal Engine 5, Kawaii Slender, Blueprint, Epic Games Store, Fab, Game Design, Tutoriel]
prev_url: "/unreal-engine-5/jeu-horreur-kawaii/"
next_url: "/unreal-engine-5/jeu-horreur-kawaii/2-integration-camera-premiere-personne-fps"
---

{{< youtube-rgpd "FylK-jqhq4c" >}}

---

## Résumé des notions clés

Dans cette vidéo d'introduction, nous posons les bases méthodologiques et techniques pour concevoir un prototype de *survival horror* (style Slenderman) baptisé **Kawaii Slender**. L'accent est mis sur la compréhension théorique des choix de développement plutôt que sur le simple copier-coller.

*   **Philosophie de développement :** Privilégier l'apprentissage conceptuel et l'autonomie pour être capable de concevoir ses propres prototypes de jeux, plutôt que de suivre une exécution mécanique.
*   **Mise en place de l'environnement :**
    *   Création et utilisation d'un compte neuf sur l'**Epic Games Launcher**.
    *   Installation d'une version stable d'**Unreal Engine 5** ($5.6.1$).
    *   Gestion de l'organisation des projets (personnalisation de l'icône de projet via le répertoire local).
*   **Création du projet et Template :**
    *   Sélection du **First Person Template** (déplacements de base, caméra, sauts et collisions pré-intégrés).
    *   Choix exclusif du système **Blueprint** (programmation visuelle sans C++).
    *   Sélection d'une variante vierge pour programmer soi-même les mécaniques fondamentales (comme le sprint et la gestion d'interface).
*   **Découverte de l'interface d'UE5 :**
    *   **Éditeur de niveau (Viewport) :** Manipulation des objets dans l'espace à l'aide des *Gizmos* (axes $X, Y, Z$ pour le déplacement, la rotation et l'échelle). raccourci de boucle de transformation avec la touche `Espace`.
    *   **Organiseur (Outliner) :** Gestion exclusive des objets présents dans la scène active (Static Meshes, lumières, dossiers d'organisation).
    *   **Paramètres du monde :** Introduction aux règles globales du niveau (gravité, *Kill Z* pour gérer la chute du joueur hors de la carte).
    *   **Panneau Détails :** Ajustement précis des variables et des coordonnées des composants sélectionnés.
    *   **Tiroir à contenu (Content Browser) :** Gestion globale de l'ensemble des fichiers du projet (sons, textures, blueprints), accessible via le raccourci `Ctrl + Espace`.
*   **Sourcing d'Assets gratuits sur Unreal Fab :**
    *   Recherche et importation de ressources $100\%$ gratuites (Packs d'environnement *Stylized Nature*, modèles d'animaux Low-Poly, musiques d'ambiance d'horreur et sons FX).
    *   Gestion de la compatibilité des versions d'assets antérieures ($5.5, 5.4$ ou $4.27$) lors de l'intégration dans un projet UE $5.6.1$.
    *   Sensibilisation aux licences (Licence Personnelle vs Licence Professionnelle Epic Games).

---

## Ce qui reste d'actualité aujourd'hui

Même si les versions du moteur graphique évoluent, les piliers fondamentaux présentés dans ce tutoriel restent indispensables pour tout développeur de jeux vidéo :

*   **Les bases de la navigation 3D :** L'usage des trois axes de transformation ($X$, $Y$, $Z$), les raccourcis de manipulation et la distinction cruciale entre l'**Outliner** (les objets chargés en scène) et le **Content Browser** (la base de données du projet) n'ont pas changé.
*   **Le prototypage par Template :** Commencer à partir d'une base saine comme le *First Person Template* pour économiser du temps sur le code des déplacements de base reste la norme absolue dans l'industrie pour créer un *Greyboxing* ou une preuve de concept (PoC).
*   **L'écosystème Fab :** La boutique unifiée d'Epic Games demeure la plaque tournante essentielle pour récupérer des *assets* et enrichir rapidement l'ambiance visuelle et sonore d'un prototype à moindres frais, notamment grâce aux contenus gratuits mis à la une chaque mois.

{{< footer >}}