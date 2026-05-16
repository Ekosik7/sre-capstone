from flask import Flask
import prometheus_client

app = Flask(__name__)

REQUEST_COUNT = prometheus_client.Counter(
    'app_requests_total', 'Total requests'
)

@app.route('/')
def hello():
    REQUEST_COUNT.inc()
    return {"status": "ok", "message": "Hello from SRE app!"}

@app.route('/health')
def health():
    return {"status": "healthy"}

@app.route('/metrics')
def metrics():
    return prometheus_client.generate_latest()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
