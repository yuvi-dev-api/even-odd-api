from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return "Even-Odd API is running 🚀"

# Even-Odd check route
@app.route("/check", methods=["GET"])
def check():
    num = request.args.get("number")

    if num is None:
        return jsonify({"error": "Please provide a number like /check?number=5"}), 400

    try:
        num = int(num)
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400

    if num % 2 == 0:
        result = "Even"
    else:
        result = "Odd"

    return jsonify({
        "number": num,
        "type": result
    })


# IMPORTANT for Render
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))