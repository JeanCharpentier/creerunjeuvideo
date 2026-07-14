---
title: "8. Utiliser le Foliage Editor dans Unreal Engine 4"
weight: 8
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Tutoriel', 'Foliage', 'Level Design', 'Optimisation']
images: ["https://img.youtube.com/vi/xzFFtah_n5w/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/xzFFtah_n5w/maxresdefault.jpg"]
---

Dans ce tutoriel, nous allons découvrir comment optimiser drastiquement votre workflow de level design en utilisant l'outil **Foliage Editor** intégré à Unreal Engine 4. Si vous avez l'habitude de placer vos arbres, rochers ou herbes un par un à la main, cet outil va littéralement changer votre façon de travailler.

{{< youtube-rgpd "xzFFtah_n5w" >}}

### Résumé du tutoriel
*   **Accès rapide :** Utilisez le raccourci `Shift + 4` pour ouvrir le mode Foliage.
*   **Principe de brosse :** Le Foliage Editor fonctionne comme un outil de peinture. Vous sélectionnez vos assets (arbres, herbes, cailloux), vous réglez la taille de la brosse et la densité, puis vous "peignez" votre terrain.
*   **Aléatoire automatique :** L'outil gère nativement la variation de taille, de rotation et de position de vos objets, rendant votre environnement beaucoup plus naturel.
*   **Gestion des pivots :** Attention à vos assets ! Si vos objets apparaissent sous le sol, vérifiez le point de pivot de votre modèle 3D (FBX) et réimportez-le si nécessaire.
*   **Workflow hybride :** Utilisez le Foliage Editor pour la végétation dense (herbe, petits arbres) et placez manuellement les éléments de gameplay ou les objets uniques (feux de camp, barrières) pour garder un contrôle total sur la jouabilité.
*   **Sauvegarde :** N'oubliez jamais de faire des `Ctrl + S` réguliers, surtout après avoir généré des milliers d'instances.

### Ce qui reste d'actualité aujourd'hui
Bien que les versions récentes d'Unreal Engine (UE5) aient introduit le système *PCG (Procedural Content Generation)* et les *Packed Level Actors*, le **Foliage Editor** reste un outil fondamental et extrêmement performant pour les tâches de level design rapide.
*   **Performance :** Le système d'instanciation utilisé par le Foliage Editor est toujours la méthode privilégiée pour afficher des milliers d'objets identiques sans saturer le moteur.
*   **Simplicité :** Pour des besoins de décoration rapide ou de remplissage de zones forestières, il reste bien plus accessible et rapide à configurer que des systèmes procéduraux complexes.
*   **Compatibilité :** Les principes de base (densité, taille de brosse, gestion des collisions) sont identiques dans toutes les versions d'Unreal Engine, ce qui en fait une compétence indispensable pour tout développeur.

{{< footer >}}