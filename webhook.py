from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/deploy/', methods=['POST'])
def deploy():
    # Run the deployment script when GitHub sends a webhook
    subprocess.run(["/bin/bash", "/var/www/html/deploy.sh"])
    return "Deployment Triggered", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
