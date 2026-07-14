---
title: "5. Création et intégration d''un arbre low-poly"
weight: 5
date: 2026-06-17
categories: ['Tutoriels Unreal Engine 4']
tags: ['Unreal Engine 4', 'Blender', 'Modélisation', 'GameDev', 'Low-poly']
images: ["https://img.youtube.com/vi/KMymcS1f79Y/maxresdefault.jpg"]
---

Dans ce cinquième épisode de notre série dédiée au développement de jeux avec Unreal Engine 4, nous quittons temporairement le moteur pour retourner dans Blender. L'objectif est de créer un élément de décor essentiel : un arbre. Nous verrons comment modéliser un tronc et un feuillage, gérer les collisions (indispensables pour que le joueur ne traverse pas les objets) et importer le tout proprement dans votre projet.

{{< youtube-rgpd "KMymcS1f79Y" >}}

### Résumé du tutoriel
*   **Référence de taille :** Utilisation d'un cube de 2x2x4 mètres dans Blender pour garantir une échelle cohérente avec le personnage dans Unreal Engine.
*   **Modélisation Low-Poly :** Création d'un tronc à partir d'un cylindre (7 vertices) et d'un feuillage via des IcoSphères.
*   **Édition organique :** Utilisation du *Proportional Editing* pour donner une forme naturelle et irrégulière aux éléments.
*   **Gestion des collisions :** Création de maillages simplifiés (nommés avec le préfixe `UCX_`) pour permettre à Unreal Engine de générer des collisions optimisées.
*   **Matériaux :** Création de slots de matériaux dans Blender, puis configuration des *Material Instances* dans Unreal Engine pour appliquer les couleurs.
*   **Importation :** Paramétrage de l'importateur FBX (désactivation de l'import automatique des matériaux/textures pour un meilleur contrôle).

### Ce qui reste d'actualité aujourd'hui
Bien que les versions d'Unreal Engine aient évolué, les fondamentaux abordés ici restent des piliers du développement 3D :
1.  **L'importance du "Blockout" :** Utiliser des objets de référence pour définir l'échelle dès le début du processus de modélisation est une pratique indispensable pour éviter les problèmes de proportion une fois en jeu.
2.  **Optimisation des collisions :** La méthode `UCX_` (Unreal Collision) reste la norme pour créer des collisions personnalisées et performantes. Utiliser des formes géométriques simples pour les collisions est toujours préférable pour économiser les ressources CPU.
3.  **Workflow Blender vers UE4 :** La séparation entre la modélisation (Blender) et le shading (Unreal Engine) est une approche professionnelle qui permet une plus grande flexibilité, notamment pour ajuster les couleurs ou les propriétés physiques des matériaux directement dans le moteur sans avoir à réexporter le modèle 3D.
4.  **Low-poly :** Le style low-poly est intemporel, non seulement pour son esthétique, mais aussi pour sa légèreté, ce qui facilite grandement le développement pour les plateformes mobiles ou les projets indépendants.

{{< footer >}}