from functools import lru_cache

from sentence_transformers import SentenceTransformer, util


MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


@lru_cache(maxsize=1)
def get_model() -> SentenceTransformer:
    return SentenceTransformer(MODEL_NAME)


def calculate_semantic_similarity(
    resume_text: str,
    job_description: str,
) -> int:
    model = get_model()

    embeddings = model.encode(
        [resume_text, job_description],
        convert_to_tensor=True,
        normalize_embeddings=True,
    )

    similarity = util.cos_sim(
        embeddings[0],
        embeddings[1],
    ).item()

    similarity = max(0.0, min(1.0, similarity))

    return round(similarity * 100)