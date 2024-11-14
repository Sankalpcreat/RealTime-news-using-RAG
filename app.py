from flask import Flask, request, jsonify
from src.rag_pipeline import rag_pipeline
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

@app.route('/summarize', methods=['POST'])
def summarize():
    if not request.is_json:
        return jsonify({"error": "Invalid input: Expected JSON data."}), 400

    data = request.get_json()
    topic = data.get("topic")
    if not topic:
        return jsonify({"error": "Missing 'topic' in request data."}), 400

    try:
        summaries = rag_pipeline(topic)
        return jsonify({"summaries": summaries})
    except Exception as e:
        return jsonify({"error": "An internal error occurred."}), 500

if __name__ == '__main__':
    app.run(debug=False)  # Set debug to False for production
