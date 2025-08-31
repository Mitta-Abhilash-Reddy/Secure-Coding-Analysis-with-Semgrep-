import streamlit as st
import subprocess
import os

st.set_page_config(page_title="Semgrep Scanner", page_icon="🔎")

st.title("🔎 Secure Coding Analysis with Semgrep")
st.write("This tool scans source code for vulnerabilities using Semgrep rules.")

# Input field for folder
folder = st.text_input("📂 Enter folder path to scan:", "sample_app")

# Option to upload a file
uploaded_file = st.file_uploader("📄 Or upload a Python file to scan:", type=["py"])

# Run Scan button
if st.button("▶️ Run Scan"):
    # Determine target: uploaded file or folder
    if uploaded_file:
        temp_file_path = "uploaded_temp.py"
        with open(temp_file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        target = temp_file_path
    else:
        target = folder

    # Check if the target exists
    if os.path.exists(target):
        with st.spinner("🔎 Scanning... please wait"):
            try:
                result = subprocess.run(
                    ["semgrep", "--config", "rules.yaml", target],
                    capture_output=True, text=True, check=True
                )
                st.success("✅ Scan Completed")
                st.subheader("Scan Results")
                if result.stdout.strip():
                    st.code(result.stdout, language="bash")
                else:
                    st.info("No issues found by Semgrep!")
            except subprocess.CalledProcessError as e:
                st.error("❌ Scan failed!")
                st.code(e.stderr, language="bash")
    else:
        st.error("❌ Target not found. Please upload a file or enter a valid folder.")

    # Cleanup temporary uploaded file
    if uploaded_file and os.path.exists(temp_file_path):
        os.remove(temp_file_path)
