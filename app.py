from flask import Flask, render_template, request
import mackolik_analyzer

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    error = None
    if request.method == "POST":
        link = request.form.get("mackolik_link")
        if link:
            try:
                prediction = mackolik_analyzer.analyze_match(link)
            except Exception as e:
                error = str(e)
    return render_template("index.html", prediction=prediction, error=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
