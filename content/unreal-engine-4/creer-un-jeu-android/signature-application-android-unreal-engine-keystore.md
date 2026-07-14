---
title: "32. Signature de votre application Android pour le Google Play Store"
weight: 32
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Android', 'Google Play Store', 'Keystore', 'Déploiement']
images: ["https://img.youtube.com/vi/VIe0vEJY6pY/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/VIe0vEJY6pY/maxresdefault.jpg"]
---

Dans cet épisode, nous abordons une étape cruciale pour tout développeur souhaitant publier son jeu sur le Google Play Store : la signature de l'application. Pour qu'un projet Unreal Engine soit reconnu et accepté par Google, il doit être signé numériquement via un fichier "Keystore".

{{< youtube-rgpd "VIe0vEJY6pY" >}}

### Résumé de la procédure
*   **Utilisation de l'invite de commande (CMD) :** Accès via `Windows + R` puis `cmd`.
*   **Navigation vers le JDK :** Utilisation de la commande `cd` pour atteindre le répertoire `bin` du Java Development Kit (JDK).
*   **Génération du Keystore :** Utilisation de l'outil `keytool` avec les paramètres de chiffrement RSA (2048 bits) et une validité de 10 000 jours.
*   **Renseignement des métadonnées :** Saisie des informations d'identité (nom, organisation, pays) nécessaires à la certification.
*   **Intégration au projet :** Déplacement du fichier `.keystore` généré dans le dossier `Build/Android` de votre projet Unreal Engine.
*   **Configuration dans l'Editor :** Renseignement des champs dans *Project Settings > Platforms > Android > Distribution Signing*.
*   **Packaging :** Activation de l'option *For Distribution* dans les paramètres de packaging pour préparer le build final.

### Ce qui reste d'actualité aujourd'hui

Bien que cet épisode utilise des versions plus anciennes d'Unreal Engine et du NVPAC, les principes fondamentaux de la signature Android restent identiques :

1.  **La nécessité du Keystore :** Google exige toujours un certificat de signature pour identifier le développeur et garantir l'intégrité de l'APK/AAB.
2.  **L'outil Keytool :** Il reste l'outil standard fourni avec le JDK pour gérer les clés de signature.
3.  **La structure des paramètres :** Dans les versions récentes d'Unreal Engine (UE5), l'emplacement des paramètres de signature dans les *Project Settings* est resté très similaire, bien que l'interface ait été légèrement modernisée.
4.  **Le mode "Distribution" :** L'option *For Distribution* est toujours indispensable pour générer un build prêt à être soumis à la console Google Play, empêchant l'utilisation des clés de debug par défaut.

*Note : Assurez-vous de conserver précieusement votre fichier Keystore et vos mots de passe. Si vous les perdez, vous ne pourrez plus mettre à jour votre application sur le Play Store.*

{{< footer >}}