from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Welcome to Bazel Flask API!", "status": "running"})

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/info")
def info():
    return jsonify({
        "app": "Bazel Flask API",
        "version": "1.0.0",
        "build_system": "Bazel"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
