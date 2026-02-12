# Python Setup Guide

## 1. Install Python
Download and install the latest version of Python from [python.org](https://www.python.org/downloads/).

## 2. Text Editor / IDE
Recommended: **Visual Studio Code (VS Code)**
- Install the "Python" extension by Microsoft.

## 3. Virtual Environments
It's best practice to use virtual environments to manage project-specific dependencies.

### Creating a Virtual Environment
```bash
# Windows
python -m venv venv

# macOS/Linux
python3 -m venv venv
```

### Activating the Environment
```bash
# Windows
.\venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

## 4. Verify Installation
Run the following in your terminal:
```bash
python --version
pip --version
```
