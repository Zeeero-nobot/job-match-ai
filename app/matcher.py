import re


SKILL_ALIASES = {
    "python": ["python"],
    "fastapi": ["fastapi"],
    "django": ["django"],
    "flask": ["flask"],

    "git": ["git"],
    "github": ["github"],

    "docker": ["docker"],
    "linux": ["linux"],

    "sql": ["sql"],
    "postgresql": ["postgresql", "postgres"],
    "mysql": ["mysql"],

    "numpy": ["numpy"],
    "pandas": ["pandas"],

    "pytorch": ["pytorch", "torch"],
    "tensorflow": ["tensorflow"],

    "scikit-learn": [
        "scikit-learn",
        "sklearn",
        "scikit learn",
    ],

    "machine learning": [
        "machine learning",
        "ml",
    ],

    "deep learning": [
        "deep learning",
        "dl",
    ],
}


def normalize_text(text: str) -> str:
    text = text.lower()

    text = re.sub(
        r"[^a-z0-9+#.\-\s]",
        " ",
        text,
    )

    text = re.sub(
        r"\s+",
        " ",
        text,
    )

    return text.strip()


def contains_skill(
    text: str,
    alias: str,
) -> bool:
    pattern = rf"\b{re.escape(alias)}\b"

    return re.search(
        pattern,
        text,
        flags=re.IGNORECASE,
    ) is not None


def extract_skills(text: str) -> set[str]:
    text = normalize_text(text)

    found_skills = set()

    for skill, aliases in SKILL_ALIASES.items():
        for alias in aliases:
            if contains_skill(text, alias):
                found_skills.add(skill)
                break

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