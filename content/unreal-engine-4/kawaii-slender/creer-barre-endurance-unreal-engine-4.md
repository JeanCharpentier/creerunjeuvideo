---
title: "18. Créer une barre d''endurance dynamique avec UMG"
weight: 18
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['UMG', 'UI', 'Blueprints', 'GameDev']
images: ["https://img.youtube.com/vi/arRHDbk6GzA/maxresdefault.jpg"]
---

Dans ce tutoriel, nous allons finaliser notre système d'endurance en ajoutant une interface visuelle (HUD). L'objectif est d'afficher une barre de progression qui se vide lorsque le joueur court et se remplit automatiquement lorsqu'il marche, offrant ainsi un retour visuel immédiat au joueur.

{{< youtube-rgpd "arRHDbk6GzA" >}}

### Résumé des étapes
*   **Préparation de la variable :** Rendre la variable `Endurance` publique dans le *FirstPersonCharacter* pour permettre aux autres Blueprints d'y accéder.
*   **Configuration de l'interface (UMG) :** Utiliser le widget HUD existant et ajouter un composant `Progress Bar`.
*   **Stylisation :** Positionner la barre (ancres), choisir sa couleur et définir son style visuel.
*   **Liaison des données (Binding) :** Créer un *Binding* sur la valeur "Percent" de la barre.
*   **Logique Blueprint :** Utiliser un `Cast To FirstPersonCharacter` pour récupérer la valeur d'endurance, la diviser par 100 (pour obtenir une valeur entre 0 et 1) et la renvoyer au `Return Node` de la fonction.

### Ce qui reste d'actualité aujourd'hui
Bien que ce tutoriel utilise une méthode de "Binding" directe (très simple pour débuter), les principes fondamentaux restent valides dans les versions récentes d'Unreal Engine :
*   **Le système UMG :** L'utilisation des `Progress Bar` et des ancres est toujours le standard pour créer des interfaces 2D.
*   **Communication entre Blueprints :** Le `Cast` reste une méthode courante pour accéder aux variables d'un personnage depuis un widget, bien que pour des projets plus complexes, l'utilisation d'**Event Dispatchers** ou de **Bind Delegates** soit recommandée pour optimiser les performances (éviter le cast à chaque frame).
*   **Normalisation des valeurs :** La conversion d'une valeur (0-100) vers un ratio (0-1) est une pratique universelle en développement d'interface.

{{< footer >}}