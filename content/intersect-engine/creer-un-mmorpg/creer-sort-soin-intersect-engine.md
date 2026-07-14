---
title: "18. Créer votre premier sort de soin"
weight: 18
prev_url: "/intersect-engine/creer-un-mmorpg/creer-lumieres-dynamiques-animees-intersect-engine/"
next_url: "/intersect-engine/creer-un-mmorpg/creer-sort-projectile-intersect-engine/"
date: 2023-10-27
categories: ['Archive']
tags: ['Intersect Engine', 'Game Development', 'Tutoriel', 'RPG', 'Spells']
images: ["https://img.youtube.com/vi/Hr_koShCWxY/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/Hr_koShCWxY/maxresdefault.jpg"]
---

Apprendre à gérer les compétences magiques est une étape cruciale pour donner de la profondeur à votre RPG. Dans ce guide, nous explorons comment configurer un sort de soin fonctionnel au sein d'Intersect Engine.

{{< youtube-rgpd "Hr_koShCWxY" >}}

### Les fondamentaux du système de sorts
La création d'un sort dans Intersect Engine repose sur une structure logique allant de la définition technique à l'intégration dans le gameplay :

*   **Le Spell Editor :** C'est ici que tout commence. Vous définissez le type de sort (Combat, Événement), son icône, sa description et, surtout, son comportement.
*   **Targeting (Ciblage) :** Le choix du type de cible est déterminant. Pour un soin, le mode "Single Target, Includes Self" est idéal, car il permet de se soigner soi-même ou de cibler un allié.
*   **Gestion des coûts et délais :**
    *   **Mana Cost :** Indispensable pour équilibrer vos classes.
    *   **Cast Time :** Ajoute une dimension tactique en rendant le lancement vulnérable aux interruptions.
    *   **Cooldown :** Empêche le spam des compétences et force le joueur à gérer ses ressources.
*   **Effets (HP Difference) :** Une valeur positive soigne, tandis qu'une valeur négative inflige des dégâts. Vous pouvez également manipuler d'autres statistiques (défense, mana, etc.).
*   **Apprentissage via Items :** Pour rendre le sort accessible, il doit être lié à un objet (parchemin) que le joueur pourra acheter ou looter, puis apprendre via son livre de sorts (*Spellbook*).

### Ce qui reste d'actualité aujourd'hui
Bien que le moteur évolue, les principes fondamentaux présentés ici restent le socle de tout projet sur Intersect Engine :
1.  **L'équilibrage par les classes :** La réflexion sur les coûts en mana par rapport aux statistiques de base de vos classes (Guerrier vs Mage) est une constante du game design.
2.  **La rigueur du test :** Le moteur étant en développement constant, la règle d'or reste de redémarrer le serveur après chaque modification majeure des sorts pour éviter les comportements erratiques.
3.  **La zone d'effet (Hit Radius) :** Comprendre comment le rayon d'impact affecte non seulement vos alliés mais aussi vos ennemis est essentiel pour éviter des situations de jeu frustrantes (comme soigner un monstre par accident).
4.  **La modularité :** La possibilité de combiner des effets (soin + buff de défense) montre que la puissance d'Intersect réside dans votre capacité à imaginer des synergies complexes plutôt que de simples sorts linéaires.

{{< footer >}}