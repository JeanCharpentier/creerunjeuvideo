---
title: "3. Création d''armes et de recettes : Maîtrisez le modding sur Hytale"
weight: 3
date: 2024-05-22
categories: ['Modding']
tags: ['Hytale', 'Tutoriel', 'Modding', 'Asset Editor', 'Crafting']
---

Dans ce troisième et dernier volet de notre série découverte, nous passons à l'étape cruciale : transformer vos minerais en armes fonctionnelles. Nous verrons comment configurer les recettes de fonte, définir les établis requis et même ajouter un petit bonus décoratif pour personnaliser votre atelier.

{{< youtube-rgpd "oMDpOJPyTDE" >}}

### Résumé de la procédure
*   **Organisation des fichiers :** Avant de multiplier les objets, structurez votre modpack en dossiers (ex: `Orz` pour les minerais, `Weapons` pour les armes) pour une meilleure lisibilité.
*   **Création d'un lingot :** Utilisez la fonction "Duplicate" sur un objet existant (ex: `ingredient_bar_iron`) dans l'Asset Editor pour créer rapidement vos nouveaux matériaux.
*   **Configuration des recettes :**
    *   **Input/Output :** Définissez la matière première et le résultat (vous pouvez même multiplier la quantité obtenue).
    *   **Temps de cuisson :** Ajustez la durée de transformation dans le four.
    *   **Bancs de travail :** Assignez l'établi nécessaire (`Furnace` pour la fonte, `Blacksmith Anvil` pour la forge).
*   **Gestion des tiers :** Vous pouvez restreindre la fabrication d'objets complexes à des établis de niveau supérieur (Tier 2, Tier 3) pour équilibrer votre progression.
*   **Bonus décoratif :** Apprenez à créer des blocs de décoration (comme des piles de lingots) en dupliquant des modèles existants et en modifiant leurs textures via un logiciel de retouche d'image.

### Ce qui reste d'actualité aujourd'hui
Bien que l'interface de l'Asset Editor puisse évoluer avec les mises à jour d'Hytale, les fondamentaux du modding restent les mêmes :
1.  **La logique de duplication :** Partir d'un objet existant est toujours la méthode la plus rapide et la plus sûre pour éviter les erreurs de configuration.
2.  **La rigueur de nommage :** Le respect des majuscules et des underscores (`_`) est vital pour que le moteur du jeu reconnaisse vos fichiers JSON.
3.  **La hiérarchie des assets :** Une bonne organisation de vos dossiers `server` et `common` est indispensable pour maintenir un modpack complexe sur le long terme.
4.  **La traduction :** L'utilisation du fichier `server.lang` reste la norme pour localiser vos objets et éviter les noms techniques peu esthétiques en jeu.

{{< footer >}}