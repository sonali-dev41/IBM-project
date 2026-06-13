from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load Model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    email_text = request.form["email"]

    vector = vectorizer.transform([email_text])

    prediction = model.predict(vector)[0]

    if prediction == 1:
        result = "⚠️ Phishing Email Detected"
    else:
        result = "✅ Safe Email"

    return render_template("index.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)
