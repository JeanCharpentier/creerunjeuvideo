---
title: "Créer un menu contrôlé à la manette sur Construct 2"
date: 2026-06-17
categories: ['Archive']
tags: ['Construct 2', 'Tutoriel', 'GameDev', 'UI', 'Gamepad']
---

Dans ce tutoriel, nous allons voir comment concevoir un menu interactif et esthétique pour vos jeux sur **Construct 2**, en remplaçant la traditionnelle navigation à la souris par une gestion complète à la manette (Gamepad). L'objectif est de créer une interface fluide où les boutons réagissent visuellement à la sélection.

{{< youtube-rgpd "BZlc06r9yfA" >}}

### Résumé des étapes clés

*   **Variables et Fonctions :** Utilisation d'une variable globale `bouton` pour suivre l'index de l'élément sélectionné et d'une fonction `CH_bouton` pour centraliser la logique de navigation (incrémentation/décrémentation).
*   **Gestion du Gamepad :** Utilisation de l'objet `Gamepad` pour détecter les pressions sur le D-Pad (haut/bas) et le bouton de validation (A).
*   **Boucle Every Tick :** Mise en place d'une vérification constante pour appliquer un effet visuel (agrandissement via `Set Scale`) sur le bouton actif.
*   **Optimisation :** Réinitialisation de la taille des boutons à chaque appel de fonction pour éviter les conflits d'affichage sans multiplier les lignes d'événements.
*   **Navigation :** Utilisation de la condition `On Button Pressed` couplée à des sous-événements pour rediriger le joueur vers les différents *Layouts* (Aventure, Options, etc.).

### Ce qui reste d'actualité aujourd'hui

Bien que Construct 2 soit un moteur plus ancien, les principes fondamentaux abordés ici restent parfaitement transposables dans **Construct 3** ou d'autres moteurs 2D :

1.  **La logique d'indexation :** Le système de variable globale pour indexer des éléments d'un menu est une pratique standard qui évite de coder des comportements spécifiques pour chaque bouton.
2.  **La modularité des fonctions :** Utiliser des fonctions pour gérer les entrées permet de garder une feuille d'événements propre et facile à déboguer.
3.  **L'expérience utilisateur (UX) :** L'idée de donner un feedback visuel (agrandissement, changement de couleur) lors de la navigation à la manette est indispensable pour le confort du joueur sur console ou PC.
4.  **Gestion des entrées :** La distinction entre le D-Pad et les joysticks analogiques est un point crucial que tout développeur doit maîtriser pour assurer la compatibilité avec différents contrôleurs.

{{< footer >}}