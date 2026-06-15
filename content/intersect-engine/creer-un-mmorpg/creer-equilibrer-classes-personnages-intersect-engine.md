---
title: "8. Créer et équilibrer vos classes de personnages"
weight: 8
prev_url: "/intersect-engine/creer-un-mmorpg/creer-lier-cartes-intersect-engine/"
next_url: "/intersect-engine/creer-un-mmorpg/optimiser-ressources-graphiques-decouper-sprites-intersect-engine/"
date: 2024-05-22
categories: ['Archive']
tags: ['Intersect Engine', 'Game Development', 'MMORPG', 'Tutoriel']
---

La création des classes de personnages est une étape fondamentale dans le développement de votre MMORPG avec Intersect Engine, car elle pose les bases de l'identité de jeu et de l'équilibrage global.

{{< youtube-rgpd "yopdeVwoURw" >}}

### Résumé des notions clés

La création de classes dans Intersect Engine se déroule au sein du **Content Editor**. Voici les points essentiels à retenir pour configurer vos archétypes :

*   **Gestion des Sprites et du Genre :** Vous pouvez définir des apparences distinctes pour les personnages masculins et féminins. Les ressources graphiques se trouvent dans le dossier `Client & Editor/Resources/Entities`.
*   **Point d'apparition (Spawn Point) :** Utilisez l'outil "Open Visual Interface" pour sélectionner précisément la case (coordonnées X, Y) sur la carte où chaque classe débutera son aventure.
*   **Statistiques de base :** Définissez les PV, la Mana, l'Armure et la vitesse de déplacement. Ces valeurs doivent être cohérentes avec le rôle de la classe (ex: un Guerrier aura plus de PV, un Mage plus de Mana).
*   **Progression et Équilibrage :**
    *   **Expérience :** Configurez le coût en points d'expérience pour monter de niveau et le multiplicateur de difficulté pour les paliers suivants.
    *   **Bonus de niveau :** Choisissez entre des bonus statiques ou en pourcentage pour chaque statistique gagnée lors d'un gain de niveau.
*   **Régénération :** Paramétrez la vitesse de récupération naturelle des points de vie et de mana, un élément crucial pour le confort de jeu.

### Ce qui reste d'actualité aujourd'hui

Bien que les versions d'Intersect Engine évoluent, la logique de structuration des données reste identique. La gestion des classes demeure le "cœur" de votre jeu :
1.  **L'interdépendance des systèmes :** Comme expliqué, il est préférable de définir vos classes avant de créer les objets (items) ou les sorts, car ces derniers dépendent souvent des prérequis de classe.
2.  **La cohérence des statistiques :** L'importance de l'équilibrage mathématique entre les classes (Tank vs DPS vs Support) est une constante dans le développement de MMORPG.
3.  **Extensibilité :** Le moteur permet toujours d'ajouter des feuilles de sprites personnalisées, à condition de respecter le format d'animation standard du moteur, ce qui garantit une grande liberté artistique.

{{< footer >}}