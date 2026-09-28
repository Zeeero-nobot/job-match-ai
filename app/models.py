from pydantic import BaseModel, Field


class MatchRequest(BaseModel):
    resume_text: str = Field(
        min_length=1,
        description="Resume text",
    )

    job_description: str = Field(
        min_length=1,
        description="Job description text",
    )


class MatchResponse(BaseModel):
    skill_match_score: int
    semantic_similarity: int
    overall_score: int
    matched_skills: list[str]
    missing_skills: list[str]