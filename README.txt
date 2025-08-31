🔎 Secure Coding Analysis with Semgrep

This project demonstrates CT-CS-01 Secure Coding Analysis Tool using Semgrep to detect insecure coding practices in Python applications.

It includes:

Command-line scanning with Semgrep

Streamlit-based UI for user-friendly scanning

🚀 Features

Detects vulnerabilities such as:

Command Injection (subprocess with shell=True)

Arbitrary Code Execution (eval)

Unsafe Deserialization (yaml.load)

Supports scanning of folders or single uploaded files

Browser-based UI built with Streamlit

🛠 Installation

Make sure you have Python 3 and pip installed.

Install Dependencies
# Update package list (Ubuntu/WSL)
sudo apt update

# Install pip
sudo apt install python3-pip

# Install Semgrep
python3 -m pip install --upgrade semgrep

# Install Streamlit
pip3 install streamlit


Verify installation:

semgrep --version
streamlit --version

📂 Project Structure
semgrep_demo_pack/
│── sample_app/          # Demo vulnerable Python app
│   └── app.py           # Contains insecure code
│── rules.yaml           # Semgrep rules for scanning
│── streamlit_ui.py      # Streamlit-based UI scanner

⚡ Usage
1. Command-Line Scan

Navigate to the project folder:

cd semgrep_demo_pack


Run Semgrep scan:

semgrep --config rules.yaml sample_app


Results will be displayed in the terminal.

2. Streamlit UI

Launch the Streamlit application:

streamlit run streamlit_ui.py


Open in your browser → http://localhost:8501

UI Options:

📂 Enter folder path → e.g., sample_app

📄 Upload a .py file → scans only the uploaded file

Click ▶️ Run Scan → view scan results in the browser

🎯 How It Was Created

Installed Semgrep in WSL (Ubuntu).

Created a sample vulnerable Python app (app.py) with insecure coding patterns.

Wrote a custom rules.yaml file for detecting vulnerabilities.

Ran scans via command line to identify issues.

Fixed one issue (removed shell=True) and re-scanned to confirm.

Built a Streamlit UI (streamlit_ui.py) to simplify scanning for non-CLI users.

📜 License

MIT License © 2025

This way, anyone who reads the README understands:

What the project is

How to install dependencies

How to run CLI and UI scans

How the project was built
