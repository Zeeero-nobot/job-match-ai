SKILLS = {
    "python",
    "fastapi",
    "django",
    "flask",
    "git",
    "github",
    "docker",
    "linux",
    "sql",
    "postgresql",
    "mysql",
    "numpy",
    "pandas",
    "pytorch",
    "tensorflow",
    "scikit-learn",
    "machine learning",
    "deep learning",
}


def extract_skills(text: str) -> set[str]:
    text = text.lower()

    found_skills = {
        skill
        for skill in SKILLS
        if skill in text
    }

    return found_skills


def calculate_match(
    resume_text: str,
    job_description: str,
) -> dict:
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    matched_skills = resume_skills & job_skills
    missing_skills = job_skills - resume_skills

    if not job_skills:
        score = 0
    else:
        score = round(
            len(matched_skills)
            / len(job_skills)
            * 100
        )

    return {
        "match_score": score,
        "matched_skills": sorted(matched_skills),
        "missing_skills": sorted(missing_skills),
    }