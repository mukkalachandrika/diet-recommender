from groq import Groq
import os

client = Groq(api_key=os.environ["GROQ_API_KEY"])

def build_prompt(profile: dict, user_question: str) -> str:
    bmi = profile["weight_kg"] / ((profile["height_cm"] / 100) ** 2)
    allergies = profile["allergies"] if profile["allergies"] else "None"
    preferences = profile["preferences"] if profile["preferences"] else "None"

    return f"""You are a certified nutritionist and diet planning expert.

Here is the user's health profile:
- Name: {profile["name"]}
- Age: {profile["age"]} years
- Gender: {profile["gender"]}
- Weight: {profile["weight_kg"]} kg
- Height: {profile["height_cm"]} cm
- BMI: {bmi:.1f}
- Activity level: {profile["activity"]}
- Health goal: {profile["goal"]}
- Food allergies / intolerances: {allergies}
- Dietary preferences: {preferences}

The user asks: "{user_question}"

Respond with a detailed, personalized diet plan that:
1. Fits their goal ({profile["goal"]}) and activity level
2. Lists a full day's meal plan (breakfast, mid-morning snack, lunch, evening snack, dinner)
3. Gives approximate calories and macros for each meal
4. Avoids all listed allergens and respects dietary preferences
5. Ends with 3 practical tips specific to their goal

Format the response with clear headings and be warm and encouraging."""


def generate_diet_plan(profile: dict, user_question: str) -> str:
    prompt = build_prompt(profile, user_question)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        max_tokens=1500,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content