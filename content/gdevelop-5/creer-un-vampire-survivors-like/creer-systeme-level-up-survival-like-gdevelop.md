---
title: "7. Créer un système d'upgrades (Level Up) - Partie 2"
weight: 7
date: 2024-05-22
categories: ['Tutoriels GDevelop']
tags: ['GDevelop5', 'Survival-like', 'GameDesign', 'Programmation']
images: ["https://img.youtube.com/vi/R7rsia81_T4/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/R7rsia81_T4/maxresdefault.jpg"]
---

Dans ce septième épisode de notre série dédiée à la création d'un jeu de type "Survival-like" sur GDevelop 5, nous clôturons notre système de montée de niveau. Après avoir mis en place l'interface des cartes d'amélioration dans la première partie, nous allons maintenant coder la logique mécanique qui permet de booster réellement les statistiques de votre personnage.

{{< youtube-rgpd "R7rsia81_T4" >}}

### Résumé du tutoriel
Dans cette vidéo, nous abordons les points clés suivants :
*   **Gestion des clics :** Détection du clic sur les boutons d'amélioration et vérification de leur identifiant (ID) pour déclencher le bon bonus.
*   **Application des upgrades :** Utilisation de variables pour multiplier les statistiques (vitesse, dégâts, cadence de tir, PV max).
*   **Gestion des projectiles :** Passage à une variable globale pour les dégâts afin que les nouveaux projectiles créés héritent des bonus acquis.
*   **Pause du jeu :** Utilisation de l'échelle de temps (*Time Scale*) pour figer le jeu pendant le choix des améliorations et éviter que le personnage ne continue de ramasser de l'expérience en arrière-plan.
*   **Mise à jour de l'UI :** Synchronisation automatique de la barre de vie après une augmentation des points de vie maximum.

### Ce qui reste d'actualité aujourd'hui
Bien que GDevelop évolue constamment, les principes fondamentaux présentés ici restent des piliers du développement de jeux :
*   **La modularité :** L'utilisation de variables globales pour les statistiques (dégâts, vitesse) est la méthode la plus propre pour assurer la cohérence entre les objets existants et ceux qui seront instanciés plus tard.
*   **Le contrôle du temps :** La manipulation de l'échelle de temps (`Time Scale`) est une technique indispensable pour les menus de pause ou les phases de sélection dans les jeux d'action.
*   **La structure des données :** Apprendre à organiser ses variables via des structures ou des tableaux permet de rendre votre code beaucoup plus lisible et facile à maintenir à mesure que votre projet grandit.
*   **L'évolutivité :** En séparant la logique de calcul (les facteurs d'amélioration) de la logique d'affichage, vous pouvez ajuster l'équilibrage de votre jeu en quelques secondes sans toucher à la structure complexe de vos événements.

{{< footer >}}