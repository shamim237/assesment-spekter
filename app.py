from flask import Flask, request, jsonify
from sentiment_model import analyze_sentiment_text

app = Flask(__name__)



@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    # Retrieve the JSON payload from the request
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'Invalid request. The payload must contain "text" field.'}), 400

    text = data['text']

    # Perform sentiment analysis using the provided code
    sentiment = analyze_sentiment_text(text)

    # Return the sentiment analysis result as JSON response
    return jsonify({'sentiment': sentiment}), 200

if __name__ == '__main__':
    app.run(debug=True)
