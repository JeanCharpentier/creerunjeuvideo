---
title: "13. Création d''une Intelligence Artificielle de base"
weight: 13
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['IA', 'Blueprint', 'NavMesh', 'PawnSensing', 'Tutoriel']
images: ["https://img.youtube.com/vi/-8nyKjiCzy0/maxresdefault.jpg"]
---

Dans cet épisode, nous posons les bases de l'intelligence artificielle pour notre projet "Kawaii Slender". L'objectif est simple : permettre à notre entité de détecter le joueur lorsqu'il entre dans son champ de vision et de le poursuivre activement. Pour ce faire, nous allons utiliser le système de navigation intégré d'Unreal Engine 4 et le composant `PawnSensing`.

{{< youtube-rgpd "-8nyKjiCzy0" >}}

### Résumé des étapes clés
*   **Mise en place du NavMeshBoundsVolume** : Ajout et redimensionnement du volume pour définir la zone de navigation autorisée pour l'IA.
*   **Visualisation** : Utilisation de la touche `P` pour vérifier les zones navigables (en vert).
*   **Création du Blueprint IA** : Duplication du `FirstPersonCharacter` pour créer le `BP_Slender`, nettoyage du graphe et suppression de la caméra.
*   **Composant PawnSensing** : Ajout du composant de détection et réglage du champ de vision (`PeripheralVisionAngle`).
*   **Logique de poursuite** : Utilisation du nœud `OnSeePawn` couplé à un `Cast` vers le joueur et la fonction `AI MoveTo` pour déclencher le déplacement vers la cible.

### Ce qui reste d'actualité aujourd'hui
Bien que les versions récentes d'Unreal Engine (UE5) aient introduit le système **Mass Entity** ou des outils plus avancés comme les **Behavior Trees** (Arbres de comportement) et les **Environment Query Systems (EQS)**, les principes fondamentaux abordés ici restent le socle de toute IA :
1.  **Le NavMesh** : Il demeure l'outil indispensable pour calculer les chemins en temps réel dans n'importe quel environnement 3D.
2.  **PawnSensing** : Bien que souvent remplacé par le composant `AIPerception` (plus performant et flexible), le `PawnSensing` reste une excellente porte d'entrée pour comprendre comment une IA "voit" ou "entend" le monde.
3.  **AI MoveTo** : Cette fonction reste la méthode la plus directe pour déplacer un personnage non-joueur vers une destination spécifique via le système de navigation.

Pour des projets plus complexes, il est recommandé de migrer vers les **Behavior Trees** afin de séparer la logique de décision de l'exécution du mouvement, ce qui permet de créer des comportements beaucoup plus riches (patrouille, recherche, attaque, etc.).

{{< footer >}}