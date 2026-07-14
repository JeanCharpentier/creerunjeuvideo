---
title: "Correctif: Animation de marche persistante à l'atterrissage"
date: 2026-06-13
weight: 8
categories: ["Bug Fix"]
tags: ["Construct 2", "Game Dev", "Tutoriel", "Animation", "Bug Fix"]
prev_url: "/construct-2/tuto-jeu-plateforme/6-gestion-collisions-hud"
next_url: "/construct-2/tuto-jeu-plateforme/7-gestion-vie-score"
images: ["https://img.youtube.com/vi/-JRy0hVrxgg/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/-JRy0hVrxgg/maxresdefault.jpg"]
---

> **Note :** Cet article traite d'un correctif rapide (hors-série) concernant un bug d'animation où le personnage conservait l'animation "marche" après l'atterrissage si la touche de direction était relâchée juste avant le contact avec le sol.

{{< youtube-rgpd "-JRy0hVrxgg" >}}

### Le Problème
Lorsqu'un joueur saute et relâche la touche directionnelle (gauche ou droite) avant d'atterrir, l'animation de marche restait bloquée en boucle jusqu'à ce qu'une nouvelle action soit entreprise.

### Solution : Utilisation des entrées clavier
Au lieu de baser l'animation de marche uniquement sur l'état de mouvement du personnage, nous allons conditionner l'animation à l'état réel des touches du clavier.

#### Étapes de modification dans la feuille d'événements (ES Joueur) :

1.  **Suppression de l'ancienne logique :** Identifiez et supprimez l'événement qui déclenchait l'animation de marche basé sur le mouvement générique du personnage.
2.  **Création des sous-événements :** Sous votre condition d'atterrissage, créez deux sous-événements utilisant l'objet **Keyboard** :
    *   **Sous-événement A :** `Keyboard` -> `Key is down` -> `Right Arrow`.
        *   Action : Régler l'animation sur `Marche`.
    *   **Sous-événement B :** Copiez le sous-événement précédent, puis modifiez la touche pour `Left Arrow` (`Keyboard` -> `Key is down` -> `Left Arrow`).
        *   Action : Conservez l'animation `Marche` (le miroir sera géré automatiquement par vos autres événements).

### Pourquoi cette méthode ?
En vérifiant directement l'état des touches (`Key is down`) plutôt que l'état de mouvement du moteur physique, on s'assure que l'animation "Marche" ne s'exécute que si le joueur maintient volontairement une direction. Si les touches sont relâchées avant l'atterrissage, la condition n'est plus remplie et le bug d'animation en boucle disparaît.

{{< footer >}}