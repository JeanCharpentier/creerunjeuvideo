---
title: "11. Gestion des collisions et effet de mort en Ragdoll"
date: 2026-06-12
category: Archive
weight: 11
tags: [Unreal Engine 5, Kawaii Slender, Blueprint, Input System, Audio, Game Design]
prev_url: "/unreal-engine-5/jeu-horreur-kawaii/10-slender-animations-3d-spacialisation-sonore-blendspace"
next_url: "/unreal-engine-5/jeu-horreur-kawaii/12-win-loose-gameover-ecran-fin-menu-widget"
images: ["https://img.youtube.com/vi/LWb6OKDjb4E/maxresdefault.jpg"]
---

{{< youtube-rgpd "LWb6OKDjb4E" >}}

Maintenant que notre poulet géant est pleinement animé et capable de nous traquer à l'oreille et à la vue, il est temps de gérer la confrontation. Dans ce onzième épisode, nous mettons en place la mécanique de défaite : la détection du contact entre l'ennemi et le joueur, suivie du déclenchement d'un effet physique de mort en **Ragdoll** pour désarticuler notre personnage.

### Concepts clés abordés dans ce tutoriel

* **Gestion des masques et canaux de collision :**
    * Configuration des profils de collision (*Collision Presets*) pour s'assurer que le monstre et le joueur s'impactent correctement.
    * Ajustement des boîtes de collision pour éviter que l'IA ne passe à travers le joueur ou ne pousse involontairement les objets collectables (burgers) éparpillés sur la carte.
* **Détection de l'impact (Capsule Overlap) :**
    * Utilisation de l'événement **On Component Begin Overlap** à partir de la capsule de collision de l'IA (`BP_Slender`).
    * Filtrage de la collision : utilisation d'un node de moulage (**Cast to BP_FirstPersonCharacter**) sur le paramètre *Other Actor* pour valider que c'est bien le joueur qui a été touché, et non un pan de décor.
* **Déclenchement et bascule en mode Ragdoll :**
    * Utilisation du node **Set Simulate Physics** appliqué au composant *Mesh* (le corps) du personnage principal pour couper les animations programmées et laisser la physique d'Unreal prendre le relais.
    * Modification du profil de collision du Mesh via le node **Set Collision Profile Name** pour le passer en mode **Ragdoll**. Cette étape est cruciale pour que les membres du corps réagissent correctement avec le sol et les obstacles lors de la chute.
* **Désactivation des contrôles et détachement de la caméra :**
    * Appel de la fonction **Disable Movement** sur le composant *Character Movement* pour figer instantanément les déplacements du joueur.
    * Utilisation du node **Detach From Component** sur la caméra à la première personne. En rompant le lien de parenté hiérarchique entre la caméra et la capsule de collision, on permet à la caméra de suivre naturellement la chute inerte du corps au sol au lieu de rester figée en l'air.

### Ce qui reste d'actualité aujourd'hui

Les mécaniques de gestion physique et de fin de partie présentées dans cette archive respectent les standards techniques d'Unreal Engine 5 :

1. **La robustesse du flux Overlap -> Cast :** Utiliser les événements d'Overlap de capsule combinés à un filtre d'identité (*Casting*) reste la méthode la plus légère et la plus fiable en gamedev pour déclencher des scripts de proximité ou d'attaque (pièges, zones de mort, coups au corps à corps).
2. **Le flux de travail Ragdoll standard :** Passer un *Skeletal Mesh* en simulation physique (`Set Simulate Physics`) tout en adaptant son profil de collision à la volée demeure la méthode universelle sous UE5 pour gérer les morts réalistes, les KO ou les projections physiques de personnages.
3. **Le découplage de la caméra à la mort :** Détacher la caméra de la capsule du joueur lors du décès est une technique de mise en scène incontournable. Elle permet d'éviter l'effet "caméra flottante" et offre une transition visuelle dramatique indispensable avant l'apparition d'un écran de type *Game Over*.

---
{{< footer >}}