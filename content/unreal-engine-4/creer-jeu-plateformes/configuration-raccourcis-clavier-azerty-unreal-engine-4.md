---
title: "5. Configuration des raccourcis clavier (AZERTY) et des contrôles"
weight: 5
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Configuration', 'Interface', 'Input', 'Débutant']
---

Bienvenue dans ce cinquième volet de notre série sur Unreal Engine 4. Travailler sur un moteur de jeu demande une aisance totale avec ses outils. Par défaut, Unreal Engine est configuré pour les claviers QWERTY, ce qui peut être un frein majeur pour les développeurs utilisant un clavier AZERTY. Dans cet article, nous allons configurer l'éditeur et les paramètres de votre projet pour une expérience de navigation fluide.

{{< youtube-rgpd "7leHNEr5um8" >}}

### Au programme de cet épisode :

*   **Optimisation de l'interface :** Apprendre à organiser ses fenêtres (Editor Preferences) pour une meilleure visibilité, notamment sur écran unique.
*   **Navigation dans le Viewport :** Remappage complet des touches de déplacement (ZQSD) pour correspondre aux standards français.
*   **Configuration des entrées (Input) :** Modification des *Action Mappings* et *Axis Mappings* dans les *Project Settings* pour que votre personnage réponde correctement aux touches AZERTY.
*   **Workflow de test :** Utilisation de la fenêtre "New Editor Window" pour séparer l'aperçu du jeu de l'éditeur et faciliter le débogage.

### Ce qui reste d'actualité aujourd'hui

Bien que les versions récentes d'Unreal Engine (UE5) aient évolué, les fondamentaux abordés ici restent cruciaux :

1.  **La gestion des Input :** La logique des *Axis Mappings* (pour les mouvements continus comme ZQSD) et des *Action Mappings* (pour les actions ponctuelles comme le saut) est le socle de la gestion des contrôles dans Unreal Engine. Même avec l'arrivée du système *Enhanced Input* dans les versions plus récentes, comprendre la hiérarchie des axes reste indispensable.
2.  **L'ergonomie de travail :** La personnalisation de l'interface via les *Editor Preferences* est une pratique recommandée pour tous les développeurs. Savoir détacher les fenêtres de prévisualisation permet de mieux surveiller les *Blueprints* en temps réel pendant que le jeu tourne.
3.  **La gestion des périphériques :** Le nettoyage des entrées inutiles (comme les contrôles VR par défaut si vous n'en avez pas besoin) est une bonne habitude pour garder un projet propre et éviter les conflits de touches.

{{< footer >}}