st.sidebar.title("⚙️ Scan Options")

# Option 1: Enter folder path
folder = st.sidebar.text_input("📂 Enter folder path to scan:", "sample_app")

# Option 2: Upload a file
uploaded_file = st.sidebar.file_uploader("📂 Or upload a file", type=["py"])

if st.sidebar.button("▶️ Run Scan"):
    if uploaded_file:
        # Save uploaded file temporarily
        with open("uploaded_temp.py", "wb") as f:
            f.write(uploaded_file.getbuffer())
        target = "uploaded_temp.py"
    else:
        target = folder

    if os.path.exists(target):
        with st.spinner("🔎 Scanning in progress..."):
            result = subprocess.run(
                ["semgrep", "--config", "rules.yaml", target],
                capture_output=True, text=True
            )
        st.success("✅ Scan Completed")
        st.code(result.stdout, language="bash")
    else:
        st.error("❌ Path not found. Please upload a file or enter valid folder.")
