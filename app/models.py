from pydantic import BaseModel


class MatchRequest(BaseModel):
    resume_text: str
    job_description: str


class MatchResponse(BaseModel):
    match_score: int
    matched_skills: list[str]
    missing_skills: list[str]