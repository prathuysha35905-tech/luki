import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from llm import explain_movie
# Load MovieLens dataset
movies = pd.read_csv(
    "../data/ml-100k/ml-100k/u.item",
    sep="|",
    encoding="latin-1",
    header=None
)

# Keep only Movie ID and Title
movies = movies[[0, 1]]
movies.columns = ["movie_id", "title"]

vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(movies["title"])
similarity = cosine_similarity(tfidf_matrix)


def search_movie(name):
    result = movies[
        movies["title"].str.contains(name, case=False, na=False)
    ]
    return result.head(10).to_dict(orient="records")


def recommend_movie(name):
    result = movies[movies["title"].str.contains(name, case=False, na=False)]

    if result.empty:
        return {"error": "Movie not found"}

    idx = result.index[0]
    selected_title = movies.iloc[idx]["title"]

    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    recommendations = []

    for i, score in scores[1:11]:

        title = movies.iloc[i]["title"]

        # Extract year from title (e.g. Toy Story (1995))
        year = "Unknown"
        if "(" in title and ")" in title:
            year = title.split("(")[-1].replace(")", "")

        recommendations.append({
            "movie_id": int(movies.iloc[i]["movie_id"]),
            "title": title,
            "year": year,
            "genre": "Unknown",
            "score": float(score),
            "reason": "Similar movie based on AI similarity."
        })

    explanation = explain_movie(selected_title, recommendations)

    return {
        "selected_movie": selected_title,
        "recommendations": recommendations,
        "ai_explanation": explanation
    }