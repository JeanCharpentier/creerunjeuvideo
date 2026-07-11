---
title: "3. Créer votre premier minerai personnalisé avec MCreator"
weight: 3
date: 2026-06-17
categories: ['GameDev']
tags: ['Minecraft', 'MCreator', 'Modding', 'Tutoriel']
images: ["https://img.youtube.com/vi/h0N2K_mwTsQ/maxresdefault.jpg"]
---

Bienvenue dans ce troisième volet de notre série dédiée au modding Minecraft. Aujourd'hui, nous passons à la pratique avec **MCreator**, l'outil incontournable pour créer du contenu sans avoir besoin de maîtriser le code Java complexe. Nous allons apprendre à intégrer un nouveau minerai, la "Yelonite", de sa texture jusqu'à sa génération automatique dans vos mondes.

{{< youtube-rgpd "h0N2K_mwTsQ" >}}

### Résumé des étapes de création
Pour ajouter un minerai fonctionnel, voici la marche à suivre dans MCreator :

*   **Préparation des ressources :** Créez une texture en 16x16 pixels au format PNG.
*   **Importation :** Utilisez le menu "Tools" pour importer votre texture en tant que "Block".
*   **Configuration du bloc :**
    *   Nommez votre identifiant (sans espaces ni accents).
    *   Définissez la dureté (ex: 6 pour une résistance équivalente au fer).
    *   Choisissez le son associé (ex: gravier) et le niveau d'outil requis pour le minage.
*   **Génération du monde :** Activez l'option "World Generation" pour définir les couches (Y) et la fréquence d'apparition du minerai.
*   **Test en jeu :** Utilisez le bouton "Play" pour lancer une instance de test et vérifier que votre bloc apparaît bien dans l'inventaire créatif et se génère naturellement.

### Ce qui reste d'actualité aujourd'hui

Bien que les versions de MCreator évoluent rapidement, les fondamentaux présentés dans cet épisode restent la base du modding moderne :

1.  **La structure des assets :** Le format 16x16 reste le standard pour conserver l'esthétique "Vanilla" de Minecraft.
2.  **La logique de minage :** La gestion des outils (Harvest Level) et de la dureté est toujours le cœur du système de progression dans n'importe quel mod d'ajout de minerais.
3.  **L'importance de la génération procédurale :** Comprendre comment régler la fréquence et les couches de spawn est essentiel pour l'équilibrage de votre mod, peu importe la version du jeu.
4.  **Le workflow de test :** L'utilisation du mode créatif et des commandes `/gamemode` pour tester rapidement ses créations en conditions réelles est une pratique que tout développeur de mods continue d'utiliser quotidiennement.

{{< footer >}}