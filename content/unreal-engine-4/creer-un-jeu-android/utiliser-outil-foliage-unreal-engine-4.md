---
title: "27. Utiliser l''outil Foliage pour peupler vos environnements"
weight: 27
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Foliage', 'Level Design', 'Optimisation', 'Tutoriel']
---

Dans cet épisode, nous abordons une étape cruciale du level design : l'habillage de votre terrain. Si placer des objets manuellement fonctionne pour quelques éléments, cela devient vite ingérable sur de grandes surfaces. Nous allons découvrir comment utiliser l'outil **Foliage** (feuillage) pour automatiser et optimiser la création de vos forêts et zones végétalisées.

{{< youtube-rgpd "VQl_z_M6088" >}}

### Résumé de l'épisode
*   **Placement manuel vs Foliage :** Pourquoi éviter le placement manuel pour les grandes zones.
*   **Configuration de l'outil Foliage :** Glisser-déposer vos assets (arbres) dans l'éditeur.
*   **Réglages de densité et de taille :** Apprendre à gérer la répartition aléatoire et l'échelle (Scaling uniforme vs libre).
*   **Outils de manipulation :** Utiliser le mode "Select" pour déplacer, supprimer ou ajuster des arbres individuellement ou par groupe (Lasso).
*   **Optimisation des matériaux :** Ajuster les paramètres *Metallic* et *Roughness* pour éviter que vos arbres ne paraissent "plastiques" ou trop brillants sous la lumière.

### Ce qui reste d'actualité aujourd'hui
Bien que les versions d'Unreal Engine aient évolué (notamment avec l'arrivée de *Nanite* et *Lumen* dans l'UE5), les principes fondamentaux présentés ici restent la base du métier :

1.  **Le workflow Foliage :** L'outil Foliage reste l'outil standard pour peindre de la végétation. Il est indispensable pour gérer des milliers d'instances sans surcharger la hiérarchie de votre scène.
2.  **La gestion de la densité :** Comprendre que la densité doit être ajustée en fonction de la taille de vos assets est une règle d'or pour éviter le "bruit visuel".
3.  **L'importance du Material Editor :** Le réglage du *Roughness* reste une étape clé pour intégrer vos assets dans l'éclairage global de votre scène. Un objet trop brillant trahit immédiatement son aspect artificiel.
4.  **L'optimisation :** Même avec des machines puissantes, le contrôle de la densité et du nombre d'instances reste le meilleur moyen de maintenir un framerate stable.

{{< footer >}}