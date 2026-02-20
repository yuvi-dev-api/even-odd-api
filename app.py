from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        num = request.form.get("number")

        try:
            num = int(num)
            if num % 2 == 0:
                result = f"{num} is Even ✅"
            else:
                result = f"{num} is Odd 🔥"
        except:
            result = "Please enter a valid number ❌"

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))