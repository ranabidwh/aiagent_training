# aiagent_training

# Python Installation and Setup Guide
This guide will walk you through the process of installing Python on your operating system and setting up a basic development environment.

## 1. Installing Python
It's recommended to install Python from the official website or through a package manager for the most stable and up-to-date versions.

### Option A: Using the Official Python Installer (Recommended for Windows & macOS)
1.  **Download Python:**
    * Go to the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
    * Click on the "Download Python X.Y.Z" button (where X.Y.Z is the latest stable version, e.g., 3.12.0). This will typically download the appropriate installer for your operating system.

2.  **Run the Installer:**
    * **For Windows:**
        * Locate the downloaded `.exe` file and double-click it.
        * **IMPORTANT:** On the first installer screen, **check the box that says "Add Python X.Y to PATH"** (this is crucial for easily running Python from the command line).
        * Click "Install Now" and follow the on-screen prompts.
        * Once the installation is complete, you might see a screen about disabling the path length limit (especially on newer Windows versions). It's generally safe to click "Disable path length limit" if prompted.

    * **For macOS:**
        * Locate the downloaded `.pkg` file and double-click it.
        * Follow the on-screen instructions. The installer will guide you through the process. Python is typically installed in `/usr/local/bin/python3`.

3.  **Verify Installation:**
    * Open your terminal or command prompt.
    * Type the following command and press Enter:
        ```bash
        python3 --version
        ```
    * You should see output similar to `Python 3.X.Y`. If you see an error, double-check your installation steps, especially the "Add to PATH" step on Windows.

### Option B: Using a Package Manager (Recommended for Linux & Advanced Users)
* **For Linux (Debian/Ubuntu-based):**
    ```bash
    sudo apt update
    sudo apt install python3 python3-pip
    ```
    * Verify installation: `python3 --version` and `pip3 --version`

* **For Linux (Fedora/RHEL-based):**
    ```bash
    sudo dnf install python3 python3-pip
    ```
    * Verify installation: `python3 --version` and `pip3 --version`

* **For macOS (using Homebrew):**
    * If you don't have Homebrew, install it first:
        ```bash
        /bin/bash -c "$(curl -fsSL [https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh](https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh))"
        ```
    * Then install Python:
        ```bash
        brew install python
        ```
    * Verify installation: `python3 --version` and `pip3 --version`

---

## 2. Setting up a Virtual Environment (Highly Recommended!)
A virtual environment creates an isolated space for your Python projects, allowing you to manage dependencies for each project separately. This prevents conflicts between different project requirements.

1.  **Navigate to your Project Directory:**
    Open your terminal or command prompt and `cd` into the directory where you plan to store your Python code.
    ```bash
    cd path/to/your/project
    ```
    (Replace `path/to/your/project` with the actual path, e.g., `cd Documents/my_python_project`)

2.  **Create a Virtual Environment:**
    Use the `venv` module (built-in with Python 3.3+):
    ```bash
    python3 -m venv venv
    ```
    This command creates a directory named `venv` (you can choose a different name, but `venv` is common) inside your project directory.

3.  **Activate the Virtual Environment:**
    * **For Windows (Command Prompt/PowerShell):**
        ```bash
        .\venv\Scripts\activate
        ```
        (Note: If using PowerShell, you might need to enable script execution: `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` first, then try the activate command again. After activating, you can revert the policy if you wish.)

    * **For macOS/Linux (Bash/Zsh):**
        ```bash
        source venv/bin/activate
        ```

    * **How to tell it's active:** Your terminal prompt will change to show `(venv)` at the beginning, indicating that you are now working within the virtual environment.

4.  **Install Project Dependencies:**
    Once your virtual environment is active, you can install any necessary Python packages using `pip`. For example, if your project needs a package called `requests`:
    ```bash
    pip install requests
    ```
    These packages will be installed only within your `venv` environment, not globally on your system.

5.  **Deactivate the Virtual Environment:**
    When you are done working on your project, you can deactivate the virtual environment:
    ```bash
    deactivate
    ```
    Your terminal prompt will return to its normal state.

---
## 3. Running Your Python Code
Now that Python is installed and your environment is set up, you can run your Python scripts.

1.  **Activate your virtual environment** (if you're using one, which is recommended).

2.  **Navigate to the directory** where your Python script (`.py` file) is located.

3.  **Run your script:**
    ```bash
    python your_script_name.py
    ```
    (Replace `your_script_name.py` with the actual name of your Python file, e.g., `python hello_world.py`)
---

## Troubleshooting
* **"Python not found" or "command not found":** This usually means Python wasn't added to your system's PATH. On Windows, rerun the installer and ensure "Add Python X.Y to PATH" is checked. On macOS/Linux, ensure your installation was successful or your shell's PATH is correctly configured.
* **Permissions errors:** On Linux/macOS, if you're having trouble installing packages or creating environments, you might be trying to install globally without `sudo`. Always use `pip install` *after* activating your virtual environment.
* **Conflicting Python versions:** If you have multiple Python versions installed, explicitly use `python3` instead of `python` to ensure you're using the correct version. Within an activated virtual environment, `python` will point to the correct version for that environment.
---
