🛡️ README — Projet Keylogger (Version pédagogique et désactivée)
🎯 Objectif du projet
Ce projet a été réalisé dans le cadre d’un exercice pédagogique visant à comprendre la structure d’un keylogger en Python.
L’objectif n’est pas de créer un logiciel malveillant fonctionnel, mais de :

analyser la logique d’un keylogger simple

apprendre à manipuler des fonctions Python (try/except/finally)

comprendre comment les Blue Teams détectent ce type de comportement

documenter un projet technique sur GitHub

développer une réflexion éthique autour de la cybersécurité

Toutes les fonctionnalités potentiellement dangereuses ont été désactivées ou limitées à un cadre strictement éducatif.

🧩 Contexte Blue Team
Les keyloggers sont des logiciels capables d’enregistrer les frappes clavier d’un utilisateur.
Ils sont souvent utilisés pour voler :

des mots de passe

des données bancaires

des messages privés

Dans un contexte Blue Team, il est essentiel de :

comprendre comment un keylogger est structuré

reconnaître ses comportements typiques

savoir où il peut se cacher dans un système

analyser son fonctionnement sans jamais exécuter de code malveillant

Ce projet permet d’acquérir ces compétences en toute sécurité.

🧠 Structure du programme
✔️ key_pressed(key)
Fonction appelée à chaque frappe clavier.
Elle distingue :

les touches normales (key.char)

les touches spéciales (via AttributeError)

Puis elle envoie la donnée à print_data(data).

✔️ print_data(data)
Fonction centrale du projet.
Elle :

affiche la touche pressée

incrémente un compteur global de frappes

enregistre la donnée dans un fichier texte (version pédagogique)

alimente un buffer permettant de détecter le mot « azerty »

✔️ log_data(data)
Fonction qui écrit les frappes dans un fichier log.txt.
Elle utilise le mode "a" (append) pour ajouter les données ligne par ligne.

✔️ start_keylogger()
Fonction principale qui :

affiche un message de démarrage

lance l’écoute du clavier pendant LOGGING_TIME secondes

gère les erreurs éventuelles

affiche un message de fin

🔢 Compteur de frappes
Pour compter le nombre total de frappes depuis le début du programme, j’ai :

créé une variable globale counter = 0

ajouté global counter dans la fonction print_data

incrémenté le compteur avec counter += 1

affiché le nombre total de frappes dans le terminal

Cela permet de suivre l’activité du programme et de comprendre comment un keylogger peut mesurer l’interaction utilisateur.

🔍 Détection du mot « azerty »
Pour détecter si l’utilisateur tape « azerty », j’ai :

créé une liste buffer = []

ajouté chaque touche pressée dans ce buffer

limité le buffer aux 6 dernières frappes

comparé "".join(buffer) avec "azerty"

Si les 6 dernières frappes correspondent au mot, un message est affiché.

Ce mécanisme illustre comment certains malwares recherchent des mots-clés sensibles.

🛑 Version désactivée et sécurisée
Ce projet est une simulation pédagogique.
Il ne constitue pas un keylogger fonctionnel destiné à un usage réel.

aucune donnée sensible n’est collectée

le code est limité à un environnement d’apprentissage

l’objectif est la compréhension, pas l’exploitation

Cette approche respecte les principes éthiques de la cybersécurité.

🧠 Réflexion éthique
La capture de frappes clavier est une activité extrêmement sensible.
Elle peut violer :

la vie privée

la confidentialité

les droits fondamentaux des utilisateurs

En tant que future professionnelle de la cybersécurité, il est essentiel de :

comprendre les risques liés à ces outils

ne jamais exécuter ou diffuser de code malveillant

toujours privilégier une approche défensive

respecter les lois et les bonnes pratiques

Ce projet m’a permis de prendre conscience de la responsabilité associée à ces connaissances.

📚 Ce que j’ai appris
la structure d’un keylogger basique

l’utilisation de try/except/finally

la gestion de fichiers en Python

la détection de motifs dans des frappes clavier

l’importance de l’éthique en cybersécurité

comment documenter un projet sur GitHub

📂 Structure du dépôt
Code
/Keylogger-BlueTeam
    |-- keylogger.py
    |-- README.md
    |-- log.txt (optionnel)
🌙 Conclusion
Ce projet m’a permis de comprendre la logique interne d’un keylogger tout en adoptant une posture Blue Team responsable.
Il constitue une base solide pour poursuivre mon apprentissage en cybersécurité défensive.