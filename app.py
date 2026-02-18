from flask import Flask, request, redirect, session
import sqlite3
import pickle
import os
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)
app.secret_key = "smartcampus_secret"

# ===============================
# 1️⃣ TRAIN MODEL IF NOT EXISTS
# ===============================
if not os.path.exists("risk_model.pkl"):
    data = {
        "attendance": [90, 85, 40, 30, 75, 50, 95, 20],
        "marks": [85, 70, 30, 20, 60, 40, 88, 15],
        "assignments": [90, 80, 35, 25, 70, 45, 92, 10],
        "risk": [0, 0, 1, 1, 0, 1, 0, 1]
    }

    df = pd.DataFrame(data)
    X = df[["attendance", "marks", "assignments"]]
    y = df["risk"]

    model = RandomForestClassifier()
    model.fit(X, y)

    pickle.dump(model, open("risk_model.pkl", "wb"))

model = pickle.load(open("risk_model.pkl", "rb"))

# ===============================
# 2️⃣ DATABASE SETUP
# ===============================
conn = sqlite3.connect("database.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
""")

c.execute("SELECT * FROM users WHERE username='admin'")
if not c.fetchone():
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("admin", "1234"))

conn.commit()
conn.close()

# ===============================
# 3️⃣ LOGIN PAGE
# ===============================
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = c.fetchone()
        conn.close()

        if user:
            session["user"] = username
            return redirect("/dashboard")
        else:
            return "<h3 style='color:red;text-align:center;'>Invalid Credentials ❌</h3><div style='text-align:center;'><a href='/'>Go Back</a></div>"

    return """
    <html>
    <head>
    <title>SmartCampus AI</title>
    <style>
        body {
            margin: 0;
            font-family: Arial;
            background: linear-gradient(135deg, #667eea, #764ba2);
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .card {
            background: white;
            padding: 40px;
            border-radius: 15px;
            width: 350px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            text-align: center;
        }
        input {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border-radius: 8px;
            border: 1px solid #ccc;
        }
        button {
            width: 100%;
            padding: 10px;
            background: #667eea;
            border: none;
            color: white;
            border-radius: 8px;
            cursor: pointer;
            font-weight: bold;
        }
        button:hover {
            background: #5a67d8;
        }
        h2 {
            margin-bottom: 20px;
        }
    </style>
    </head>
    <body>
        <div class="card">
            <h2>SmartCampus AI</h2>
            <form method="POST">
                <input name="username" placeholder="Username" required>
                <input name="password" type="password" placeholder="Password" required>
                <button type="submit">Login</button>
            </form>
        </div>
    </body>
    </html>
    """

# ===============================
# 4️⃣ DASHBOARD
# ===============================
@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "user" not in session:
        return redirect("/")

    prediction = ""
    color = ""

    if request.method == "POST":
        attendance = float(request.form["attendance"])
        marks = float(request.form["marks"])
        assignments = float(request.form["assignments"])

        data = np.array([[attendance, marks, assignments]])
        result = model.predict(data)

        if result[0] == 1:
            prediction = "High Risk of Failure 🚨"
            color = "red"
        else:
            prediction = "Low Risk ✅"
            color = "green"

    return f"""
    <html>
    <head>
    <title>Dashboard</title>
    <style>
        body {{
            margin: 0;
            font-family: Arial;
            background: #f4f6f9;
        }}
        .navbar {{
            background: #667eea;
            color: white;
            padding: 15px;
            display: flex;
            justify-content: space-between;
        }}
        .container {{
            padding: 40px;
            display: flex;
            justify-content: center;
        }}
        .card {{
            background: white;
            padding: 30px;
            border-radius: 15px;
            width: 400px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }}
        input {{
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border-radius: 8px;
            border: 1px solid #ccc;
        }}
        button {{
            width: 100%;
            padding: 10px;
            background: #667eea;
            border: none;
            color: white;
            border-radius: 8px;
            cursor: pointer;
            font-weight: bold;
        }}
        button:hover {{
            background: #5a67d8;
        }}
        .result {{
            margin-top: 20px;
            font-weight: bold;
            color: {color};
            text-align: center;
        }}
        a {{
            color: white;
            text-decoration: none;
        }}
    </style>
    </head>
    <body>
        <div class="navbar">
            <div>SmartCampus AI Dashboard</div>
            <div>Welcome {session['user']} | <a href="/logout">Logout</a></div>
        </div>

        <div class="container">
            <div class="card">
                <h3>Student Risk Prediction</h3>
                <form method="POST">
                    <input name="attendance" placeholder="Attendance %" required>
                    <input name="marks" placeholder="Internal Marks" required>
                    <input name="assignments" placeholder="Assignments %" required>
                    <button type="submit">Predict Risk</button>
                </form>

                <div class="result">{prediction}</div>
            </div>
        </div>
    </body>
    </html>
    """

# ===============================
# LOGOUT
# ===============================
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
