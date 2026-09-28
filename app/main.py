from fastapi import FastAPI

from app.matcher import calculate_match
from app.models import MatchRequest, MatchResponse


app = FastAPI(
    title="Job Match AI",
    description="API for comparing resumes with job descriptions",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "Job Match AI is running"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.post("/analyze", response_model=MatchResponse)
def analyze(request: MatchRequest):
    return calculate_match(
        request.resume_text,
        request.job_description,
    )