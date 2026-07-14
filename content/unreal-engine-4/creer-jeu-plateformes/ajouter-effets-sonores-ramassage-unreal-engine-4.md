---
title: "24. Ajouter des effets sonores lors du ramassage d''objets"
weight: 24
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Blueprints', 'Audio', 'GameDev', 'Tutoriel']
images: ["https://img.youtube.com/vi/AHinfzIpISY/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/AHinfzIpISY/maxresdefault.jpg"]
---

Dans cet épisode, nous allons finaliser l'interaction de ramassage de nos pièces en ajoutant un retour audio immédiat. Au lieu d'un simple changement de score visuel, le joueur bénéficiera d'un feedback sonore spatialisé, renforçant ainsi le "game feel" de notre projet. Nous verrons comment utiliser la position de l'acteur lui-même pour déclencher ce son.

{{< youtube-rgpd "AHinfzIpISY" >}}

### Résumé des étapes clés
*   **Accès au Blueprint :** Ouvrez le Blueprint `ZonePièce` pour modifier la logique existante.
*   **Insertion du nœud :** Entre le `Set Score` et le `Destroy Actor`, insérez un nœud `Play Sound at Location`.
*   **Sélection du son :** Choisissez votre asset audio (ex: "Pièce") dans la bibliothèque.
*   **Spatialisation :** Utilisez le nœud `Get Actor Location` avec la cible `Self` pour que le son soit émis précisément à l'emplacement de la pièce dans le monde.
*   **Compilation et test :** Compilez le Blueprint et testez en jeu pour vérifier que le son se déclenche bien lors de la collision.
*   **Optimisation :** Ajustez les délais (ex: temps d'attente de victoire) pour affiner le rythme de votre jeu.

### Ce qui reste d'actualité aujourd'hui
Bien que les versions d'Unreal Engine aient évolué, les principes fondamentaux abordés ici restent des piliers du développement :
1.  **Le Feedback Audio :** La spatialisation des sons (`Play Sound at Location`) est toujours la méthode standard pour les effets ponctuels (SFX) dans l'UE5.
2.  **La modularité des Blueprints :** La logique d'insertion de nœuds entre deux actions reste la base de la programmation visuelle.
3.  **L'utilisation de 'Self' :** Comprendre que `Self` fait référence à l'instance de l'acteur qui exécute le code est crucial pour éviter les erreurs de positionnement dans des scènes complexes.
4.  **Itération rapide :** La capacité à modifier des variables (comme le temps d'attente de victoire) et à tester immédiatement est le cœur du workflow de développement sur Unreal.

{{< footer >}}