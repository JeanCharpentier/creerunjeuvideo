---
title: "5. Gestion de la course et de l'endurance (Stamina)"
date: 2026-06-12
category: Archive
weight: 5
tags: [Unreal Engine 5, Kawaii Slender, Blueprint, Input System, Audio, Game Design]
prev_url: "/unreal-engine-5/jeu-horreur-kawaii/4-gestion-variables-batterie-lampe"
next_url: "/unreal-engine-5/jeu-horreur-kawaii/6-ui-umg-widget-affichage-hud-ue5"
images: ["https://img.youtube.com/vi/Yp4z3tJNZ2s/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/Yp4z3tJNZ2s/maxresdefault.jpg"]
---

{{< youtube-rgpd "Yp4z3tJNZ2s" >}}

Après avoir vu comment gérer l'énergie d'une lampe-torche, nous nous attaquons à un autre pilier du jeu de survie : **le système de course et d'endurance (stamina)**[cite: 12]. En nous appuyant sur des mécaniques similaires, nous allons adapter et optimiser notre logique pour répondre aux exigences d'un gameplay fluide[cite: 12].

### Concepts clés abordés dans ce tutoriel

* **Configuration fine de l'Enhanced Input System :**
    * Création d'une action d'entrée `IACourse` en mode booléen[cite: 12].
    * Utilisation du trigger **Hold** (maintenir la touche) au lieu de *Pressed* pour un comportement naturel de sprint (le joueur court uniquement quand il maintient la touche Shift gauche)[cite: 12].
    * Ajustement du *Hold Time Threshold* à `0.05` seconde pour garantir un déclenchement quasi instantané de la course[cite: 12].
* **Manipulation des composants de déplacement :**
    * Exploitation du composant **Character Movement** pour modifier dynamiquement les propriétés physiques du personnage[cite: 12].
    * Altération en temps réel de la variable `Max Walk Speed` pour faire passer la vitesse de marche (ex: 600) à une vitesse de sprint élevée (ex: 3000)[cite: 12].
* **Logique de consommation et de régénération :**
    * Création des variables de contrôle `court` (booléen) et `endurance` (float initialisé à `1.0` pour représenter $100\%$)[cite: 12].
    * Mise en place d'un système de vérification sécurisé (supérieur ou égal à `0.0`) pour vider l'endurance uniquement lorsque le joueur est en mouvement[cite: 12].
    * Création d'un *Custom Event* `augmenter_endurance` lié à une boucle temporelle (`Set Timer by Event`) pour recharger automatiquement la jauge dès que l'action s'arrête[cite: 12].
* **Contrôle avancé des Timers et validation de flux :**
    * Promotion de la valeur de retour du timer en variable de type **Timer Handle** (`Th_Endurance`) afin de pouvoir l'identifier dans la mémoire du moteur[cite: 12].
    * Utilisation des nodes `Does Timer Exist by Handle` et `Clear and Invalidate Timer by Handle` pour couper manuellement la régénération et éviter que deux timers contradictoires ne tournent en tâche de fond[cite: 12].
* **Optimisation par la Vélocité (Condition de mouvement) :**
    * Extraction du vecteur 3D via `GetVelocity` pour vérifier que le joueur se déplace réellement sur les axes $X$, $Y$ ou $Z$[cite: 12].
    * Utilisation d'un comparateur de vecteur avec une marge d'erreur (*Tolerance*) pour empêcher l'endurance de se vider si le joueur maintient la touche Shift en restant immobile[cite: 12].

### Ce qui reste d'actualité aujourd'hui

Les mécaniques implémentées dans cette archive respectent les bonnes pratiques indispensables sur les versions récentes d'Unreal Engine 5 :

1. **La maîtrise des Timer Handles :** Nettoyer et invalider ses timers (`Clear and Invalidate`) est une règle d'or en programmation Blueprint. Oublier de tuer un timer de régénération avant de relancer une action crée des conflits logiques et des fuites de performance invisibles mais dévastatrices.
2. **Le découplage Input / Vélocité :** Se baser uniquement sur la pression d'une touche pour consommer une ressource est une erreur classique de gamedev. Interroger le vecteur de vélocité (`GetVelocity`) du *Character Movement* reste la méthode standard et la plus fiable pour corréler une perte d'énergie à un mouvement réel du joueur.
3. **L'Enhanced Input System par défaut :** L'architecture des *Input Actions* (`IA_`) et *Input Mapping Contexts* (`IMC_`) introduite ici est désormais le système natif et obligatoire d'UE5, rendant la gestion des comportements comme le *Hold* extrêmement propre et modulaire.

---
{{< footer >}}