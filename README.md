\# Project 2 — Personalized GenAI Diet Recommender



A Flask web app that captures user health details into a profile stored in SQLite, and generates a personalized AI diet plan when the user asks a question — using their saved profile as context for the LLM.



\---



\## Point 1 — Project Understanding



\### Problem Being Solved

People struggle to get personalized diet advice because generic plans don't account for individual health details like weight, height, age, allergies, and fitness goals. This app solves that by storing a personal health profile and using an LLM to generate a diet plan tailored specifically to that person.



\### User Actions Supported

\- Create a personal health profile (name, age, gender, weight, height, activity level, goal, allergies, dietary preferences)

\- View all saved profiles on the home page

\- Delete any profile

\- Ask questions to the AI assistant in natural language and get a personalized diet plan

\- Use quick-prompt chips for common queries like "full day plan" or "pre/post workout meals"



\### Data Involved

\- User profile data stored in SQLite database (diet.db)

\- Fields: name, age, gender, weight\_kg, height\_cm, activity level, goal, allergies, preferences, created\_at timestamp

\- BMI is calculated on the fly from weight and height before sending to the LLM



\### Constraints and Guardrails

\- The LLM is instructed to avoid all listed allergens

\- The LLM is instructed to respect dietary preferences (vegetarian, etc.)

\- The LLM is instructed to align meal plan strictly with the user's goal

\- Profile must have all required fields before saving (form validation)



\---



\## Point 2 — Tools and Technologies



\- Language: Python 3

\- Framework: Flask (web server and routing)

\- Database: SQLite via Python built-in sqlite3 module

\- LLM Provider: Groq API (free tier)

\- LLM Model: llama-3.3-70b-versatile

\- Frontend: HTML, CSS (no frameworks, plain templates)

\- Version Control: Git, GitHub

\- IDE: VS Code / Notepad



\---



\## Point 3 — Approach and Implementation



\### Step by Step How It Was Built



1\. Created the SQLite schema in database.py with a users table covering all health fields

2\. Built Flask routes in app.py — home page, new profile form, save profile, diet page, delete profile

3\. Built three HTML templates — index.html (profile list), profile.html (create form), diet.html (ask and view plan)

4\. Built the LLM integration in llm.py using the Groq API



\### LLM Prompt Design



The prompt was built to inject the full user profile as context before asking the LLM to generate the plan.



First iteration of prompt (too vague, output was generic):

"Generate a diet plan for a person who wants to lose weight."



Second iteration (added profile details, better but no structure):

"Generate a diet plan for {name}, age {age}, weight {weight}kg, goal: {goal}."



Final prompt (full profile + BMI + clear instructions + structured output):

\- Injects name, age, gender, weight, height, BMI (calculated), activity level, goal, allergies, preferences

\- Instructs the LLM to generate 5 meals: breakfast, mid-morning snack, lunch, evening snack, dinner

\- Asks for approximate calories and macros for each meal

\- Instructs to avoid all allergens and respect preferences

\- Asks for 3 personalized tips at the end aligned to the user's goal

\- Uses a warm and encouraging tone



\### Key Architecture Decisions

\- SQLite was chosen over MySQL for zero setup — no server needed, file-based

\- Groq API was chosen because it is completely free with no credit card required

\- BMI is calculated in Python before the prompt so the LLM receives it directly

\- Profile is fetched fresh from the database on every request so changes reflect immediately



\---



\## Point 4 — What Has Been Implemented



\### Working Features Delivered

\- Create health profile form with all fields and validation

\- Save profile to SQLite database

\- View all profiles on home page with name, age, goal badge

\- Delete any profile with confirmation

\- Ask any diet question in natural language

\- AI generates full personalized meal plan with calories and macros

\- Quick prompt chips for common queries

\- BMI calculation shown on the profile banner

\- Allergen and preference awareness in generated plans

\- Clean responsive UI with green health theme



\### What Was Not Implemented

\- Edit/update profile (only create and delete)

\- User login or authentication (single user mode)

\- Saving generated diet plans to database for history

\- Export diet plan as PDF



\---



\## Setup and Run



1\. Clone the repo

&#x20;  git clone https://github.com/mukkalachandrika/diet-recommender.git

&#x20;  cd diet-recommender



2\. Install dependencies

&#x20;  pip install flask groq



3\. Set your Groq API key — free at console.groq.com

&#x20;  Windows: set GROQ\_API\_KEY=your-key-here

&#x20;  Mac/Linux: export GROQ\_API\_KEY=your-key-here



4\. Run the app

&#x20;  python app.py



5\. Open browser at http://localhost:5000



\---



\## Project Structure



diet\_recommender/

├── app.py            — Flask routes

├── database.py       — SQLite schema and CRUD helpers

├── llm.py            — Prompt builder and Groq API call

├── requirements.txt

└── templates/

&#x20;   ├── index.html    — Profile listing home page

&#x20;   ├── profile.html  — Create profile form

&#x20;   └── diet.html     — Ask questions and view diet plan



\---



\## Screenshots



outputs have beed attached with the folder name screenshots



