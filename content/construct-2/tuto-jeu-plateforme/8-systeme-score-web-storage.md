---
title: "8. Système de score et persistance des données" 
date: 2026-06-13
weight: 10
categories: ["Archive"]
tags: ["Construct 2", "Tutoriel", "Game Dev", "Score", "Web Storage"]
prev_url: "/construct-2/tuto-jeu-plateforme/7-gestion-vie-score"
next_url: "/construct-2/tuto-jeu-plateforme/patch-mise-a-jour-webstorage"
images: ["https://img.youtube.com/vi/BGQoPxLLeF0/maxresdefault.jpg"]
---

> **Note :** Cet article détaille la création d'un système de score global et par niveau, ainsi que la sauvegarde de session via l'objet *Web Storage* de Construct 2.

{{< youtube-rgpd "BGQoPxLLeF0" >}}

### 1. Configuration des variables globales
Dans votre feuille d'événements `ES Menu`, créez deux variables globales (clic droit > Add global variable) :
*   **score_actuel** (nombre, initialisé à 0) : Pour le score global de la session.
*   **score_niveau** (nombre, initialisé à 0) : Pour le suivi du score accumulé dans le niveau en cours.

### 2. Intégration du Web Storage
Pour conserver les données entre les différents layouts :
1.  Ajoutez l'objet **Web Storage** dans votre projet (disponible pour tous les layouts).
2.  Dans `ES Menu` sur l'événement `System > On start of layout` :
    *   Action : `Web Storage > Set local value`.
    *   **Key :** `"WS_score_actuel"`
    *   **Value :** `score_actuel`
3.  Toujours dans `On start of layout`, mettez à jour votre objet texte `T_score_actuel` pour afficher la valeur stockée :
    *   Action : `T_score_actuel > Set text` à `WebStorage.LocalValue("WS_score_actuel")`.

### 3. Gestion du score dans le jeu (ES Joueur)
Le score doit évoluer en fonction des actions du joueur et des changements de niveau :

*   **Initialisation :** Au lancement du niveau (`On start of layout`), synchronisez la variable d'instance du joueur avec le score du niveau :
    *   Action : `S_Perso > Set value (Jscore)` à `score_niveau`.
*   **Changement de niveau :** Avant de changer de layout, mettez à jour la variable globale :
    *   Action : `System > Set value (score_niveau)` à `S_Perso.Jscore`.
*   **Gestion de la mort :** Lors de chaque condition de mort (chute, ennemi, pics), enregistrez le score actuel :
    *   Action : `System > Set value (score_actuel)` à `S_Perso.Jscore`.

### 4. Réinitialisation
Pour garantir que le score repart à zéro lors d'un retour au menu principal après une mort :
*   Dans `ES Menu`, ajoutez une action dans `On start of layout` :
    *   Action : `System > Set value (score_niveau)` à `0`.

{{< footer >}}