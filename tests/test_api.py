from unittest.mock import patch

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok"
    }


@patch(
    "app.matcher.calculate_semantic_similarity",
    return_value=80,
)
def test_analyze(mock_similarity):
    response = client.post(
        "/analyze",
        json={
            "resume_text": "Python Git SQL",
            "job_description": (
                "Python Git SQL Docker FastAPI"
            ),
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["skill_match_score"] == 60
    assert data["semantic_similarity"] == 80
    assert data["overall_score"] == 66

    assert "python" in data["matched_skills"]
    assert "docker" in data["missing_skills"]


@patch(
    "app.matcher.calculate_semantic_similarity",
    return_value=90,
)
def test_skill_aliases(mock_similarity):
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

    assert data["skill_match_score"] == 100
    assert data["semantic_similarity"] == 90
    assert data["overall_score"] == 97

    assert "postgresql" in data["matched_skills"]
    assert "scikit-learn" in data["matched_skills"]
    assert "machine learning" in data["matched_skills"]


def test_empty_resume_is_rejected():
    response = client.post(
        "/analyze",
        json={
            "resume_text": "",
            "job_description": "Python developer",
        },
    )

    assert response.status_code == 422