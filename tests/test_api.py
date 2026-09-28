from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok"
    }


def test_analyze():
    response = client.post(
        "/analyze",
        json={
            "resume_text": "Python Git SQL",
            "job_description": "Python Git SQL Docker FastAPI",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["match_score"] == 60
    assert "python" in data["matched_skills"]
    assert "docker" in data["missing_skills"]


def test_skill_aliases():
    response = client.post(
        "/analyze",
        json={
            "resume_text": (
                "I have experience with Python, "
                "Postgres, sklearn and ML."
            ),
            "job_description": (
                "We need Python, PostgreSQL, "
                "scikit-learn and machine learning."
            ),
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["match_score"] == 100
    assert "postgresql" in data["matched_skills"]
    assert "scikit-learn" in data["matched_skills"]
    assert "machine learning" in data["matched_skills"]