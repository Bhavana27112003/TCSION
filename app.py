from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)

with open("sentiment_model.pkl", "rb") as f:
    model = pickle.load(f)

emoji_map = {
    "positive": "😊 Positive",
    "neutral": "😐 Neutral",
    "negative": "😡 Negative"
}

positive_words = {"good", "great", "excellent", "amazing", "nice", "love", "fantastic", "awesome", "perfect", "satisfied"}
negative_words = {"bad", "terrible", "poor", "awful", "hate", "worst", "useless", "disappointing", "frustrating"}
neutral_words = {"okay", "average", "fine", "decent", "normal", "acceptable", "moderate"}

def simple_rule_predict(text):
    words = set(text.lower().split())

    if words & positive_words:
        return "positive"
    if words & negative_words:
        return "negative"
    if words & neutral_words:
        return "neutral"
    return None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    review = request.form.get("review", "").strip().lower()

    if not review:
        return jsonify({"sentiment": "Please enter a review."})

    # Rule-based fallback for very short reviews
    if len(review.split()) <= 3:
        rule_result = simple_rule_predict(review)
        if rule_result:
            return jsonify({"sentiment": emoji_map[rule_result]})

    prediction = model.predict([review])[0]
    return jsonify({"sentiment": emoji_map.get(prediction, prediction)})

if __name__ == "__main__":
    app.run(debug=True)