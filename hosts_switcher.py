import os
from flask import Flask, request, render_template
import subprocess

app = Flask(__name__)

# Paths for hosts files
BLOCKED_HOSTS = "/etc/hosts-manager/block_hosts"
ALLOWED_HOSTS = "/etc/hosts-manager/allow_hosts"
HOSTS_FILE = "/etc/hosts"

@app.route("/", methods=["GET", "POST"])
def manage_hosts():
    message = ""
    if request.method == "POST":
        action = request.form.get("action")
        if action == "block":
            message = update_hosts(BLOCKED_HOSTS)
        elif action == "unblock":
            message = update_hosts(ALLOWED_HOSTS)
    return render_template("index.html", message=message)

def update_hosts(source_file):
    try:
        subprocess.run(
            ["sudo", "cp", source_file, HOSTS_FILE],
            check=True
        )
        return "Operation successful."
    except subprocess.CalledProcessError:
        return "Error: Could not update hosts file. Ensure sudo permissions are provided."

@app.route("/control", methods=["POST"])
def control_service():
    action = request.form.get("action")
    if action == "stop":
        os.system("sudo systemctl stop hosts_manager.service")
        return "Service stopped. Reload the page to restart."
    elif action == "restart":
        os.system("sudo systemctl restart hosts_manager.service")
        return "Service restarted successfully."
    return "Invalid action."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

