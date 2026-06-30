---
title: "27. Remplacer le personnage par défaut"
weight: 27
date: 2026-06-17
categories: ['Tutoriels Unreal Engine 4']
tags: ['Unreal Engine 4', 'GameDev', 'Animation', 'Retargeting', 'Personnage']
---

Dans cet épisode, nous allons aborder une étape cruciale pour personnaliser votre projet : remplacer le mannequin par défaut (le "Dummy") par votre propre modèle 3D. Que vous ayez créé votre personnage sur un logiciel de modélisation ou via un outil comme Fuse, le processus de remplacement et de "retargeting" des animations reste une compétence fondamentale pour tout développeur Unreal Engine.

{{< youtube-rgpd "Is-zJf2VfL0" >}}

### Résumé des étapes clés
*   **Importation du modèle :** Importez votre fichier `.fbx` en veillant à bien cocher les options de squelette et de maillage.
*   **Configuration du Rig :** Utilisez le *Rig Manager* pour assigner le "Humanoid Rig" à votre nouveau squelette afin qu'il soit compatible avec les animations d'Unreal.
*   **Retargeting des animations :** Dupliquez le *Animation Blueprint* du projet de base et effectuez un "Retarget" vers votre nouveau squelette.
*   **Ajustements manuels :** Utilisez l'option "Recursive Set Translation Retargeting" sur les articulations (clavicules, hanches) pour corriger les déformations des membres.
*   **Intégration dans le Character Blueprint :** Remplacez le mesh par défaut dans votre *Character Blueprint* et assignez le nouvel *Animation Blueprint* pour que votre personnage prenne vie.
*   **Polissage :** Ajustez la position de la caméra dans le viewport pour correspondre à la taille et à la morphologie de votre nouveau modèle.

### Ce qui reste d'actualité aujourd'hui
Bien que les versions d'Unreal Engine aient évolué (notamment avec l'arrivée d'UE5 et de l'IK Rig), les principes fondamentaux expliqués ici restent parfaitement valables :
1.  **La structure des squelettes :** La hiérarchie des os et le besoin d'un rig humanoïde standardisé sont toujours la base du système d'animation.
2.  **Le workflow de Retargeting :** La logique de copier des animations d'un squelette source vers un squelette cible est une compétence qui ne change pas, même si les outils (comme l'IK Retargeter dans UE5) sont devenus plus puissants.
3.  **L'importance du Character Blueprint :** Le remplacement du mesh et la gestion des composants dans le viewport restent la méthode standard pour définir l'apparence du joueur en jeu.
4.  **La correction manuelle :** Savoir ajuster les offsets de translation sur les articulations reste indispensable pour corriger les problèmes de "bras cassés" ou de pieds flottants lors de l'importation de modèles personnalisés.

{{< footer >}}