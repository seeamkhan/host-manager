#!/bin/bash

echo "Starting setup for Hosts Manager..."

# Ensure script is run as sudo
if [ "$EUID" -ne 0 ]; then
  echo "Please run as root (e.g., sudo ./setup.sh)"
  exit
fi

# Install Python dependencies
echo "Creating virtual environment and installing dependencies..."
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Create hosts backup folder
echo "Setting up hosts backup folder..."
mkdir -p /etc/hosts-manager
cp etc_hosts/block_hosts /etc/hosts-manager/block_hosts
cp etc_hosts/allow_hosts /etc/hosts-manager/allow_hosts

# Add systemd service for Linux
if [ "$(uname)" == "Linux" ]; then
  echo "Setting up systemd service..."
  cat <<EOF >/etc/systemd/system/hosts_manager.service
[Unit]
Description=Hosts Manager Flask App
After=network.target

[Service]
User=$USER
WorkingDirectory=$(pwd)
ExecStart=$(pwd)/venv/bin/python $(pwd)/hosts_switcher.py
Restart=always

[Install]
WantedBy=multi-user.target
EOF
  systemctl enable hosts_manager.service
  systemctl start hosts_manager.service
fi

echo "Setup complete. Visit http://localhost:8080 to use the tool."
