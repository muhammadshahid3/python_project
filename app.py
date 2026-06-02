from flask import Flask, jsonify
import random

app = Flask(__name__)

# Aapke sample quotes ki list
quotes = [
    "Khudi ko kar buland itna ke har taqdeer se pehle...",
    "Consistency is the key to success.",
    "Docker makes local and EC2 life super easy! 🚀",
    "CI/CD pipeline is running successfully!",
    "No more 'works on my machine' issues."
]

@app.route('/')
def home():
    # Randomly ek quote select hoga aur JSON response milega
    selected_quote = random.choice(quotes)
    return jsonify({
        "status": "success",
        "message": "Welcome to Dockerized Flask API on EC2!",
        "data": {
            "quote": selected_quote
        }
    })

if __name__ == '__main__':
    # Server ko 0.0.0.0 par chalana zaroori hai taake EC2 ke bahar access ho sake
    app.run(host='0.0.0.0', port=80)
