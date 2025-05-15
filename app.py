from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = ""
    if request.method == "POST":
        letter = request.form.get("letter", "").lower()
        if letter:
            if letter in "aeiou":
                prediction = "Today will be a fantastic day full of surprises!"
            else:
                prediction = "Expect a calm and peaceful day ahead."
        else:
            prediction = "Please enter a letter."
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
