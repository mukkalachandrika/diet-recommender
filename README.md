# Project 2 — Personalized GenAI Diet Recommender

A Flask web app that stores user health profiles in SQLite and generates personalized diet plans using the Anthropic Claude API.

## Tech Stack
- **Backend**: Python, Flask
- **Database**: SQLite (via `sqlite3` built-in)
- **LLM**: Anthropic Claude (`claude-sonnet-4-20250514`)
- **Frontend**: HTML, CSS (no frameworks)

## Setup & Run

```bash
# 1. Clone the repo and navigate to the folder
cd diet_recommender

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set your Anthropic API key
export ANTHROPIC_API_KEY=your_key_here   # Mac/Linux
set ANTHROPIC_API_KEY=your_key_here      # Windows

# 4. Run the app
python app.py
```

Visit `http://localhost:5000` in your browser.

## Features

### User Profile Management (CRUD)
- **Create** a health profile (name, age, gender, weight, height, activity level, goal, allergies, preferences)
- **Read** all saved profiles on the homepage
- **Delete** any profile
- Data is stored in `diet.db` (SQLite, auto-created on first run)

### AI Diet Plan Generation
- Profile is loaded as context for every LLM call
- User types a question in natural language (e.g. "give me a full day diet plan")
- Claude generates a personalized plan: meals, calories, macros, and tips
- Quick-prompt chips for common queries

## Project Structure
```
diet_recommender/
├── app.py          # Flask routes
├── database.py     # SQLite schema + CRUD helpers
├── llm.py          # Prompt builder + Anthropic API call
├── requirements.txt
└── templates/
    ├── index.html  # Profile listing page
    ├── profile.html # Create profile form
    └── diet.html   # Ask questions + view plan
```

## LLM Prompt Design
The prompt in `llm.py` injects the full user profile (BMI calculated on the fly) as context, then instructs Claude to:
1. Generate a full-day meal plan (5 meals)
2. Include approximate calories and macros per meal
3. Avoid allergens and respect dietary preferences
4. Append 3 personalized tips aligned to the user's goal

## Screenshots
_(Add screenshots of the profile form, profile listing, and a generated diet plan here)_
