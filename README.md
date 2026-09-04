# 🎬 LUKI – AI-Powered Movie Recommendation System

LUKI is a full-stack AI-powered movie recommendation system designed to help users discover movies based on their interests and the movies they already enjoy. The application combines a modern interactive web interface, a Python-based FastAPI backend, machine learning techniques, external movie data, and a local Large Language Model (LLM) to create a more intelligent and engaging movie discovery experience.

Instead of simply displaying a list of popular movies, LUKI allows users to search for a movie and receive recommendations based on similarity between movies. The recommendation engine analyzes available movie information and identifies movies that are most relevant to the user's selected title. The results are then presented through an interactive interface where users can explore recommendations, filter movies by genre, revisit recent searches, and view additional information.

One of the main features of LUKI is **"LUKI's Take"**, an AI-generated explanation system that provides a natural-language explanation of why a particular movie may be relevant to the user's interests. This feature integrates a locally running Large Language Model through LM Studio, allowing the application to combine traditional recommendation techniques with generative AI.

The project was developed as a hands-on exploration of how machine learning systems, REST APIs, frontend development, external APIs, and Large Language Models can be integrated into a single full-stack application.

---

## 🎯 Project Objective

The primary objective of LUKI is to build an intelligent movie discovery platform that goes beyond a traditional search interface.

The system aims to:

- Help users discover movies similar to the ones they already enjoy.
- Demonstrate the practical implementation of a movie recommendation engine.
- Integrate machine learning techniques into a real-world web application.
- Provide AI-generated explanations for movie recommendations.
- Create a visually appealing and interactive user interface.
- Connect a frontend application with a Python REST API backend.
- Integrate external movie data and posters using the TMDB API.
- Explore the integration of local Large Language Models into web applications.

LUKI demonstrates how multiple technologies can work together to solve a practical recommendation problem.

---

# 🧠 How LUKI Works

The overall workflow of the application follows the architecture below:

```text
User
  │
  │ Searches for a movie
  ▼
┌───────────────────────────────┐
│           Frontend            │
│   HTML • CSS • JavaScript     │
└───────────────┬───────────────┘
                │
                │ API Request
                ▼
┌───────────────────────────────┐
│        FastAPI Backend        │
│            Python             │
└───────────────┬───────────────┘
                │
        ┌───────┴────────┐
        │                │
        ▼                ▼
┌──────────────┐   ┌───────────────┐
│Recommendation│   │ AI Explanation│
│    Engine    │   │     Engine    │
└──────┬───────┘   └───────┬───────┘
       │                   │
       ▼                   ▼
Movie Similarity      Qwen / Local LLM
       │                   │
       └─────────┬─────────┘
                 │
                 ▼
        Movie Recommendations
        + AI Explanation
