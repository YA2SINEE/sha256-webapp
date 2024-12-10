# SHA256 Web Application Kaddouri Yassine M2 TNSID

## But du projet

Ce projet consiste en une application web simple permettant de générer un hash SHA256 à partir d'une chaîne de caractères fournie par l utilisateur. L'application expose une API REST via Flask et une interface web permettant de visualiser l'historique des chaînes de caractères traitées, ainsi que leurs résultats en hash SHA256. Le tout est stocké dans un fichier `data.json` pour conserver un historique des requêtes.

L objectif de ce projet est de démontrer l'utilisation de Docker pour déployer une application Flask avec un stockage de données local, ainsi que l'intégration de services web (API et interface utilisateur).

---

## Fonctionnalités

- Génération de hash SHA256 via une API REST.
- Visualisation des chaînes et de leurs hashes sur une interface web.
- Stockage des résultats dans un fichier JSON local.
- Déploiement facile via Docker.

---

## Prérequis

- **Docker** : Assurez-vous que Docker est installé sur votre machine. Vous pouvez suivre les instructions d installation sur le [site officiel de Docker](https://docs.docker.com/get-docker/).

---

## Télécharger et exécuter le projet

### 1. Cloner ce repository

Tout d abord, vous devez cloner le projet depuis GitHub ou Docker Hub (si vous préférez utiliser l image Docker directement).

**Via GitHub** :
```bash
git clone https://github.com/YA2SINEE/sha256-webapp.git
cd sha256-webapp

**Via Docker Hub** :
docker pull ya2sinee/sha256-webapp:v1

2. Construire l image Docker (si vous avez cloné le projet)
Si vous avez cloné le repository Git, vous devez maintenant construire l image Docker avec la commande suivante :

docker build -t sha256-webapp .

3. Lancer l application
Une fois l image construite ou téléchargée, vous pouvez lancer l application via Docker en utilisant cette commande :

docker run -d -p 5001:5000 -v "$(pwd)/data.json:/app/data.json" sha256-webapp

Cela exécutera l application sur le port 5001 et sauvegardera les données dans le fichier data.json à l endroit où vous avez cloné le projet.

---

Utilisation

1. Générer un hash SHA256 via l API REST
Vous pouvez envoyer une requête POST à l API pour générer un hash SHA256 à partir d une chaîne de caractères. Par exemple, pour la chaîne "hello", vous pouvez utiliser curl avec la commande suivante :

curl -X POST -H "Content-Type: application/json" -d '{"string":"hello"}' http://localhost:5001/hash


Cela renverra un hash SHA256 de la chaîne "hello" et l ajoutera au fichier data.json.

2. Visualiser l historique sur l interface Web

Une fois l application lancée, vous pouvez accéder à l interface web pour voir l historique des chaînes et leurs hashes générés. Ouvrez simplement votre navigateur et rendez-vous à l adresse suivante :

http://127.0.0.1:5001

L interface affichera les chaînes traitées et leurs hashes associés.

---

Résolution des problèmes

Port déjà utilisé : Si vous obtenez une erreur comme "port déjà alloué", cela signifie qu une autre application utilise déjà le port 5001. Vous pouvez changer le port en modifiant la commande docker run pour utiliser un autre port. 
Par exemple :

docker run -d -p 5002:5000 -v "$(pwd)/data.json:/app/data.json" sha256-webapp

Fichier data.json vide : Si vous ne voyez pas de données dans data.json, assurez-vous que vous avez bien envoyé une requête POST à l API. Vérifiez également que le fichier data.json est bien dans le bon répertoire et est accessible.

---
