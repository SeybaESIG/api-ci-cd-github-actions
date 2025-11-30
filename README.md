# **Python CI/CD Pipeline – GitHub Actions**

Ce projet démontre un pipeline CI/CD utilisant GitHub Actions. Il met en place une petite application Python avec FastAPI, des tests automatisés avec Pytest et la construction d’une image Docker. L’objectif est d’avoir un exemple clair, simple et reproductible de workflow CI pour un projet Python moderne.

## **Fonctionnalités**

* Application Python minimaliste (FastAPI)
* Tests automatisés (Pytest)
* Installation Python et dépendances dans le pipeline
* Exécution des tests à chaque push
* Build automatique de l’image Docker
* Structure de projet propre et adaptée au CI/CD

## **Structure du projet**

python-ci-cd-pipeline/
├── app/
│   ├── main.py
│   ├── **init**.py
│   └── requirements.txt
├── tests/
│   └── test_app.py
├── Dockerfile
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
└── README.md

## **Lancer les tests en local**

pip install -r app/requirements.txt
pytest

## **Builder et lancer l'application avec Docker**

docker build -t python-ci-cd-pipeline .
docker run -p 8000:8000 python-ci-cd-pipeline

L’API sera disponible sur :
[http://localhost:8000/health](http://localhost:8000/health)

## **Pipeline GitHub Actions**

Un workflow CI est exécuté automatiquement :

* à chaque push sur la branche main
* à chaque pull request vers main

Il effectue :

1. Installation de Python
2. Installation des dépendances
3. Exécution des tests
4. Construction de l’image Docker
