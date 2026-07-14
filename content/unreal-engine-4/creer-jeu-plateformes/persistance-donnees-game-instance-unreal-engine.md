---
title: "46. Persistance des données entre les niveaux avec la Game Instance"
weight: 46
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Blueprint', 'Game Instance', 'Développement', 'Tutoriel']
images: ["https://img.youtube.com/vi/c9dJzeapnjM/maxresdefault.jpg"]
---

Dans cet épisode, nous abordons une problématique classique du développement de jeux vidéo : comment conserver des informations (comme le score du joueur) lorsqu'on change de niveau. Par défaut, Unreal Engine réinitialise les variables de votre personnage à chaque chargement de map. Pour pallier cela, nous allons utiliser la **Game Instance**.

{{< youtube-rgpd "c9dJzeapnjM" >}}

### Résumé du fonctionnement
La Game Instance est un objet global qui survit au changement de niveau. Voici les étapes clés pour mettre en place votre système de score persistant :

*   **Création :** Créez une nouvelle classe Blueprint basée sur `GameInstance` et nommez-la `MyGameInstance`.
*   **Configuration :** Allez dans *Edit > Project Settings > Maps & Modes* et assignez votre `MyGameInstance` dans la section *Game Instance Class*.
*   **Stockage :** Lors du passage à un nouveau niveau (via votre zone de collision), utilisez un `Cast To MyGameInstance` pour transférer le score actuel du joueur vers une variable de la Game Instance.
*   **Récupération :** Au `BeginPlay` du niveau suivant, effectuez à nouveau un `Cast` vers la Game Instance pour récupérer la valeur stockée et mettre à jour le score du joueur.
*   **Cycle de vie :** Le score transite du Joueur vers la Game Instance avant le changement de map, puis de la Game Instance vers le Joueur au démarrage du nouveau niveau.

### Ce qui reste d'actualité aujourd'hui
Bien que cet épisode soit basé sur Unreal Engine 4, les concepts fondamentaux restent identiques dans Unreal Engine 5 :

1.  **La Game Instance est toujours la solution privilégiée** pour les données temporaires qui doivent survivre au chargement de niveaux (score, état de santé, inventaire temporaire).
2.  **Le "Cast" reste une méthode standard** pour communiquer entre les classes, bien qu'il soit conseillé d'utiliser des *Interfaces* pour des projets plus complexes afin de réduire les dépendances.
3.  **La limite de la Game Instance :** Comme mentionné, elle est réinitialisée à la fermeture du jeu. Pour une persistance à long terme, il faudra toujours coupler ce système avec le **SaveGame** (système de sauvegarde sur disque), qui sera le sujet de notre prochaine leçon.

{{< footer >}}