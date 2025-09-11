Simple AI Assistant - Quick guide (for non-technical users)

Files included:
- app.py             : The Streamlit app you run locally.
- requirements.txt   : Python packages to install.
- .env.example       : Example environment file (DO NOT upload personal keys).
- readme.txt         : This file.

Quick steps to create the ZIP (already done if you ran make_zip.py):
1. Unzip my-ai.zip (if you downloaded it).
2. Rename .env.example -> .env and open the file, replace the placeholder with your OpenAI API key:
    OPENAI_API_KEY=sk-xxxx
3. Install Python (if not installed) from https://www.python.org/downloads/
   - On Windows, during install check "Add Python to PATH".
4. Open Command Prompt (Windows) or Terminal (Mac/Linux).
   - Change directory to the project folder, e.g.:
     cd C:\Users\YourName\Downloads\my-ai
     or
     cd /Users/yourname/Downloads/my-ai
5. Run:
     pip install -r requirements.txt
     streamlit run app.py
6. A browser tab will open with the app. Upload PDF/TXT files (Index), then ask questions.

How to upload my-ai.zip to Google Drive and get a link:
1. Visit https://drive.google.com and sign in.
2. Click "New" -> "File upload" and select my-ai.zip.
3. After upload, right-click the file -> "Get link".
4. Change the access to "Anyone with the link" -> Viewer, then click "Copy link".
   (Only do this if you are OK sharing the ZIP. Do NOT upload your .env with the real API key.)

Troubleshooting:
- If 'pip' is not recognized, reinstall Python and ensure "Add to PATH" is checked.
- If a package install fails, try: pip install --upgrade pip
- If Streamlit does not open automatically, the command will show a URL you can copy into your browser.

Need help? Tell me which step you get stuck on and paste any error text.
