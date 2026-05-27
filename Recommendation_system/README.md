# 🎬 Movie Recommendation System

A full-stack AI-powered movie recommendation web application built using Flask and Machine Learning.
It suggests similar movies using TF-IDF + Cosine Similarity and provides a modern Netflix-like UI experience with search, trending section,
auto-suggestions, watchlist, and movie details page.

---

# 🚀 Features

- 🔎 Smart movie search system  
- 🧠 AI-based recommendations using TF-IDF + Cosine Similarity  
- ⚡ Auto-suggestions while typing  
- 🔥 Trending movies section  
- 🎬 Click movie → details page  
- 🔐 Login system (basic session-based authentication)  
- ⭐ Watchlist feature  
- 🎨 Netflix-style dark UI  
- 📱 Fully responsive design  
- ⚡ Fast Flask backend API  

---

# 🧠 How It Works

1. User searches a movie name  
2. Movie text is converted into numerical vectors using TF-IDF  
3. Cosine similarity calculates similarity between movies  
4. Top matching movies are returned as recommendations   

---

# 🛠️ Tech Stack

Frontend: HTML, CSS, JavaScript  
Backend: Flask (Python)  
Machine Learning: Scikit-learn (TF-IDF, Cosine Similarity)  
Dataset: CSV file (movies dataset)  

---

# 📁 Project Structure

movie-recommender/
│
├── app.py
├── movies.csv
├── users.json
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── movie.html
│
├── static/
│   ├── style.css
│   ├── script.js
│
└── README.md

---

# ⚙️ Installation & Setup

## 1. Clone the repository
git clone https://github.com/Shravya886/task1-movie-recommendation-system.git
cd movie-recommender


## 2. Install dependencies
pip install flask pandas scikit-learn

---

## 3. Run the application
python app.py

---

## 4. Open in browser
http://127.0.0.1:5000/

---

# 🎯 Features Explained

🧠 Recommendation Engine  
Uses TF-IDF Vectorization + Cosine Similarity to find similar movies based on genre/text similarity.

🔎 Auto-Suggestions  
Live search feature that suggests movies while typing using Flask API.

🔥 Trending Section  
Displays popular or randomly selected movies dynamically.

🎬 Movie Details Page  
Click any movie card to view full details like title, year, genre.

---

# 🎨 UI Design

- Netflix-inspired dark theme  
- Grid-based movie cards  
- Hover animations with smooth transitions  
- Highlighted search results  
- Fully responsive mobile-friendly design  

---

# 🚀 Future Improvements

- 🎥 Trailer integration using YouTube API  
- 🤖 Hybrid recommendation system (collaborative filtering + content-based)  
- ☁️ Database integration (MongoDB / Firebase)  
- 📱 Mobile-first UI redesign  
- ❤️ Personalized recommendations based on user history  
- 🔐 Advanced authentication system (JWT/OAuth)  

---

# 👨‍💻 Author

Shravya Mididoddi

---

# 📜 License

This project is open-source and free to use for learning, academic, and portfolio purposes.
