import os
import sys
from fastapi.testclient import TestClient


# Configuration du chemin d'import pour pytest lancé depuis la racine du projet
BASE_DIR = os.path.dirname(os.path.abspath(__file__))   # Dossier du fichier test
PROJECT_ROOT = os.path.dirname(BASE_DIR)               # Racine du projet
APP_DIR = os.path.join(PROJECT_ROOT, "app")            # Dossier app/
sys.path.append(APP_DIR)

from main import app
client = TestClient(app)


def test_health_endpoint_status_code():
    """Vérifie que /health retourne le code 200 OK."""
    response = client.get("/health")
    assert response.status_code == 200


def test_health_endpoint_body():
    """Vérifie que /health retourne {"status": "ok"}."""
    response = client.get("/health")
    assert response.json() == {"status": "ok"}

