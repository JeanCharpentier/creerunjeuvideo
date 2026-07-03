---
title: "10. Créer un monde infini et ajouter des décors"
weight: 10
date: 2023-10-27
categories: ['Tutoriels']
tags: ['GDevelop', 'Survival', 'GameDev', 'TiledBackground']
---

Dans cet avant-dernier épisode de notre série sur la création d'un jeu de type *Survival*, nous allons nous attaquer à deux problématiques majeures pour donner vie à votre monde : la création d'un sol infini et l'ajout de décors procéduraux. L'objectif est de rendre votre environnement moins répétitif tout en optimisant les performances pour que votre map semble ne jamais s'arrêter.

{{< youtube-rgpd "9SAQK1m3HjE" >}}

### Ce que nous avons appris dans cet épisode :

*   **Gestion du sol infini :** Utilisation d'un objet *Tiled Background* (Mosaïque) dont on modifie le décalage (offset) en fonction de la position de la caméra pour créer une illusion de mouvement infini.
*   **Z-Order :** Organisation de la profondeur des objets pour que le sol reste toujours en arrière-plan (Z = -50) et que les décors s'affichent correctement.
*   **Spawn aléatoire de décors :** Création d'un groupe d'objets "décor" et utilisation d'une variable de scène (`decor_random`) pour faire apparaître des éléments variés (crânes, colonnes, fontaines) autour du joueur.
*   **Optimisation des performances :** Mise en place d'une boucle "Pour chaque objet" qui supprime automatiquement les décors trop éloignés du joueur (distance > 1500 pixels) afin de ne pas surcharger la mémoire.
*   **Préparation au debug :** Identification du problème d'apparition des objets dans le champ de vision du joueur, qui sera corrigé dans la vidéo finale.

### Ce qui reste d'actualité aujourd'hui

*   **L'utilisation des Tiled Backgrounds :** C'est toujours la méthode la plus efficace dans GDevelop pour créer des sols ou des ciels qui se répètent sans consommer trop de ressources.
*   **La logique de "Cleanup" :** Supprimer les objets hors champ est une règle d'or en GameDev. Que ce soit pour des décors ou des ennemis, ne jamais laisser des instances s'accumuler inutilement est crucial pour maintenir un framerate stable.
*   **Le système de nommage dynamique :** La technique consistant à créer des objets par leur nom (`"decor" + VariableString(decor_random)`) reste une astuce très puissante pour éviter des dizaines d'événements conditionnels ("Si variable = 1, créer décor 1...").
*   **La structure des projets :** L'importance de bien organiser ses événements en groupes (spawner, gestion du sol, etc.) facilite grandement la maintenance et le débogage de votre jeu.

{{< footer >}}