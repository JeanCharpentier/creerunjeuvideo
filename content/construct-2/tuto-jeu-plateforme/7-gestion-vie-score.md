---
title: "7. Système de vie et gestion des scores"
date: 2026-06-13
weight: 9
categories: ["Archive"]
tags: ["Construct 2", "Game Dev", "Tutoriel", "Score", "Variables"]
prev_url: "/construct-2/tuto-jeu-plateforme/correctif-animation-atterrissage"
next_url: "/construct-2/tuto-jeu-plateforme/8-systeme-score-web-storage"
images: ["https://img.youtube.com/vi/UGUg7gjT6JQ/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/UGUg7gjT6JQ/maxresdefault.jpg"]
---

> **Note :** Cet article est une archive pédagogique du septième épisode de ma série sur la création d'un jeu de plateforme avec Construct 2.

{{< youtube-rgpd "UGUg7gjT6JQ" >}}

### Points clés abordés

* **Variables globales :** Utilisation de variables pour suivre l'état du joueur (`Score` et `Vie`).
* **Gestion des pièces :** * Détection de collision entre le joueur et l'objet `Pièce`.
    * Destruction de la pièce après contact.
    * Incrémentation de la variable globale `Score` et mise à jour de l'affichage textuel (HUD).
* **IA d'ennemi et dégâts :**
    * Système de "double collision" : saut sur l'ennemi (destruction) vs contact latéral (perte de vie).
    * Soustraction d'une valeur à la variable `Vie` lors d'un contact non létal.
* **Condition de défaite (Game Over) :** Vérification de la valeur de la variable `Vie` après chaque impact. Si `Vie <= 0`, déclenchement de l'action `Restart Layout`.

### Logique des variables dans Construct 2

La gestion des données est au cœur de cet épisode. Voici la structure logique recommandée pour vos événements :

1. **Incrémentation (Score) :**
   * Événement : `Joueur > On collision with Pièce`
   * Action : `Système > Add to Score (ex: +10)`
   * Action : `HUD_TexteScore > Set text` à `"Score : " & Score`

2. **Décrémentation (Vie) :**
   * Événement : `Joueur > On collision with Ennemi` (seulement si contact latéral)
   * Action : `Système > Subtract from Vie (1)`
   * Action : `Vérification : Si Vie <= 0 alors Restart Layout`

### Conseils d'optimisation
* **Modularité :** En utilisant des variables globales, vous permettez au score de persister entre différents layouts si vous le souhaitez.
* **HUD dynamique :** Assurez-vous que vos objets texte sont rafraîchis à chaque modification de variable pour que l'interface soit toujours synchronisée avec l'état réel du jeu.
* **Feedback visuel :** N'hésitez pas à ajouter une petite animation ou un son lors de la collecte des pièces pour renforcer le ressenti (game feel) du joueur.

{{< footer >}}