from flask import Flask, request, jsonify
from sentiment_model import analyze_sentiment
import psycopg2
from psycopg2 import sql

app = Flask(__name__)

# Database connection setup
def get_db_connection():
    conn = psycopg2.connect(
        host="db",  # Use 'db' if using Docker, 'localhost' if local
        database="api_db",
        port="5432",
	user="my_api",
        password="my_api_pass"
    )
    return conn

# Function to log the API calls
def log_api_call(text, sentiment):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        sql.SQL("INSERT INTO api_logs (text, sentiment) VALUES (%s, %s)"),
        [text, sentiment]
    )
    conn.commit()
    cursor.close()
    conn.close()

@app.route('/sentiment', methods=['POST'])
def sentiment():
    data = request.get_json()
    text = data['text']
    sentiment_result = analyze_sentiment(text)
    
    # Log the API call to PostgreSQL
    log_api_call(text, sentiment_result)

    return jsonify(sentiment_result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
