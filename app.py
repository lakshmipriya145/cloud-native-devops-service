from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "🚀 Cloud Native DevOps Project LIVE"

@app.route('/health')
def health():
    return {"status": "running"}

@app.route('/about')
def about():
    return "Deployed using Docker + Cloud"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
