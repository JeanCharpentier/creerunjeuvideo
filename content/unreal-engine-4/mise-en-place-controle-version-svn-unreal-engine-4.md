---
title: "Mise en place du contrôle de version (SVN) sur Unreal Engine 4"
date: 2026-06-17
categories: ['Tutoriels']
tags: ['Unreal Engine 4', 'SVN', 'TortoiseSVN', 'Version Control', 'GameDev']
images: ["https://img.youtube.com/vi/E4tMAdkYQBY/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/E4tMAdkYQBY/maxresdefault.jpg"]
---

Travailler en équipe sur un projet Unreal Engine 4 nécessite une gestion rigoureuse des fichiers pour éviter les conflits et les pertes de données. Dans ce tutoriel, nous allons voir comment configurer un système de contrôle de version (Versioning) avec **Subversion (SVN)** et **TortoiseSVN**, afin de synchroniser votre projet entre plusieurs collaborateurs.

{{< youtube-rgpd "E4tMAdkYQBY" >}}

### Résumé de la procédure
*   **Installation :** Téléchargez et installez [TortoiseSVN](https://tortoisesvn.net/) sur votre machine Windows.
*   **Préparation du dossier :** Créez un dossier vide, effectuez un "SVN Checkout" en renseignant l'URL de votre dépôt (repository).
*   **Intégration du projet :** Copiez les fichiers essentiels de votre projet (`Config/`, `Content/`, `.uproject`, et `Source/` si C++) dans ce dossier.
*   **Ajout au serveur :** Utilisez le menu contextuel TortoiseSVN (`Add`) pour préparer les fichiers, puis `Commit` pour les envoyer sur le serveur.
*   **Connexion dans UE4 :** Dans l'éditeur Unreal, allez dans **Source Control > Connect to Source Control**, sélectionnez "Subversion", renseignez vos identifiants et l'URL du dépôt.
*   **Workflow quotidien :** Utilisez le bouton "Source Control" dans l'éditeur pour faire des `Submit` (envoi) et des `Checkout` (récupération des modifications des autres).

### Ce qui reste d'actualité aujourd'hui
Bien que les outils de versioning aient évolué (avec une montée en puissance de **Git** via LFS ou **Perforce** pour les gros projets AAA), les principes fondamentaux expliqués ici restent parfaitement valables pour Unreal Engine :

1.  **Le contrôle de version est indispensable :** Même en solo, avoir un historique de ses modifications permet de revenir en arrière en cas de corruption de projet.
2.  **Exclusion des fichiers temporaires :** Il est toujours crucial de ne pas versionner les dossiers `Intermediate`, `Saved` et `DerivedDataCache`, car ils sont générés automatiquement et alourdiraient inutilement votre dépôt.
3.  **Communication via les messages de commit :** La règle d'or reste la même : rédigez des messages explicites lors de vos soumissions pour que vos collaborateurs comprennent les changements effectués.
4.  **Verrouillage des fichiers :** Le concept de "Checkout" dans Unreal Engine permet de marquer un fichier comme étant en cours de modification, évitant ainsi que deux personnes ne travaillent sur le même Blueprint simultanément, ce qui est une limitation majeure des fichiers binaires dans les moteurs de jeu.

{{< footer >}}