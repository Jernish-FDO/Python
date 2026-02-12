# Python Setup for All Devices

This guide provides instructions for installing Python on any device, from high-end PCs to smartphones.

---

## 💻 Desktop & Laptop

### Windows
1.  **Download**: Visit [python.org](https://www.python.org/downloads/windows/).
2.  **Install**: Run the installer.
3.  **⚠️ CRITICAL**: Check the box **"Add Python to PATH"** at the start.
4.  **Verify**: Open PowerShell/CMD and type `python --version`.

### macOS
1.  **Official**: Download from [python.org](https://www.python.org/downloads/macos/).
2.  **Homebrew (Recommended)**:
    - Install Homebrew: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
    - Install Python: `brew install python`
3.  **Verify**: Open Terminal and type `python3 --version`.

### Linux (Ubuntu/Debian)
1.  **Update**: `sudo apt update`
2.  **Install**: `sudo apt install python3 python3-pip`
3.  **Verify**: Type `python3 --version`.

---

## 📱 Mobile Devices

### Android (Advanced/Terminal)
1.  **Install Termux**: Get it from [F-Droid](https://f-droid.org/en/packages/com.termux/) (Avoid Play Store version as it is outdated).
2.  **Setup**: Open Termux and type:
    ```bash
    pkg update && pkg upgrade
    pkg install python
    ```
3.  **Verify**: `python --version`

### Android (Beginner/IDE)
1.  **Install Pydroid 3**: Available on the [Google Play Store](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3).
2.  It provides a ready-to-use editor and interpreter.

### iOS (iPhone/iPad)
1.  **Pythonista 3**: A powerful, paid IDE with deep iOS integration.
2.  **Pyto**: A great alternative with support for many libraries.
3.  **iSH Shell**:
    - Install "iSH Shell" from App Store.
    - Type `apk add python3` inside the app.

---

## 🌐 Online (No Installation)
If you can't install anything, use these in your browser:
- [Google Colab](https://colab.research.google.com/) (Great for Data Science)
- [Replit](https://replit.com/) (Great for collaborative coding)
- [Python.org Shell](https://www.python.org/shell/) (Basic testing)
