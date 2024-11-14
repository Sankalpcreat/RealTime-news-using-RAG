# app.py
from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
from src.rag_pipeline import rag_pipeline
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Initialize Flask-RESTx API with Swagger UI
api = Api(app, title="Real-Time News Summarizer API", description="API for summarizing real-time news using RAG pipeline")

# Define the API namespace
ns = api.namespace('summarizer', description='Summarize news topics')

# Define the expected input payload using Flask-RESTx's fields
summarize_model = api.model('Summarize', {
    'topic': fields.String(required=True, description='Topic for news summarization')
})

@ns.route('/summarize')
class SummarizeResource(Resource):
    @api.expect(summarize_model)
    def post(self):
        """Summarize news based on the provided topic."""
        if not request.is_json:
            return {"error": "Invalid input: Expected JSON data."}, 400

        data = request.get_json()
        topic = data.get("topic")
        if not topic:
            return {"error": "Missing 'topic' in request data."}, 400

        try:
            summaries = rag_pipeline(topic)
            return {"summaries": summaries}
        except Exception as e:
            return {"error": "An internal error occurred."}, 500

if __name__ == '__main__':
    app.run(debug=False)
