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

## 🔧 AWS Builder ID Setup

### Step 1: Create AWS Builder ID
1. Visit: https://us-east-1.credentials.signin.aws/#/security
2. Click "Create AWS Builder ID"
3. Enter your email address
4. Verify email and set password
5. Complete profile setup

<img width="1865" height="695" alt="image" src="https://github.com/user-attachments/assets/cac10004-d031-4cd8-b469-bf4afaf6cb97" />


### Step 2: Authentication Flow
```bash
# Start authentication
q login

# Follow the browser link that opens
# Sign in with your AWS Builder ID
# Grant permissions to Amazon Q CLI
```

### Step 3: Create Builder Directory Structure
```bash
# Create project workspace
mkdir -p ~/builder-workspace
cd ~/builder-workspace

# Initialize project structure
mkdir -p {src,docs,tests,config}
echo "# Builder Workspace" > README.md

# Set as default workspace
export Q_WORKSPACE=~/builder-workspace
echo 'export Q_WORKSPACE=~/builder-workspace' >> ~/.bashrc
```

## 🛠️ Verification Commands
```bash
# Check installation
q --version

# Test authentication
q login

# Verify workspace
echo $Q_WORKSPACE

# Start interactive session
q chat
```

---
[← Previous: Introduction](../01-introduction/README.md) | [Back to Main](../README.md) | [Next: Demo →](../03-hands-on-demo/README.md)
