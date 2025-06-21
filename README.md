## **Movie Recommendation System – Content-Based & Collaborative Filtering**

### Business Problem

In today’s digital world, users are overwhelmed by endless movie options. Without intelligent recommendation systems, they may miss out on films they’d love — reducing satisfaction and platform engagement.

> **How can we recommend the Top 5 movies to a user based on their historical ratings using content-based and collaborative filtering techniques?**

This project uses the MovieLens dataset to build both **content-based** and **collaborative filtering** recommendation systems.

---

### Project Overview

This project creates a **personalized movie recommender system** using:

- **Content-Based Filtering** – recommends movies similar in genre/content to those the user liked.
- **Collaborative Filtering** – recommends movies based on other users with similar tastes.

The goal is to suggest **Top 5 relevant movies** per user.

---

## Business Understanding

###  Objective

Improve user satisfaction by delivering personalized recommendations, just like Netflix or Amazon Prime Video.

###  Scope

- Uses the MovieLens `ml-latest-small` dataset.
- Focuses on **explicit user ratings**.
- Suggests **unseen and potentially interesting movies**.

---

## Data Understanding

The project uses the `ml-latest-small` dataset from MovieLens:

- **100,836 ratings**
- **610 users**
- **9,742 movies**

### Key Files

- `movies.csv` – Movie titles and genres  
- `ratings.csv` – User ratings for movies  
- `tags.csv` – User-generated tags  
- `links.csv` – External IDs for IMDb and TMDb  

---

##  Modeling Approach

### Content-Based Filtering
- Utilizes **TF-IDF vectorization** on movie genres.
- Uses **cosine similarity** to find movies with similar content.
- Recommends movies the user hasn’t rated but are content-wise similar to those they liked.

### Collaborative Filtering
- Creates a **user-item matrix** from ratings.
- Identifies users with similar preferences.
- Recommends movies liked by similar users but unseen by the current user.

---

## Conclusion

- Built a working movie recommendation system using both **content-based** and **collaborative filtering**.
- The system provides **Top 5 personalized suggestions**.
- Results were interpretable and aligned well with expected user interests.
- **Content-based model successfully deployed** as a simple web application using Streamlit.

---

##  What's Next?

-  Add collaborative filtering using a user-item matrix to improve recommendation diversity.
-  Combine content-based and collaborative approaches into a **hybrid recommendation system**.
-  Incorporate additional metadata like **movie tags, summaries, or cast info** to enrich content-based filtering.
-  Explore advanced techniques such as **matrix factorization** or **deep learning models** for enhanced personalization.
