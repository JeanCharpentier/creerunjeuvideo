---
title: "37. Personnalisation des icônes et déploiement final sur Google Play"
weight: 37
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Android', 'Google Play', 'Mobile', 'Packaging', 'Tutoriel']
images: ["https://img.youtube.com/vi/gJd4bnrbn9k/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/gJd4bnrbn9k/maxresdefault.jpg"]
---

Dans cet épisode, nous abordons une étape cruciale pour tout développeur mobile sous Unreal Engine 4 : la préparation de votre build pour le Google Play Store. Il est impératif de remplacer les icônes par défaut fournies par le moteur, sous peine de voir votre application rejetée par les systèmes automatisés de Google pour violation de propriété intellectuelle (les icônes par défaut étant liées à *Unreal Tournament 3*).

{{< youtube-rgpd "gJd4bnrbn9k" >}}

### Résumé des étapes clés
*   **Remplacement des icônes :** Accédez aux *Project Settings > Platforms > Android* pour remplacer les icônes par défaut par vos propres assets (respectez scrupuleusement les formats PNG et les dimensions indiquées).
*   **Gestion des versions :** N'oubliez pas d'incrémenter le `Store Version` dans les paramètres Android avant chaque nouveau packaging.
*   **Packaging :** Relancez le processus de compilation (*File > Package Project > Android*) pour générer les nouveaux fichiers APK et OBB.
*   **Google Play Console :** Mettez à jour votre version Alpha en supprimant l'ancienne version et en téléchargeant les nouveaux fichiers.
*   **Configuration des services :** Complétez impérativement la fiche de votre jeu dans les "Services de jeux" (description, icônes, images de bannière) pour chaque langue ajoutée.
*   **Publication :** Une fois les voyants au vert, validez la publication. Attention : certains éléments deviennent définitifs (comme les succès) une fois le jeu publié.

### Ce qui reste d'actualité aujourd'hui
Bien que les interfaces de la Google Play Console évoluent régulièrement, les principes fondamentaux abordés ici restent des piliers du développement mobile :
1.  **La conformité des assets :** L'utilisation d'icônes personnalisées est toujours une exigence stricte pour éviter le rejet automatique de vos builds.
2.  **Le versioning :** La gestion rigoureuse des numéros de version (`Version Code`) est indispensable pour que le Play Store accepte vos mises à jour.
3.  **La préparation des services :** La configuration des "Services de jeux" (Play Games Services) demande toujours une attention particulière sur les métadonnées (descriptions, localisations) avant la mise en ligne.
4.  **L'irréversibilité des données :** La règle selon laquelle les succès (Achievements) ne peuvent plus être supprimés une fois le jeu publié est une constante pour protéger la progression des joueurs.

{{< footer >}}