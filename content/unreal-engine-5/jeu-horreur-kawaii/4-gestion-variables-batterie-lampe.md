---
title: "4. Gestion d'une batterie et cycle de rechargement automatique"
date: 2026-06-12
category: Archive
weight: 4
tags: [Unreal Engine 5, Kawaii Slender, Blueprint, Input System, Audio, Game Design]
prev_url: "/unreal-engine-5/jeu-horreur-kawaii/3-creer-lampe-torche-blueprint-joueur"
next_url: "/unreal-engine-5/jeu-horreur-kawaii/5-variable-sprint-course-stamina"
images: ["https://img.youtube.com/vi/SN8yuzdtLFg/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/SN8yuzdtLFg/maxresdefault.jpg"]
---

{{< youtube-rgpd "SN8yuzdtLFg" >}}

Dans ce quatrième volet de la série *Kawaii Slender*, nous faisons évoluer notre mécanique de lampe-torche rudimentaire en y ajoutant une gestion dynamique et systémique : une jauge de batterie "magique" qui se décharge à l'utilisation et se régénère automatiquement au fil du temps lorsque la lampe est éteinte.

### Concepts clés abordés dans ce tutoriel

* **Création et paramétrage des Variables de contrôle :**
    * Mise en place d'une variable booléenne `Lampe ON` pour suivre et interroger l'état binaire (allumé/éteint) de l'accessoire à tout moment.
    * Création d'une variable de type *Float* nommée `Batterie`, initialisée à `1.0` (représentant $100\%$ de charge). Cette normalisation (entre `0.0` et `1.0`) est idéale pour l'intégration future avec les barres de progression de l'interface utilisateur (HUD).
* **Contrôles de flux et conditions de sécurité :**
    * Utilisation intensive du node **Branch** pour valider les actions du joueur (ex: vérifier si la batterie est supérieure à `0.0` avant d'autoriser l'allumage).
    * Privilégier l'utilisation des comparateurs de sécurité (supérieur ou égal `/` inférieur ou égal) à la place d'une égalité stricte pour éviter les bugs de calcul flottant inhérents aux moteurs de jeu.
* **Gestion du temps avec les Timers (Boucles de calcul) :**
    * Implémentation du node **Set Timer by Event** paramétré en mode `Looping` pour répéter des blocs de logique à intervalles réguliers (toutes les secondes).
    * Création de deux *Custom Events* dédiés : `DiminuerBatterie` (soustraction de `0.1` à chaque cycle) et `AugmenterBatterie` (addition de `0.1` en phase de repos).
    * Utilisation des nœuds de redirection (*Reroute Nodes*) pour conserver un Blueprint propre, lisible et facile à déboguer malgré les interconnexions.
* **Logique d'interdiction et comportement de gameplay :**
    * Verrouillage du système : si la batterie tombe à `0.0`, la lampe s'éteint d'elle-même et le joueur se retrouve bloqué dans le noir, le forçant à attendre que la jauge remonte entièrement à `1.0` avant de pouvoir presser à nouveau l'interrupteur.

### Ce qui reste d'actualité aujourd'hui

Les paradigmes de programmation visuelle et les choix d'optimisation abordés dans cette archive s'appliquent parfaitement aux architectures de jeu actuelles sur Unreal Engine 5 :

1. **La puissance des Timers face à l'Event Tick :** L'optimisation CPU est plus critique que jamais. Utiliser des boucles de temps (`Set Timer by Event`) à la place de l'échantillonnage par image (`Event Tick`) reste la règle absolue en gamedev pour toutes les mécaniques de fond (jauges de survie, énergie, faim, rechargement).
2. **La normalisation des données ($0$ à $1$) :** Stocker des ressources sous forme de ratio entre `0.0` et `1.0` est la norme standard de l'industrie. Cela permet d'alimenter directement et proprement les matériaux d'interface (*UI Materials*) et les barres de progression des widgets UMG (*Widget Blueprints*) sans calculs complexes de conversion.
3. **Les raccourcis de productivité de l'éditeur :** Le maintien de la touche `Ctrl` enfoncée pour glisser-déposer automatiquement une variable sous forme de node "Get" (obtenir la valeur) demeure une manipulation incontournable pour fluidifier votre flux de travail au quotidien dans l'éditeur de Blueprints.

---
{{< footer >}}