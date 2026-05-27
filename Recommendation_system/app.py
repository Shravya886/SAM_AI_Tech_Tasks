from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load dataset
movies = pd.read_csv("movies.csv")
movies["id"] = movies.index
movies["title_lower"] = movies["title"].str.lower()
movies["genre"] = movies["genre"].fillna("")

# TF-IDF
tfidf = TfidfVectorizer(stop_words="english")
matrix = tfidf.fit_transform(movies["genre"])
similarity = cosine_similarity(matrix)


# ---------------- RECOMMENDATION ----------------
def get_recommendations(movie_name):

    movie_name = movie_name.lower().strip()

    if movie_name not in movies["title_lower"].values:
        return None, []

    index = movies[movies["title_lower"] == movie_name].index[0]

    searched_movie = {
        "id": int(index),
        "title": movies.iloc[index]["title"],
        "year": movies.iloc[index]["year"],
        "genre": movies.iloc[index]["genre"]
    }

    distances = similarity[index]

    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])

    recommendations = []

    for i in movie_list[1:7]:
        recommendations.append({
            "id": int(i[0]),
            "title": movies.iloc[i[0]]["title"],
            "year": movies.iloc[i[0]]["year"],
            "genre": movies.iloc[i[0]]["genre"]
        })

    return searched_movie, recommendations


# ---------------- SUGGESTION API ----------------
@app.route("/suggest")
def suggest():
    query = request.args.get("q", "").lower().strip()

    if not query:
        return jsonify({"suggestions": []})

    filtered = movies[movies["title_lower"].str.contains(query)]["title"].head(6)

    return jsonify({"suggestions": filtered.tolist()})


# ---------------- HOME ----------------
@app.route("/", methods=["GET"])
def home():

    movie_name = request.args.get("movie")

    # 🚨 FIX: ignore empty string
    if not movie_name or movie_name.strip() == "":
        return render_template(
            "index.html",
            searched_movie=None,
            recommendations=[],
            movie_name=""
        )

    searched_movie, recommendations = get_recommendations(movie_name)

    return render_template(
        "index.html",
        searched_movie=searched_movie,
        recommendations=recommendations,
        movie_name=movie_name
    )


# ---------------- MOVIE PAGE ----------------
@app.route("/movie/<int:id>")
def movie_detail(id):

    movie = movies.iloc[id]

    return render_template(
        "movie.html",
        movie={
            "id": id,
            "title": movie["title"],
            "year": movie["year"],
            "genre": movie["genre"],
            "description": f"{movie['title']} is a {movie['genre']} film released in {movie['year']}."
        }
    )


if __name__ == "__main__":
    app.run(debug=True)