---
title: "20. Créer une quête de type FedEx"
weight: 20
prev_url: "/intersect-engine/creer-un-mmorpg/creer-sort-projectile-intersect-engine/"
next_url: "/intersect-engine/creer-un-mmorpg/gestion-droits-administration-moderation-intersect-engine/"
date: 2024-05-22
categories: ['Archive']
tags: ['Intersect Engine', 'Game Development', 'MMORPG', 'Tutoriel', 'Scripting']
---

Apprendre à manipuler le système d'événements est une étape cruciale pour donner vie à votre MMORPG. Aujourd'hui, nous explorons comment créer une quête de type "FedEx" (livraison d'objet) en utilisant les outils de base d'Intersect Engine.

{{< youtube-rgpd "jf3-ILiL2tQ" >}}

### Résumé des notions clés

Pour mettre en place ce système de quête simple, voici les étapes fondamentales à suivre dans l'éditeur :

*   **Gestion des Variables (Switches) :** Utilisation des *Player Switches* dans le "Switch & Variable Editor" pour suivre l'état d'avancement de la quête (vrai/faux).
*   **Création des NPCs (Événements) :**
    *   **NPC Donneur :** Utilisation d'une condition (`Conditional Branch`) pour vérifier si la quête est active. Si non, on donne l'objet au joueur et on bascule le switch sur "True".
    *   **NPC Récepteur :** Vérification du switch sur "True". Si le joueur possède l'objet, on le lui retire (`Take Item`), on lui octroie de l'expérience, et on réinitialise le switch pour permettre la répétition ou la fin de la quête.
*   **Logique de contrôle :**
    *   Utilisation du `Logic Flow` pour gérer les embranchements conditionnels.
    *   Gestion des inventaires pleins via les retours de commandes `Give/Take Item`.
    *   Affichage de dialogues contextuels avec la commande `Show Text`.

### Ce qui reste d'actualité aujourd'hui

Bien que les versions d'Intersect Engine aient évolué, les principes fondamentaux présentés ici restent le socle de tout développement sur ce moteur :

1.  **La puissance des Switches :** Le système de variables booléennes reste la méthode la plus fiable pour gérer la progression des joueurs dans une quête ou un scénario.
2.  **L'Event Editor :** La structure par "Trigger" (Action Button) et par "Commandes" (Logic Flow) est toujours le cœur battant de l'interactivité dans Intersect. Comprendre comment imbriquer des conditions est indispensable pour créer des quêtes complexes.
3.  **L'importance de la planification :** Comme souligné dans le tutoriel, la structure de vos quêtes doit être pensée en amont sur papier. La gestion des états (quand donner l'objet, quand le retirer, quand réinitialiser la quête) est ce qui différencie un monde vivant d'un monde statique.
4.  **Modularité :** La méthode consistant à créer des petits systèmes isolés (NPC donneur, NPC récepteur) permet de tester facilement vos fonctionnalités avant de les intégrer dans une boucle de jeu plus vaste.

{{< footer >}}