# Job Match AI

AI-powered API for comparing resumes with job descriptions.

The project analyzes technical skills, detects missing skills, calculates a skill match score, and uses sentence embeddings to estimate semantic similarity between a resume and a job description.

## Features

- Resume and job description comparison
- Technical skill extraction
- Skill aliases and normalization
- Missing skill detection
- Skill match score
- Semantic similarity using sentence embeddings
- Overall match score
- REST API with FastAPI
- Automated tests with pytest
- Docker support
- GitHub Actions CI

## Tech Stack

- Python 3.10
- FastAPI
- Pydantic
- Sentence Transformers
- PyTorch
- pytest
- Docker
- GitHub Actions

## How It Works

The final score is calculated from two parts:

- 70% — technical skill match
- 30% — semantic similarity between the resume and the job description

Example:

```text
Skill match: 60%
Semantic similarity: 80%

Overall score:
60 * 0.7 + 80 * 0.3 = 66%
```

The project also supports aliases such as:

```text
Postgres -> PostgreSQL
sklearn -> scikit-learn
ML -> machine learning
Torch -> PyTorch
```

## API

### Health Check

```http
GET /health
```

Response:

```json
{
  "status": "ok"
}
```

### Analyze Resume

```http
POST /analyze
```

Example request:

```json
{
  "resume_text": "Python developer with experience in Git, SQL, pandas and machine learning.",
  "job_description": "We are looking for a Junior Python Developer with Python, Git, SQL, Docker, FastAPI and machine learning knowledge."
}
```

Example response:

```json
{
  "skill_match_score": 67,
  "semantic_similarity": 78,
  "overall_score": 70,
  "matched_skills": [
    "git",
    "machine learning",
    "python",
    "sql"
  ],
  "missing_skills": [
    "docker",
    "fastapi"
  ]
}
```

## Project Structure

```text
job-match-ai/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── matcher.py
│   ├── models.py
│   └── semantic.py
│
├── tests/
│   └── test_api.py
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── .dockerignore
├── .gitignore
├── Dockerfile
├── README.md
├── requirements.txt
└── requirements-docker.txt
```

## Run Locally

Clone the repository:

```bash
git clone https://github.com/Zeeero-nobot/job-match-ai.git
cd job-match-ai
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the API:

```bash
python -m uvicorn app.main:app --reload
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## Run Tests

```bash
python -m pytest
```

## Run with Docker

Build the image:

```bash
docker build -t job-match-ai .
```

Run the container:

```bash
docker run --rm -p 8000:8000 job-match-ai
```

Then open:

```text
http://127.0.0.1:8000/docs
```

## Continuous Integration

GitHub Actions automatically runs the test suite on:

- every push to `main`
- every pull request to `main`

## Current Limitations

- Skill extraction is based on a predefined skill dictionary.
- The current scoring weights are fixed.
- Resume files such as PDF or DOCX are not supported yet.
- The project currently exposes an API only and does not include a frontend.

## Future Improvements

- PDF resume upload
- DOCX parsing
- Larger skill database
- Configurable scoring weights
- Improved NLP-based skill extraction
- Web interface
- Deployment to a cloud platform

## Author

Volodymyr

Computer Science / Artificial Intelligence student at the Institute for Applied System Analysis, Igor Sikorsky Kyiv Polytechnic Institute.