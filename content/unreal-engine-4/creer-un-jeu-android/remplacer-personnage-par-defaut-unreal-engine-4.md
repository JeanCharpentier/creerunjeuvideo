---
title: "29. Remplacer le personnage par défaut dans Unreal Engine 4"
weight: 29
date: 2026-06-17
categories: ['Développement de jeu']
tags: ['Unreal Engine 4', 'Character Design', 'Animation', 'Tutoriel']
---

Dans cet épisode, nous abordons une étape cruciale pour personnaliser votre projet : le remplacement du mannequin par défaut d'Unreal Engine 4 par un modèle personnalisé. Que vous choisissiez un personnage masculin ou féminin, l'objectif est d'intégrer votre propre asset tout en conservant la compatibilité avec le système d'animation existant.

{{< youtube-rgpd "" >}}

### Résumé de l'épisode
*   **Importation des assets :** Création d'un dossier dédié, importation du fichier FBX (mesh + squelette) en utilisant le squelette par défaut (`SK_Mannequin`).
*   **Configuration de l'import :** Activation des options `Import Mesh` et `Skeletal Mesh`, tout en s'assurant que les textures et matériaux sont bien importés.
*   **Intégration au Blueprint :** Remplacement du mesh dans le `ThirdPersonCharacter` via le panneau `Details`.
*   **Correction des proportions (Retargeting) :** Ajustement de la taille du personnage via les options de "Retargeting" dans l'éditeur de squelette pour éviter l'effet de déformation (personnage étiré).
*   **Optimisation :** Utilisation de la fonction `Recursively Set Translation Retargeting` pour appliquer rapidement les réglages à tous les os du squelette.

### Ce qui reste d'actualité aujourd'hui
Bien que cet article se concentre sur Unreal Engine 4, les principes fondamentaux restent identiques dans les versions plus récentes (UE5) :
1.  **Gestion des dossiers :** Une organisation rigoureuse des assets (textures, meshes, blueprints) dès le début du projet est une règle d'or pour éviter la dette technique.
2.  **Squelette partagé :** L'utilisation du squelette par défaut d'Unreal permet de réutiliser instantanément tout le pack d'animations du moteur, ce qui fait gagner un temps précieux aux développeurs indépendants.
3.  **Retargeting :** La compréhension du *Translation Retargeting* reste indispensable pour intégrer des modèles tiers sans avoir à refaire manuellement chaque animation.
4.  **LODs (Level of Detail) :** Bien que non détaillés dans ce cours, les LODs restent essentiels pour maintenir les performances sur mobile (Android), surtout pour des modèles haute définition.

{{< footer >}}