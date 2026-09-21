from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    query = ""

    if request.method == "POST":
        query = request.form.get("query", "")

    return render_template("index.html", query=query)

if __name__ == "__main__":
    app.run(debug=True)
