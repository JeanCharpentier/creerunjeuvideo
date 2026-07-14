---
titre: "14. Créer un Aim Offset pour la visée verticale"
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['FPS', 'Animation', 'Aim Offset', 'GameDev']
images: ["https://img.youtube.com/vi/IztmaEUPPsA/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/IztmaEUPPsA/maxresdefault.jpg"]
---

Dans cet épisode de notre série dédiée à la création d'un FPS sur Unreal Engine 4, nous allons nous attaquer à une étape cruciale pour le réalisme de votre jeu : permettre à l'arme de suivre le regard du joueur sur l'axe vertical. Grâce à l'utilisation des **Aim Offsets**, nous allons créer une transition fluide entre les différentes poses de visée.

{{< youtube-rgpd "IztmaEUPPsA" >}}

### Résumé des étapes clés
*   **Préparation des poses :** Extraction de 9 poses fixes (haut, bas, centre, gauche, droite) à partir de l'animation `Aim_Space_Idle` pour constituer la base de notre mélangeur.
*   **Configuration des Assets :** Utilisation du *Bulk Edit via Property Matrix* pour définir les poses en mode *Mesh Space* et les lier à l'animation de référence (`Idle_Rifle_Hip`).
*   **Création de l'Aim Offset :** Configuration des axes *Yaw* (horizontal) et *Pitch* (vertical) avec une plage de -90° à +90°.
*   **Intégration dans l'Anim Graph :** Ajout du nœud Aim Offset dans le Blueprint d'animation et création des variables `AimYaw` et `AimPitch`.
*   **Logique de calcul (Event Graph) :** Utilisation d'un `Delta Rotator` pour calculer la différence entre la rotation du contrôleur et celle de l'acteur, puis lissage avec un `RInterpTo`.
*   **Finalisation :** Ajustement de la position de la caméra dans le Character Blueprint pour un meilleur rendu visuel en vue subjective.

### Ce qui reste d'actualité aujourd'hui
Bien que cet article traite d'Unreal Engine 4, les concepts fondamentaux abordés ici sont toujours le standard de l'industrie dans **Unreal Engine 5** :
*   **Le système d'Aim Offset :** La logique de mélange de poses basée sur des valeurs de rotation reste la méthode privilégiée pour les jeux de tir à la troisième personne (ou pour voir ses propres bras en vue subjective).
*   **L'interpolation (RInterpTo) :** Le lissage des mouvements de visée est essentiel pour éviter les saccades lors des changements de direction rapides.
*   **La séparation des rotations :** La distinction entre la rotation du contrôleur (la souris) et celle du mesh (le corps du personnage) est une base indispensable pour éviter que le personnage ne pivote de manière irréaliste à chaque mouvement de caméra.

{{< footer >}}