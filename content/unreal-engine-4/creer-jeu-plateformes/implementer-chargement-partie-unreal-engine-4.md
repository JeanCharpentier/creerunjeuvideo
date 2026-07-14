---
title: "49. Implémenter le chargement de partie dans Unreal Engine 4"
weight: 49
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Blueprints', 'SaveGame', 'GameInstance', 'Tutoriel']
images: ["https://img.youtube.com/vi/3uzieUiEco0/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/3uzieUiEco0/maxresdefault.jpg"]
---

Dans cet épisode, nous finalisons notre système de sauvegarde en nous concentrant sur la logique de chargement. Après avoir appris à enregistrer les données, il est crucial de savoir comment les récupérer, les injecter dans la `GameInstance` pour assurer la persistance entre les niveaux, et enfin déclencher le chargement du bon niveau.

{{< youtube-rgpd "3uzieUiEco0" >}}

### Résumé de la procédure de chargement
*   **Load Game from Slot** : Utilisation du nœud pour récupérer les données du fichier de sauvegarde spécifié.
*   **Cast to SaveGame** : Vérification que les données chargées correspondent bien à votre classe `SaveGame` personnalisée.
*   **Récupération des variables** : Extraction du score et du nom du niveau via les fonctions `Get` de votre objet de sauvegarde.
*   **Synchronisation avec la GameInstance** : Injection des données chargées dans la `GameInstance` pour que le joueur puisse les récupérer dès le chargement du niveau.
*   **Open Level** : Utilisation du nom du niveau stocké dans la sauvegarde pour téléporter le joueur au bon endroit.
*   **Bonne pratique** : Utiliser des variables de type `String` pour le nom du slot afin de faciliter la maintenance du code.

### Ce qui reste d'actualité aujourd'hui
Bien que le système de sauvegarde par menu soit une approche classique, les principes fondamentaux abordés ici restent le socle de tout système de persistance dans Unreal Engine :

1.  **La GameInstance comme pont** : La `GameInstance` est l'objet qui survit au changement de niveau. Elle reste l'endroit idéal pour stocker temporairement les données avant qu'elles ne soient appliquées au joueur (Pawn) lors du `BeginPlay` d'un niveau.
2.  **La structure de données** : Le découplage entre l'objet `SaveGame` (qui stocke les données sur le disque) et la `GameInstance` (qui gère l'état du jeu en mémoire) est une architecture propre et robuste.
3.  **Gestion des slots** : L'utilisation de variables pour définir les noms des slots de sauvegarde est une règle d'or pour éviter les erreurs de frappe et faciliter le refactoring de votre projet.
4.  **Limites du Open Level** : Comme mentionné, le changement de niveau (`Open Level`) réinitialise l'état du monde. Comprendre que les données doivent être "poussées" dans la `GameInstance` avant ce changement est essentiel pour éviter la perte d'informations.

{{< footer >}}