
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/student")
def get_student():
    return jsonify({
        "student_id": "YOUR-STUDENT-ID",
        "name": "YOUR FULL NAME",
        "program": "BSIT",
        "year": 3,
        "section": "YOUR SECTION"
    })


@app.route("/hello")
def say_hello():
    name = request.args.get("name", "Student")
    return jsonify({
        "message": f"Hello, {name}!"
    })


# Example custom endpoint for the additional task
@app.route("/jero")
def custom_api():
    name = request.args.get("name", "Student")
    return jsonify({
        "message": f"Hello, {name}! Welcome to my custom API.",
        "endpoint": "/jero",
        "activity": "Laboratory Activity 4"
    })


if __name__ == "__main__":
    app.run(debug=True)
