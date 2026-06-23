---
title: "35. Déployer votre version Alpha sur la Google Play Console"
weight: 35
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Android', 'Google Play', 'Déploiement', 'Mobile', 'Tutoriel']
---

Dans cet épisode, nous franchissons une étape cruciale de votre projet : le déploiement de votre build Alpha sur la Google Play Console. Préparer son jeu pour la distribution mobile demande de la rigueur, notamment dans la gestion des fichiers APK/OBB et la conformité aux exigences de Google.

{{< youtube-rgpd "" >}}

### Résumé des étapes de déploiement
*   **Configuration de la signature :** Désactivation de la signature automatique par Google Play pour privilégier la gestion via les outils du GDK.
*   **Upload des fichiers :** Chargement de l'APK et du fichier d'extension OBB (Main) générés lors de l'export Android.
*   **Gestion des versions :** Importance de l'incrémentation du `StoreVersion` dans les paramètres du projet pour éviter les conflits de mise à jour.
*   **Notes de version :** Rédaction des modifications (changelog) pour informer les testeurs des nouveautés ou correctifs.
*   **Classification du contenu :** Remplissage rigoureux du questionnaire de classification (PEGI/ESRB) pour éviter toute suspension du compte développeur.
*   **Tarifs et disponibilité :** Configuration de la gratuité, sélection des pays de diffusion et déclaration de la présence d'annonces publicitaires.

### Ce qui reste d'actualité aujourd'hui
Bien que les outils de Google Play Console évoluent régulièrement, les fondamentaux abordés ici restent indispensables :
1.  **Le Versioning :** L'incrémentation du code de version (`StoreVersion`) est une règle immuable sur le Play Store. Sans cela, impossible de publier une mise à jour.
2.  **La conformité :** Le questionnaire de classification est toujours aussi critique. Google est extrêmement strict sur la véracité des informations fournies (violence, contenu pour adultes, etc.).
3.  **Les fichiers OBB :** Bien que les *Android App Bundles* (.aab) soient désormais la norme imposée par Google pour remplacer les APK, la logique de gestion des fichiers d'extension reste pertinente pour les projets Unreal Engine de grande taille.
4.  **La prudence juridique :** La lecture des conditions d'exportation et des règles de contenu est toujours la meilleure protection contre le bannissement de votre application.

{{< footer >}}