from flask import Flask, request, render_template
from textblob import TextBlob

app = Flask(__name__)

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"
2
def chatbot_response(user_input):
    sentiment = analyze_sentiment(user_input)
    if "hello" in user_input.lower():
        reply = "Hello! How can I help you today?"
    elif "help" in user_input.lower():
        reply = "Sure! I'm here to help. What do you need assistance with?"
    else:
        reply = "Thanks for sharing that."
    return f"{reply} (Sentiment: {sentiment})"

@app.route("/", methods=["GET", "POST"])
def home():
    response = ""
    if request.method == "POST":
        user_input = request.form["message"]
        response = chatbot_response(user_input)
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)