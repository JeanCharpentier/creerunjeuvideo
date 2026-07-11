---
title: "9. Créer un menu de victoire pour votre jeu de plateforme 3D"
weight: 9
date: 2023-10-27
categories: ['Tutoriels GDevelop']
tags: ['GDevelop 5', '3D', 'GameDev', 'UI', 'Débutant']
images: ["https://img.youtube.com/vi/SLxC_FtjkYU/maxresdefault.jpg"]
---

Dans ce neuvième et ultime épisode de notre série dédiée à la création d'un jeu de plateforme 3D sur GDevelop 5, nous allons boucler la boucle. Après avoir mis en place les mécaniques de mouvement et la condition de défaite, il est temps d'offrir à vos joueurs la satisfaction de terminer le niveau.

{{< youtube-rgpd "SLxC_FtjkYU" >}}

### Au programme de cet épisode :
*   **Gestion du score cible :** Création d'une variable globale `scoreMax` pour définir l'objectif à atteindre.
*   **Interface de victoire :** Création d'un calque dédié pour afficher un message de félicitations.
*   **Sécurisation du code :** Utilisation de conditions de comparaison robustes (supérieur ou égal) pour éviter les bugs de calcul.
*   **Interaction utilisateur :** Ajout d'un bouton "Rejouer" pour relancer la scène proprement.
*   **Nettoyage :** Mise en place des ancres pour que votre interface reste parfaitement centrée, quel que soit l'écran.

### Ce qui reste d'actualité aujourd'hui
Même avec les mises à jour récentes de GDevelop, les principes abordés ici restent les fondations indispensables de tout jeu :
*   **L'utilisation des calques (Layers) :** C'est toujours la méthode la plus propre pour gérer les interfaces (UI) séparément du monde 3D.
*   **Variables globales :** Elles restent le moyen le plus simple pour faire transiter des informations (comme le score) entre différentes scènes.
*   **La logique de "Freeze" :** Figer le jeu lors de l'affichage d'un menu est une bonne pratique pour éviter que le joueur ne continue à bouger en arrière-plan.
*   **Sécurité des variables :** Utiliser `supérieur ou égal` au lieu de `égal` est un réflexe de développeur chevronné qui vous évitera bien des surprises avec les nombres à virgule flottante.

Félicitations pour avoir suivi cette première saison ! Vous avez désormais un prototype fonctionnel. N'hésitez pas à expérimenter, à ajouter des ennemis ou des plateformes mouvantes pour pimenter votre niveau.

{{< footer >}}