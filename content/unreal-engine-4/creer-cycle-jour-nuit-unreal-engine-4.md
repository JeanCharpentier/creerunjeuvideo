---
title: "Créer un cycle jour/nuit dynamique dans Unreal Engine 4"
date: 2026-06-17
categories: ['Développement Unreal Engine']
tags: ['Unreal Engine 4', 'Blueprints', 'Cycle Jour-Nuit', 'Level Design']
images: ["https://img.youtube.com/vi/AzyoRemYMUM/maxresdefault.jpg"]
---

Dans ce tutoriel, nous allons voir comment mettre en place un système de cycle jour/nuit simple et efficace dans Unreal Engine 4. Ce guide répond à une problématique courante : comment automatiser la rotation du soleil pour simuler le passage du temps dans votre environnement.

{{< youtube-rgpd "AzyoRemYMUM" >}}

### Résumé du processus
*   **Utilisation des Timelines :** Création d'une `Timeline` dans le *Level Blueprint* pour gérer la variation de valeur sur 24 secondes (symbolisant 24 heures).
*   **Configuration de la courbe :** Utilisation d'une piste `Float` allant de 0 à 360 degrés pour piloter la rotation.
*   **Manipulation de la lumière :** Liaison de la `Timeline` à la rotation de la `Directional Light` (Light Source).
*   **Mise à jour du ciel :** Appel de la fonction `Update Sun Direction` sur le `BP_Sky_Sphere` pour synchroniser les textures du ciel avec la position du soleil.
*   **Paramétrage technique :** Passage de la lumière en mode `Movable` et désactivation des ombres statiques (`Cast Static Shadows`) pour permettre un rendu dynamique fluide.

### Ce qui reste d'actualité aujourd'hui

Bien que ce tutoriel utilise des méthodes fondamentales d'Unreal Engine 4, ces concepts restent parfaitement valides dans les versions plus récentes (UE5) pour des projets légers :

1.  **Le système de Timeline :** C'est toujours l'outil le plus intuitif pour créer des animations basées sur le temps directement dans les Blueprints sans passer par le *Sequencer*.
2.  **La gestion des Sky Spheres :** La logique de rafraîchissement du ciel (`Update Sun Direction`) est la base du système de ciel procédural classique.
3.  **L'importance du mode "Movable" :** Comprendre la différence entre les lumières statiques et dynamiques est crucial pour tout développeur, quel que soit le moteur, afin d'optimiser les performances.
4.  **Flexibilité :** La méthode de division utilisée pour ralentir la vitesse du cycle montre comment manipuler mathématiquement vos variables pour ajuster le "gameplay" de votre environnement.

*Note : Pour des projets plus avancés, il est recommandé d'utiliser le système "Ultra Dynamic Sky" ou le "Sun Sky" intégré nativement dans les versions récentes pour une gestion plus réaliste de l'atmosphère.*

{{< footer >}}