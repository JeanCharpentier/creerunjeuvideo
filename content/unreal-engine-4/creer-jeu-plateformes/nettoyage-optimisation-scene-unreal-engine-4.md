---
title: "7. Nettoyage et optimisation de votre scène dans Unreal Engine 4"
weight: 7
date: 2026-06-17
categories: ['Développement de jeux']
tags: ['Unreal Engine 4', 'Workflow', 'Optimisation', 'Level Design']
---

Dans cet épisode, nous abordons une étape cruciale du développement : le nettoyage de votre environnement de travail. Avant de commencer à construire votre niveau final, il est essentiel de supprimer les éléments de test, les prototypes et les objets inutiles qui encombrent votre *World Outliner* et alourdissent inutilement votre scène.

{{< youtube-rgpd "ZgfPNlYCWPs" >}}

### Résumé des étapes de nettoyage
*   **Utilisation du World Outliner :** Apprenez à naviguer dans votre hiérarchie pour identifier et supprimer les éléments de test (murs, escaliers, formes géométriques de base).
*   **Suppression propre :** Nettoyage des dossiers obsolètes (ex: *World Coway*) et des acteurs de template (ex: *FirstPersonCharacter*).
*   **Gestion des ombres :** Comprendre pourquoi des ombres persistent après la suppression d'un objet et comment les corriger.
*   **Reconstruction de l'éclairage :** Utilisation de l'outil *Build Lighting Only* pour mettre à jour le rendu de la scène après les modifications.
*   **Bonnes pratiques de sauvegarde :** Utiliser le raccourci `Ctrl + S` pour sauvegarder l'intégralité du projet plutôt que de se limiter à la scène active.

### Ce qui reste d'actualité aujourd'hui
Bien que cet article se concentre sur Unreal Engine 4, les principes fondamentaux restent identiques dans les versions plus récentes (UE5) :

1.  **Organisation du World Outliner :** Garder une hiérarchie propre est indispensable pour éviter de se perdre dans des projets complexes. L'utilisation de dossiers et d'une nomenclature claire est une règle d'or.
2.  **Gestion des ressources :** Supprimer les objets inutilisés n'est pas seulement une question de visibilité, c'est aussi une question de performance. Chaque acteur présent dans la scène consomme des ressources de calcul.
3.  **Le cycle "Build" :** Le processus de *Lightmass* (ou *Lumen* dans UE5) nécessite toujours une mise à jour après des changements structurels majeurs pour éviter les artefacts visuels.
4.  **Sauvegarde systématique :** La discipline de sauvegarde est universelle. Ne comptez pas uniquement sur l'auto-save ; prenez l'habitude de sauvegarder manuellement vos changements pour éviter toute perte de données lors d'un crash.

{{< footer >}}