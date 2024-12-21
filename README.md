# Hosts Manager

A simple tool to block and unblock websites (e.g., YouTube) using `/etc/hosts`. Designed for Ubuntu and macOS. 

## Features
- Browser-based interface for blocking/unblocking websites.
- Automatically blocks websites at system startup.
- Easy setup and cross-platform compatibility.

## Prerequisites
- Python 3 installed.
- Admin (sudo) privileges on your system.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/host-manager.git
   cd host-manager
   ```
2. Run the setup script `./setup.sh`
3. Access the interface in your browser: `http://localhost:8080`

## Usage
- Open the URL and use the buttons to block or unblock websites.
- Provide your sudo password when prompted.

## Debug
- To Start/Stop the service on the system from terminal:
```
systemctl enable hosts_manager.service
systemctl start hosts_manager.service

systemctl stop hosts_manager.service
```
