# Content Based Movie Recommendation Systems

## Business Problem
In the age of digital content, users are often overwhelmed by thousands of movie choices. Without a guiding system, users may miss out on films they would have enjoyed, leading to reduced satisfaction and platform engagement.

> **How can we accurately recommend the Top 5 movies to a user based on their historical movie ratings using content-based filtering techniques?**

This project aims to build such a recommender system using content based filtering, trained on historical ratings data from MovieLens.

## Project Overview
This project builds a **personalized movie recommendation system** using the **MovieLens dataset** to suggest films based on user ratings.

## Business Understanding
### Objective
To improve user satisfaction and engagement on a movie streaming platform by providing **Top 5 personalised movie recommendations** based on users' past ratings. The goal is to simulate how platforms like Netflix and Prime Video tailor suggestions to each user.

### Scope
This project uses the MovieLens `ml-latest-small` dataset. It focuses on:
- Explicit rating data (0.5 to 5.0 scale).
- Recommending unseen movies to users.

### Success Criteria

| Metric                 | Goal                            |
|------------------------|----------------------------------|
| RMSE / MAE             | Below 1.0                        |
| Recommendation Relevance | Top 5 suggestions match user interests |
| Coverage               | Recommendations generated for most users |
| Scalability            | Can extend to larger datasets or real-world scenarios |

## Data Understanding

The dataset used is the `ml-latest-small` version from MovieLens, containing 100,836 ratings by 610 users across 9,742 movies.

### Key Files:
- `movies.csv` – Contains `movieId`, `title`, `genres`
- `ratings.csv` – Contains `userId`, `movieId`, `rating`, `timestamp`
- `tags.csv`  – Contains user-generated tags
- `links.csv`  – External references (IMDb, TMDb)

### Ratings Data:
- Ratings range from 0.5 to 5.0 in 0.5 increments.
- Explicit feedback format.
- 
## Modelling and Evaluation
The project implemented a content-based movie recommendation system using cosine similarity on TF-IDF vectors of movie genres and descriptions.The system works by understanding what kind of movies a person likes—such as genre or storyline—and then suggesting similar ones they haven’t seen yet. Evaluation was carried out using RMSE and MAE metrics.
## Conclusion
The recommender system demonstrated effective personalized recommendations with good predictive performance. Future improvements could include hybrid approaches combining content and collaborative filtering and integrating user feedback or deep learning models for enhanced accuracy.
