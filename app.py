from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def dashboard():
    data = {
        "health_score": 26.7,
        "steps": 2350,
        "heart_rate": 72,
        "sleep": 7.5,
        "calories": 938,
        "confidence_sleep": 92,
        "confidence_hydration": 87,
        "confidence_exercise": 94
    }
    return render_template("dashboard.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
