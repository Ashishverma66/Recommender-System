# 🎬 Movie Recommender System

A content-based movie recommendation system that suggests movies similar to a user's favorite based on key features like genre, cast, crew, keywords, and more. This project leverages NLP and machine learning techniques to create a scalable and accurate recommender.

---

## 📌 Overview

This project uses the TMDB 5000 Movie Dataset to build a recommender system that:

- Combines multiple features into a single text field ("tags")
- Applies text vectorization and similarity scoring
- Returns the top 5 similar movies
- (Optional) Uses TMDB API to fetch movie posters

---

## 🧠 Core Concepts

- **Content-Based Filtering** using metadata
- **Vectorization** with `CountVectorizer`
- **Cosine Similarity** to measure movie similarity
- **Pickling** for model reuse and fast loading

---

## 📁 Project Structure

