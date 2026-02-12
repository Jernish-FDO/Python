from flask import Flask, jsonify

app = Flask(__name__)

# Your very first Web API, buddy!
@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to your Python API!",
        "status": "Online",
        "buddy": "Jernish"
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    print("🚀 API starting at http://127.0.0.1:5000")
    app.run(debug=True)
