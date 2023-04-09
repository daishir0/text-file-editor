from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    keyword = request.form.get("keyword")
    results = []
    with open(os.path.join("..", "script.txt"), "r", encoding='utf-8') as f:
        for idx, line in enumerate(f.readlines()):
            if keyword in line:
                results.append({"line_number": idx, "text": line.strip()})
    return jsonify(results)

@app.route("/edit", methods=["POST"])
def edit():
    line_number = int(request.form.get("line_number"))
    edited_text = request.form.get("edited_text")

    with open(os.path.join("..", "script.txt"), "r", encoding='utf-8') as f:
        lines = f.readlines()

    lines[line_number] = f"{edited_text}\n"

    with open(os.path.join("..", "script.txt"), "w", encoding='utf-8') as f:
        f.writelines(lines)

    return "OK"

if __name__ == "__main__":
    app.run(debug=True)
