---
title: "14. Création de chemins de plateformes"
weight: 14
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Level Design', 'Infinity Blade', 'Platforming', 'Workflow']
---

Dans cet épisode, nous abordons une étape cruciale du level design : la création d'un chemin de plateformes cohérent pour guider le joueur à travers votre environnement. En utilisant les assets du pack *Infinity Blade: Ice Lands*, nous allons transformer des piliers statiques en un parcours de plateforme dynamique et jouable.

{{< youtube-rgpd "wuoWYSpMB1Q" >}}

### Résumé de l'épisode
*   **Sélection des assets :** Utilisation des modèles `SM_Ice_Fort_Pilar` issus du pack *Infinity Blade* pour créer des points d'appui.
*   **Manipulation et Scale :** Ajustement des échelles (Scale) des objets pour les rendre plus accessibles et adaptés à la taille du personnage.
*   **Organisation du projet :** Utilisation du *World Outliner* pour créer des dossiers et maintenir une hiérarchie propre dans votre scène.
*   **Duplication efficace :** Utilisation du raccourci `Ctrl + W` pour dupliquer rapidement les éléments et construire le chemin.
*   **Itération et Test :** Importance de tester régulièrement les sauts en jeu pour ajuster la distance entre les plateformes et éviter les raccourcis non désirés par le joueur.

### Ce qui reste d'actualité aujourd'hui
Bien que cet épisode se concentre sur Unreal Engine 4, les principes fondamentaux du level design restent identiques dans les versions plus récentes (UE5) :

1.  **Le "Greyboxing" (ou prototypage) :** Même avec des assets finaux, la méthode consistant à placer des objets, tester le gameplay, puis ajuster, est la base de tout bon niveau.
2.  **Gestion de l'Outliner :** L'organisation par dossiers est une bonne pratique indispensable dès que votre scène commence à comporter plus d'une dizaine d'objets.
3.  **Le "Player Feel" :** Le réglage de la distance entre les plateformes doit toujours être dicté par les capacités de mouvement de votre personnage (vitesse, hauteur de saut, *Air Control*).
4.  **Réutilisation des assets :** Apprendre à varier l'échelle et la rotation d'un même asset permet de créer une grande diversité visuelle sans surcharger la mémoire de votre projet.

{{< footer >}}