---
title: "15. Intégrer un personnage MakeHuman"
weight: 15
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Tutoriel', 'MakeHuman', 'Animation', 'Retargeting', 'GameDev']
images: ["https://img.youtube.com/vi/h1wmjbMYCD4/maxresdefault.jpg"]
---

Dans cet épisode, nous abordons une étape cruciale pour tout développeur solo : l'importation d'un personnage personnalisé dans Unreal Engine 4. Après de nombreuses heures de recherche et de tests, j'ai réussi à intégrer un modèle généré via **MakeHuman** (version 1.1.0) et à le faire fonctionner avec le système d'animation par défaut d'Unreal Engine.

{{< youtube-rgpd "h1wmjbMYCD4" >}}

### Résumé du tutoriel
*   **Préparation dans MakeHuman :** Utilisation de la version 1.1.0, réglage des paramètres morphologiques pour un look "Slender", et surtout, sélection du squelette **"Game Engine"** pour assurer la compatibilité avec Unreal.
*   **Exportation :** Configuration du format FBX (unités en centimètres, désactivation du binaire) pour une intégration propre.
*   **Importation dans UE4 :** Configuration des paramètres d'import pour inclure les textures et matériaux.
*   **Retargeting des animations :** Utilisation du *Retarget Manager* pour lier le squelette de notre personnage au rig humanoïde d'Unreal, permettant ainsi d'utiliser les animations natives (Idle, Walk, Run, Jump).
*   **Ajustements :** Correction des problèmes de posture (mains, jambes) via le mode "Edit Pose" et personnalisation des matériaux (yeux).

### Ce qui reste d'actualité aujourd'hui
Bien que les versions des logiciels aient évolué, les fondamentaux abordés dans cette vidéo restent des piliers du développement de jeux :
1.  **Le workflow de retargeting :** La logique de faire correspondre un squelette personnalisé à un rig standard (comme celui d'Unreal) est toujours la méthode la plus efficace pour gagner du temps sur l'animation.
2.  **L'importance du squelette "Game Engine" :** Choisir un rig compatible dès l'exportation évite des heures de débuggage manuel dans Blender ou Maya.
3.  **La gestion des matériaux :** La manipulation des *Material Instances* et des paramètres vectoriels reste la base pour donner une identité visuelle unique à vos personnages sans avoir à refaire toutes les textures.
4.  **Le debug de collision :** Les problèmes de collision rencontrés lors de l'intégration sont des défis classiques qui nécessitent toujours une attention particulière sur les *Physics Assets*.

{{< footer >}}