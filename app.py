import os
from transformers import pipeline
from flask import Flask, request, jsonify

app = Flask(__name__)
generator = pipeline("text-generation", model="distilgpt2")
@app.route("/generate", methods=["POST"])
def generate():
    prompt = request.json.get("prompt", "")
    result = generator(prompt, max_new_tokens=50, num_return_sequences=1, truncation=True)
    return jsonify(result[0])

# ADD THIS NEW ENDPOINT
@app.route("/health", methods=["GET"])
def health_check():
    # Health check endpoint for automated testing
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)