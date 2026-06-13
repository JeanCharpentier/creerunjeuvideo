---
title: "5. Intégrer et déplacer votre vaisseau"
weight: 5
prev_url: "/game-maker-studio/shoot-them-up/creation-objets-scrolling-parallaxe-gamemaker/"
next_url: "/game-maker-studio/shoot-them-up/limiter-deplacements-vaisseau-game-maker-studio/"
date: 2023-10-27
categories: ['Archive']
tags: ['Game Maker', 'GML', 'Tutoriel', 'Developpement de jeu', 'Debutant']
---

Dans ce guide, nous allons apprendre à placer votre vaisseau dans la room et à lui donner vie grâce aux bases du Game Maker Language (GML).

{{< youtube-rgpd "sqdTCqctBGc" >}}

### Résumé des notions clés

*   **Placement dans la Room :** Utilisez l'onglet "Object" pour sélectionner votre vaisseau et le placer dans votre niveau. L'utilisation de la grille (Grid) est essentielle pour aligner précisément vos éléments.
*   **Le concept Événement/Action :** La logique de Game Maker repose sur ce duo. Un événement (ex: appui sur une touche) déclenche une action spécifique.
*   **Utilisation du GML (Game Maker Language) :** Plutôt que le Drag & Drop, nous utilisons ici l'éditeur de code pour une meilleure flexibilité.
*   **Variables intégrées :** Game Maker gère nativement les coordonnées `x` et `y` de vos objets, vous évitant de les déclarer manuellement.
*   **Système de coordonnées :** Dans Game Maker, l'origine (0,0) se situe en haut à gauche. Pour monter, on soustrait une valeur à `y` ; pour descendre, on l'additionne.
*   **Syntaxe condensée :** Apprenez à utiliser les opérateurs d'affectation composée comme `y -= 5` ou `y += 5` pour un code plus propre et rapide.
*   **Commentaires :** Utilisez `//` pour des notes personnelles et `///` pour nommer vos blocs de code dans l'interface de l'objet.

### Ce qui reste d'actualité aujourd'hui

Bien que les versions récentes de Game Maker aient évolué, les fondamentaux abordés ici restent le socle de tout projet :

1.  **La gestion des coordonnées :** Le système de coordonnées (0,0 en haut à gauche) est une norme dans la quasi-totalité des moteurs 2D. Maîtriser ce déplacement est indispensable.
2.  **L'importance du GML :** Apprendre à écrire du code plutôt que de se reposer uniquement sur des briques visuelles vous donne une liberté créative totale et facilite le débogage de vos jeux complexes.
3.  **La structure événementielle :** La logique "Événement -> Action" est le cœur battant de Game Maker. Comprendre comment les événements clavier (`Keyboard Event`) interagissent avec les variables d'instance est une compétence transférable à n'importe quel autre langage de programmation orienté objet.
4.  **Bonnes pratiques :** L'utilisation des commentaires et la simplification du code (`y += 5`) sont des habitudes de développeur professionnel qui rendent votre projet maintenable sur le long terme.

{{< footer >}}