# \# Project 2 — Personalized GenAI Diet Recommender

# 

# A Flask web app that stores user health profiles in SQLite and generates personalized diet plans using the Groq API with LLaMA 3.

# 

# \## Tech Stack

# \- Backend: Python, Flask

# \- Database: SQLite (built-in, no setup needed)

# \- LLM: Groq API (llama-3.3-70b-versatile) — Free

# \- Frontend: HTML, CSS

# \- Version Control: Git, GitHub

# 

# \## Setup and Run

# 

# 1\. Clone the repo

# &#x20;  git clone https://github.com/YOUR-USERNAME/diet-recommender.git

# &#x20;  cd diet-recommender

# 

# 2\. Install dependencies

# &#x20;  pip install flask groq

# 

# 3\. Set your Groq API key (free at console.groq.com)

# &#x20;  set GROQ\_API\_KEY=your-groq-key-here

# 

# 4\. Run the app

# &#x20;  python app.py

# 

# Visit http://localhost:5000 in your browser.

# 

# \## Features

# 

# \### User Profile Management (CRUD)

# \- Create a health profile (name, age, gender, weight, height, activity level, goal, allergies, preferences)

# \- View all saved profiles on the homepage

# \- Delete any profile

# \- Data stored in SQLite (diet.db — auto created on first run)

# 

# \### AI Diet Plan Generation

# \- User profile is loaded as context for every LLM call

# \- User types a question in natural language

# \- Groq LLaMA 3 generates a personalized plan with meals, calories, macros and tips

# \- Quick prompt chips for common queries

# 

# \## Project Structure

# 

# diet\_recommender/

# ├── app.py            # Flask routes

# ├── database.py       # SQLite schema and CRUD helpers

# ├── llm.py            # Prompt builder and Groq API call

# ├── requirements.txt

# └── templates/

# &#x20;   ├── index.html    # Profile listing page

# &#x20;   ├── profile.html  # Create profile form

# &#x20;   └── diet.html     # Ask questions and view plan

# 

# \## LLM Prompt Design

# The prompt in llm.py injects the full user profile as context including BMI calculated on the fly and instructs LLaMA 3 to generate a full day meal plan with 5 meals, approximate calories and macros per meal, allergen free options respecting dietary preferences, and 3 personalized tips aligned to the user goal.

# 

# \## Screenshots

# 

# \### Home Page — Profile Listing

# 

# \### Create Profile Form

# !\[Profile Form](screenshots/profile.png)

# 

# \### Generated Diet Plan

# !\[Diet Plan](screenshots/diet.png)

