---
title: "7. Ramassage d'objets (Raycast), système de score et éclairage d'ambiance"
date: 2026-06-12
category: Archive
weight: 7
tags: [Unreal Engine 5, Kawaii Slender, Blueprint, Input System, Audio, Game Design]
prev_url: "/unreal-engine-5/jeu-horreur-kawaii/6-ui-umg-widget-affichage-hud-ue5"
next_url: "/unreal-engine-5/jeu-horreur-kawaii/8-ia-behavior-tree-blackboard-ennemi"
---

{{< youtube-rgpd "VYW1HT98yQA" >}}

Dans ce septième volet de la série *Kawaii Slender*, nous passons à une étape essentielle du gameplay : l'interaction avec l'environnement. Nous allons voir comment permettre au joueur de cibler et de ramasser des objets au sol (des burgers Low-Poly) pour incrémenter un système de score, tout en ajustant la lisibilité de notre scène nocturne.

### Concepts clés abordés dans ce tutoriel

* **Amélioration de la lisibilité et de la jouabilité (Quality of Life) :**
    * Ajout d'une source lumineuse subtile de type **Point Light** attachée de manière permanente au joueur.
    * Cette technique permet de conserver une ambiance générale très sombre et oppressante (torche éteinte) tout en offrant un rayon de visibilité minimal pour que le joueur puisse se déplacer et repérer les éléments interactifs sans frustration.
* **Détection par tir de rayon invisible (Line Trace / Raycast) :**
    * Utilisation du node **Line Trace By Channel** pour projeter un rayon invisible depuis le centre de la caméra (notre viseur).
    * Calcul des coordonnées vectorielles : définition du point de départ (*Start*) via la position de la caméra, et du point d'arrivée (*End*) en multipliant le vecteur de direction (*Get Forward Vector*) par une variable de distance maximale d'interaction (ex: 200 à 300 unités).
    * Configuration du mode de débogage (*Draw Debug Type*) sur **For One Frame** ou **For Duration** pour matérialiser le rayon rouge/vert à l'écran et valider visuellement les collisions.
* **Identification et interaction avec les objets (Hit Result) :**
    * Exploitation de la structure de retour **Out Hit** pour extraire l'identité précise de l'entité survolée.
    * Utilisation du node **Break Hit Result** pour isoler le composant touché (*Hit Actor*).
    * Implémentation d'un filtre d'identité via un moulage (**Cast to BP_Burger**) pour s'assurer que le rayon n'interagit qu'avec les objets collectables et ignore les murs ou le décor.
* **Logique de collecte et destruction d'acteurs :**
    * Appel de la fonction **Destroy Actor** sur l'objet ciblé dès que le joueur presse la touche d'interaction et que le Cast est validé.
    * Déclenchement de micro-mécaniques associées (effets sonores *Play Sound 2D* ou déclenchement de particules au point d'impact).
* **Mise à jour du Score et liaison UMG :**
    * Création d'une variable entière `Score` (ou `BurgersRamassés`) au sein du Blueprint du personnage.
    * Utilisation de l'opérateur d'incrémentation `++` ou d'une addition basique pour ajouter une unité à chaque ramassage réussi.
    * Intégration d'un nouveau bloc de texte (*Text Block*) dans notre interface existante (`WBP_MainUI`), positionné en bas à droite de l'écran grâce aux ancres, et lié dynamiquement à la variable de score du joueur avec un node de conversion automatique *Integer to Text*.

### Ce qui reste d'actualité aujourd'hui

Les mécaniques de détection et de ciblage implémentées dans cette archive restent de parfaits standards de développement sur Unreal Engine 5 :

1. **Le Line Trace comme pilier de l'interaction :** Qu'il s'agisse d'ouvrir une porte, de ramasser un objet, de lire une note ou de tirer avec une arme à feu, le node *Line Trace By Channel* (Raycast) reste la méthode la plus précise, légère et universelle pour gérer l'interaction à la première personne.
2. **Le filtrage par Cast ou par Interface :** Utiliser un node de *Cast* en sortie d'un *Hit Result* est parfait pour prototyper rapidement l'identification d'un objet. Pour des projets à plus grande échelle, cette logique évolue naturellement vers les *Blueprint Interfaces (BPI)*, mais la structure mathématique du tir de rayon reste identique.
3. **L'affichage dynamique des données textuelles :** Lier un champ de texte UMG à une variable mise en cache dans le profil du personnage demeure la méthode la plus rapide pour afficher des compteurs (score, munitions, clés) de manière fluide et synchronisée.

---
{{< footer >}}