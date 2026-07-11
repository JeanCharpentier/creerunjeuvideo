---
title: "6. Créer un double saut (Double Jump)"
weight: 6
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['FPS', 'Blueprint', 'Character Movement', 'Tutoriel']
images: ["https://img.youtube.com/vi/vQ17Ngz905s/maxresdefault.jpg"]
---

Dans cet épisode de notre série dédiée à la création d'un FPS solo sur Unreal Engine 4, nous allons implémenter une mécanique essentielle pour la mobilité de votre personnage : le **double saut**.

{{< youtube-rgpd "vQ17Ngz905s" >}}

### Résumé du tutoriel
Pour mettre en place ce système, nous allons délaisser la fonction "Jump" classique d'Unreal Engine au profit de la fonction **Launch Character**. Voici les étapes clés :

*   **Utilisation de Launch Character :** Contrairement à la fonction de saut standard, celle-ci permet de définir un vecteur de lancement précis, idéal pour des mécaniques de dash ou de sauts multiples.
*   **Le nœud "Do N" :** C'est l'élément central pour limiter le nombre de sauts. En réglant "N" sur 2, vous autorisez un double saut. Vous pouvez facilement augmenter cette valeur pour des sauts triples ou plus.
*   **Gestion de la vélocité Z :** Nous récupérons la valeur `Jump Z Velocity` depuis le composant *Character Movement* pour assurer une cohérence avec votre saut initial.
*   **Z Override :** L'activation de cette option est cruciale : elle permet de réécrire la vélocité verticale, garantissant que le joueur puisse sauter même s'il est en phase de descente.
*   **Reset via "On Landed" :** Pour réinitialiser le compteur de sauts, nous utilisons l'événement `On Landed`, qui détecte quand le personnage touche le sol.

### Ce qui reste d'actualité aujourd'hui

Bien que les versions d'Unreal Engine aient évolué, les principes fondamentaux abordés ici restent des piliers du développement de jeux :

1.  **Modularité des Blueprints :** La logique utilisée ici (Launch Character + Do N) est toujours la méthode la plus propre pour créer des capacités de mouvement personnalisées sans alourdir le Character Movement Component.
2.  **Accessibilité des variables :** Apprendre à puiser directement dans les variables du `Character Movement` (comme le `Jump Z Velocity`) est une compétence indispensable pour tout développeur UE, quelle que soit la version du moteur.
3.  **Design de niveau :** Comme mentionné dans la vidéo, une mécanique de saut n'a de valeur que si le level design est pensé pour l'exploiter. La verticalité de vos cartes doit toujours être corrélée aux capacités de mouvement que vous offrez au joueur.
4.  **Flexibilité :** L'utilisation d'un nœud `Do N` permet une extensibilité facile : vous pouvez, par exemple, lier le nombre de sauts autorisés à un objet ramassé ou à une compétence débloquée dans un arbre de talents.

{{< footer >}}