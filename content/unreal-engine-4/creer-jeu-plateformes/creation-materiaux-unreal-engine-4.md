---
title: "9. Création et application de matériaux"
weight: 9
date: 2026-06-17
categories: ['Tutoriels Unreal Engine 4']
tags: ['Unreal Engine 4', 'Matériaux', 'GameDev', 'Texturing', 'Débutant']
---

Dans cet épisode, nous quittons l'aspect "gris par défaut" de nos objets pour leur donner vie. La création de matériaux est une étape fondamentale pour transformer des formes géométriques simples en éléments crédibles pour votre jeu. Nous allons apprendre à manipuler l'éditeur de matériaux d'Unreal Engine 4 pour définir la couleur, la rugosité et les propriétés métalliques de vos surfaces.

{{< youtube-rgpd "DuPka6B_HNc" >}}

### Résumé de la leçon
*   **Organisation :** Création d'un dossier dédié aux matériaux pour garder votre projet propre.
*   **Nommage :** Utilisation de préfixes (ex: `Mat_`) pour identifier rapidement vos assets.
*   **L'éditeur de matériaux :** Découverte de l'interface nodale, similaire aux Blueprints.
*   **Constant 3 Vector :** Utilisation de ce nœud pour définir une couleur de base via le sélecteur RVB.
*   **Propriétés physiques :**
    *   **Roughness (Rugosité) :** Contrôle le reflet de la lumière (0 = miroir, 1 = mat).
    *   **Metallic (Métallique) :** Définit si l'objet réagit comme un métal (0 = non-métal, 1 = métal).
*   **Application :** Comment assigner un matériau créé à un objet spécifique dans le panneau "Details".

### Ce qui reste d'actualité aujourd'hui
Bien que les versions récentes d'Unreal Engine (UE5) aient introduit des systèmes comme *Lumen* ou *Nanite*, les bases fondamentales présentées ici restent inchangées :
1.  **Le système de nœuds :** La logique de connexion entre les entrées (Base Color, Roughness, Metallic) est le cœur du moteur de rendu d'Unreal.
2.  **Workflow de travail :** La méthodologie de création de dossiers et de nommage reste une bonne pratique indispensable pour tout projet professionnel.
3.  **PBR (Physically Based Rendering) :** Les concepts de rugosité et de metallic sont les piliers du rendu réaliste moderne. Comprendre comment ces valeurs influencent la lumière est toujours la première étape avant de passer à des textures complexes (PBR maps).

{{< footer >}}