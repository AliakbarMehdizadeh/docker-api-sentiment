from flask import Flask, request, jsonify
from sentiment_model import analyze_sentiment

app = Flask(__name__)

@app.route('/sentiment', methods=['POST'])
def sentiment():
    data = request.get_json()
    text = data['text']
    sentiment = analyze_sentiment(text)
    return jsonify(sentiment)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5001) 