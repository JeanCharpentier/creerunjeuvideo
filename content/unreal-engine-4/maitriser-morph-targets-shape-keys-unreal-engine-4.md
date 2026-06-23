---
title: "Maîtriser les Morph Targets (Shape Keys) dans Unreal Engine 4"
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Blender', 'Animation', 'Morph Targets', 'Shape Keys', 'Tutoriel']
---

Dans cet article, nous explorons comment créer des déformations complexes sur vos modèles 3D en utilisant les **Shape Keys** de Blender, pour ensuite les animer dans **Unreal Engine 4** via les **Morph Targets**. Cette technique est idéale pour les expressions faciales, les transformations d'objets ou les animations organiques.

{{< youtube-rgpd "4qXonFMoogQ" >}}

### Résumé du processus
*   **Blender (Shape Keys) :** Création de la forme de base (*Basis*) et des variantes de formes (*Key 1, Key 2...*). Utilisation du mode *Object* pour définir les clés et du mode *Edit* pour sculpter les déformations.
*   **Exportation :** Export au format FBX en s'assurant de bien sélectionner l'objet.
*   **Importation Unreal Engine :** Import en tant que *Skeletal Mesh* (même sans squelette). Il est crucial de cocher l'option *Import Morph Targets* dans les paramètres d'importation.
*   **Implémentation :** Utilisation d'une *Timeline* dans le *Blueprint* de l'acteur pour piloter la valeur (de 0 à 1) de la *Morph Target* via le nœud `Set Morph Target`.
*   **Matériaux :** Ne pas oublier de cocher l'option **"Use With Morph Targets"** dans les détails du matériau pour éviter les artefacts visuels lors de la déformation.

### Ce qui reste d'actualité aujourd'hui

Bien que cet article se base sur une version spécifique d'Unreal Engine 4 (la 4.19), les principes fondamentaux restent parfaitement valables pour les versions actuelles d'Unreal Engine 5 :

1.  **Compatibilité des formats :** Le workflow Blender vers Unreal via FBX reste le standard industriel pour le transfert de données de maillage avec morphing.
2.  **Gestion des noms :** La nomenclature est toujours capitale. Unreal Engine identifie les *Morph Targets* par leur nom exact défini dans Blender ; toute erreur de casse ou d'orthographe empêchera l'animation de fonctionner.
3.  **Performance :** Les *Morph Targets* sont toujours une solution très performante pour des animations locales sans avoir besoin de créer des chaînes d'os complexes (rigging).
4.  **Le piège du Material :** L'option "Use With Morph Targets" dans l'éditeur de matériaux est une étape souvent oubliée qui reste nécessaire pour que le shader calcule correctement les normales lors de la déformation du mesh.
5.  **Stabilité :** Le bug de "scintillement" (flickering) mentionné dans la vidéo était spécifique aux versions 4.17/4.18. Aujourd'hui, les versions modernes d'Unreal gèrent nativement et de manière stable les *Morph Targets* complexes.

{{< footer >}}