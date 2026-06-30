---
title: "5. Importer et configurer une arme personnalisée dans UDK"
weight: 5
date: 2026-06-17
categories: ['Unreal Engine 3']
tags: ['UDK', 'Blender', 'GameDev', 'Tutoriel', 'UnrealScript']
---

Dans cette dernière partie de notre série, nous allons franchir l'étape cruciale : intégrer votre modèle 3D créé sous Blender dans l'Unreal Development Kit (UDK). Nous verrons comment importer le mesh, configurer les sockets pour les effets visuels, créer les classes nécessaires en UnrealScript et enfin tester votre arme en jeu.

{{< youtube-rgpd "WgkhKdyq9cc" >}}

### Résumé des étapes clés
*   **Importation FBX :** Configuration du package dans le *Content Browser* et paramétrage de l'import (Skeletal Mesh, animations, textures).
*   **Préparation du Mesh :** Ajustement de l'orientation (Yaw/Roll) et création d'un *AnimSet* vide.
*   **Gestion des Sockets :** Création des points d'ancrage pour le *Muzzle Flash* (sortie du canon) et le point de maintien de l'arme.
*   **Configuration du code :** Modification du fichier `DefaultEngine.ini` pour déclarer votre dossier de classes et utilisation de l'assistant *UnrealScript Wizard* pour générer la structure de l'arme.
*   **Scripting :** Ajout des lignes de code pour définir le type de tir (projectile) et l'emplacement du *Muzzle Flash*.
*   **Compilation :** Utilisation de l'outil *Unreal Frontend* pour compiler les scripts.
*   **Intégration Map :** Placement des *Pickup Factories* dans le niveau pour tester l'arme et ses munitions en jeu.

### Ce qui reste d'actualité aujourd'hui
Bien que l'UDK (Unreal Engine 3) soit aujourd'hui considéré comme un moteur "legacy", les concepts fondamentaux abordés ici restent le socle de tout développement sur les versions modernes (UE4/UE5) :
1.  **Le pipeline de contenu :** La logique d'importation via FBX, la gestion des matériaux et des textures reste quasi identique dans le workflow actuel.
2.  **Les Sockets :** L'utilisation de points d'attache sur un squelette pour les effets de particules (Muzzle Flash) est une pratique standard indispensable.
3.  **La séparation Logique/Visuel :** La distinction entre le mesh (l'apparence) et la classe (le comportement/code) est le principe même de la programmation orientée objet dans le jeu vidéo.
4.  **L'importance de la documentation :** Comme le souligne le tutoriel, fouiller dans les assets natifs du moteur pour comprendre comment les développeurs originaux ont configuré leurs armes reste la meilleure méthode d'apprentissage pour un développeur junior.

{{< footer >}}