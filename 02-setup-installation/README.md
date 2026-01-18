# 02 - Setup & Installation

## 🎯 Learning Objectives
- Install Amazon Q Developer CLI (Kiro CLI)
- Configure AWS Builder ID authentication
- Verify installation and connectivity

## 📚 Amazon Q Developer CLI (Kiro CLI) Installation

### **Windows Installation (via WSL)**
As of 2026, Amazon Q CLI requires Windows Subsystem for Linux (WSL) for installation.

#### Step 1: Install WSL
Open PowerShell as Administrator and run:
```powershell
wsl --install
```

Restart your computer and set up your Linux (Ubuntu) username/password.

#### Step 2: Download and Install Amazon Q CLI
Open your WSL terminal and run:
```bash
# Install unzip if needed
sudo apt install unzip

# Download Amazon Q CLI
curl --proto '=https' --tlsv1.2 -sSf "https://desktop-release.q.us-east-1.amazonaws.com/latest/q-x86_64-linux.zip" -o "q.zip"

# Extract and install
unzip q.zip
cd q && ./install.sh
```

#### Step 3: Authenticate
In the WSL terminal, run:
```bash
q login
```
Follow the link to authorize with your AWS Builder ID.

#### Step 4: Start Using Amazon Q
Begin a session by typing:
```bash
q chat
```

### **Linux/Mac Installation**
```bash
# Download and install directly
curl --proto '=https' --tlsv1.2 -sSf "https://desktop-release.q.us-east-1.amazonaws.com/latest/q-x86_64-linux.zip" -o "q.zip"
unzip q.zip
cd q && ./install.sh

# Authenticate
q login

# Start session
q chat
```

## 🛠️ Verification Commands
```bash
# Check installation
q --version

# Test authentication
q login

# Start interactive session
q chat
```

---
[← Previous: Introduction](../01-introduction/README.md) | [Back to Main](../README.md) | [Next: Demo →](../03-hands-on-demo/README.md)
