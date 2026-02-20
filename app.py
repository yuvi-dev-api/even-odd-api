from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Even Odd API is Running 🚀"

@app.route("/check")
def check():
    num = request.args.get("number")

    if num is None:
        return jsonify({"error": "Please provide a number"}), 400

    try:
        num = int(num)
    except:
        return jsonify({"error": "Invalid number"}), 400

    if num % 2 == 0:
        return jsonify({"number": num, "type": "Even"})
    else:
        return jsonify({"number": num, "type": "Odd"})

if __name__ == "__main__":
    app.run()
