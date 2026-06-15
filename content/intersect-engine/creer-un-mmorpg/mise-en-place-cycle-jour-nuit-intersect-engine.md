---
title: "16. Mise en place d'un cycle jour/nuit dynamique"
weight: 16
prev_url: "/intersect-engine/creer-un-mmorpg/creer-systeme-recolte-ressources-intersect-engine/"
next_url: "/intersect-engine/creer-un-mmorpg/creer-lumieres-dynamiques-animees-intersect-engine/"
date: 2023-10-27
categories: ['Archive']
tags: ['Intersect Engine', 'Game Development', 'MMORPG', 'Tutoriel']
---

Découvrez comment dynamiser l'immersion de votre MMORPG en configurant un cycle jour/nuit automatisé grâce au Time Editor d'Intersect Engine.

{{< youtube-rgpd "MbZ9VSXxe4U" >}}

### Résumé des notions clés

*   **Accès à l'éditeur :** Le paramétrage du temps se situe dans le `Content Editor`, sous l'onglet `Time Editor`.
*   **Gestion du Time Rate :** 
    *   La valeur `1` correspond au temps réel.
    *   Une valeur supérieure à 1 accélère le cycle (ex: 1000 pour un test rapide).
    *   Une valeur entre 0 et 1 ralentit le cycle.
*   **Personnalisation visuelle :** 
    *   **Color Overlay :** Permet de teinter l'écran (bleu ciel pour le jour, bleu sombre pour la nuit).
    *   **Brightness :** Ajuste l'opacité de la teinte pour simuler l'intensité lumineuse.
*   **Synchronisation :** Possibilité de synchroniser l'heure du jeu avec celle du serveur réel via l'option `Sync With Server`.
*   **Bonne pratique :** Il est recommandé de redémarrer le serveur après avoir modifié ces paramètres pour garantir la bonne prise en compte des changements par le client.

### Ce qui reste d'actualité aujourd'hui

Bien que les versions d'Intersect Engine évoluent, le fonctionnement du `Time Editor` reste un pilier fondamental pour la gestion de l'ambiance dans vos projets. La capacité à manipuler le `Time Rate` est toujours une technique indispensable pour tester rapidement vos transitions visuelles sans attendre des cycles complets de 24 heures. De plus, la gestion des teintes (overlays) reste la méthode la plus efficace pour créer une atmosphère cohérente avant d'implémenter des systèmes d'éclairage plus complexes comme les sources lumineuses dynamiques (torches, lampadaires), qui seront le sujet de notre prochaine étape.

{{< footer >}}