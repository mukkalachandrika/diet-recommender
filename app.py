from flask import Flask, render_template, request, redirect, url_for, flash, session
from database import init_db, save_profile, get_profile, get_all_profiles, delete_profile
from llm import generate_diet_plan
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

init_db()


@app.route("/")
def index():
    profiles = get_all_profiles()
    return render_template("index.html", profiles=profiles)


@app.route("/profile/new", methods=["GET", "POST"])
def new_profile():
    if request.method == "POST":
        data = {
            "name":        request.form["name"].strip(),
            "age":         int(request.form["age"]),
            "gender":      request.form["gender"],
            "weight_kg":   float(request.form["weight_kg"]),
            "height_cm":   float(request.form["height_cm"]),
            "activity":    request.form["activity"],
            "goal":        request.form["goal"],
            "allergies":   request.form.get("allergies", "").strip(),
            "preferences": request.form.get("preferences", "").strip(),
        }
        user_id = save_profile(data)
        flash("Profile saved successfully!", "success")
        return redirect(url_for("diet_page", user_id=user_id))
    return render_template("profile.html")


@app.route("/profile/<int:user_id>/delete", methods=["POST"])
def delete(user_id):
    delete_profile(user_id)
    flash("Profile deleted.", "info")
    return redirect(url_for("index"))


@app.route("/diet/<int:user_id>", methods=["GET", "POST"])
def diet_page(user_id):
    profile = get_profile(user_id)
    if not profile:
        flash("Profile not found.", "error")
        return redirect(url_for("index"))

    diet_plan = None
    question = ""

    if request.method == "POST":
        question = request.form.get("question", "Give me a personalized diet plan for today.")
        diet_plan = generate_diet_plan(profile, question)

    return render_template("diet.html", profile=profile, diet_plan=diet_plan, question=question)


if __name__ == "__main__":
    app.run(debug=True)
