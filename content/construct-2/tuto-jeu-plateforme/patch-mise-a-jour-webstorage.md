---
title: "Patch : Mise à jour du système WebStorage"
date: 2026-06-13
weight: 11
categories: ["Archive", "Bug Fix"]
tags: ["Construct 2", "Game Dev", "Tutoriel", "WebStorage", "Patch"]
prev_url: "/construct-2/tuto-jeu-plateforme/8-systeme-score-web-storage"
next_url: "/construct-2/tuto-jeu-plateforme/9-systeme-codes-niveaux"
images: ["https://img.youtube.com/vi/CZJy3SqyupE/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/CZJy3SqyupE/maxresdefault.jpg"]
---

> **Note :** Cet article est une archive corrective visant à mettre à jour la méthode de persistance des données (WebStorage), suite à des changements dans les versions de Construct 2.

{{< youtube-rgpd "CZJy3SqyupE" >}}

### Pourquoi ce patch ?
Dans les versions initiales de Construct 2 (il y a plusieurs années), l'utilisation de l'objet *WebStorage* était la méthode standard pour conserver des données comme le score ou le nom d'utilisateur entre deux layouts. Ce tutoriel patch explique comment adapter cette logique pour assurer la compatibilité avec les versions plus récentes du moteur.

### Points clés du patch

* **Rappel du WebStorage :** L'objet permet de stocker des données côté navigateur de façon persistante. Il est idéal pour sauvegarder le score de session ou le niveau atteint.
* **Mise à jour de la logique :** Si votre version de Construct 2 présente des incompatibilités avec l'ancienne manipulation de l'objet *WebStorage*, ce correctif détaille comment réinitialiser les clés de stockage lors du démarrage du layout (`On start of layout`) pour éviter les conflits de données.
* **Test de persistance :** Le tutoriel démontre comment vérifier que le score est correctement transmis entre le niveau de jeu et l'écran de Game Over ou le menu principal.

### Rappel technique
Pour une persistance efficace :
1.  **Déclaration :** Assurez-vous que l'objet `WebStorage` est bien présent dans votre projet.
2.  **Stockage :** Utilisez l'action `Set local value` pour enregistrer vos variables globales.
3.  **Récupération :** Utilisez l'expression `WebStorage.LocalValue("NOM_DE_VOTRE_CLE")` pour afficher les données sauvegardées.
4.  **Nettoyage :** Si vous changez de session de jeu (ex: retour au menu principal), prévoyez une action pour remettre à zéro vos variables globales et les clés du WebStorage pour éviter que le score du joueur précédent ne soit conservé.

### Ce qui reste d'actualité
La logique de sauvegarde locale via le navigateur reste une compétence clé pour tout projet Web. Même si les outils ont évolué, le principe de stocker une valeur dans une "clé" et de la récupérer plus tard est une notion fondamentale du développement web et applicatif.

{{< footer >}}