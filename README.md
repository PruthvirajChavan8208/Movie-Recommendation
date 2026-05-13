# 🎬 Movie Recommendation System

An interactive web application that suggests movies based on user preferences. This project uses Content-Based Filtering and Natural Language Processing (NLP) to find similarities between movie tags, genres, and descriptions.

## 🚀 Live Demo
Click here to view the Live App-->https://movie-recommendation-r2bnku4suubds2xmq3zk36.streamlit.app/

## 💡 How it Works
The system analyzes movie titles and features from the cleaned_data.csv. It uses a Similarity Matrix (stored in similarity.pkl) to calculate the mathematical "closeness" between movies. When a user enters a movie title, the app:
1. Finds the index of that movie in the dataset.
2. Accesses the pre-computed similarity scores for that specific index.
3. Sorts and displays the Top 5 most similar movies.

## 🛠️ Features
- Smart Search: Search for any movie from the 5,000+ movie dataset.
- Fast Performance: Uses a pre-computed similarity matrix for instant results.
- Interactive Interface: Built with Streamlit for a clean and professional user experience.

## 🧰 Tech Stack
- Language: Python
- Libraries: Streamlit, Pandas, NumPy, Pickle
- Technique: Content-Based Filtering (Cosine Similarity)
- Deployment: Streamlit Cloud

## 📁 Project Structure
- app.py: The main application logic and Streamlit UI.
- cleaned_data.csv: The processed movie dataset.
- similarity.pkl: The similarity matrix file (Approx 180MB).
- requirements.txt: Necessary Python packages for deployment.

## 🔧 Installation & Local Setup
1. Clone this repository to your local machine.
2. Install the required libraries:
   `bash
   pip install -r requirements.txt
