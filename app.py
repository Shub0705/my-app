from flask import Flask, jsonify
import datetime
import socket

app = Flask(__name__)

BUILD_TIME = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
HOSTNAME = socket.gethostname()

@app.route("/")
def home():
    return f"""
    🚀 Deployed successfully via Jenkins Webhook!<br><br>
    🔁 CI Trigger: GitHub Webhook<br>
    🕒 Build Time: {BUILD_TIME}<br>
    🖥 Server: {HOSTNAME}<br>
    ✅ Status: Running new version
    """

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "build_time": BUILD_TIME,
        "server": HOSTNAME
    }), 200

@app.route("/version")
def version():
    return {
        "app": "flask-webhook-demo",
        "version": "v2.0",
        "deployed_via": "jenkins-webhook"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

