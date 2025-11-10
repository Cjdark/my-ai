import streamlit as st
from openai import OpenAI
import requests
from bs4 import BeautifulSoup


# Initialize Groq client
client = OpenAI(
    api_key="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",  # 🔑 Replace with your Groq API key
    base_url="https://api.groq.com/openai/v1"  # ✅ Important for Groq
)

# Streamlit page setup
st.set_page_config(page_title="MinnalX ", page_icon="⚡")
st.title("I am Minnal😉⚡")

def fetch_webpage_text(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # Remove unwanted elements (scripts, styles, navbars, footers, ads)
        for tag in soup(["script", "style", "header", "footer", "nav", "aside"]):
            tag.decompose()

        # Get cleaned text
        text = soup.get_text(separator="\n")
        cleaned = "\n".join([line.strip() for line in text.splitlines() if line.strip()])

        return cleaned[:5000]  # limit length
    except Exception as e:
        return f"Error fetching page: {e}"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "Your name is minnalX,You are a helpful marketing AI assistant."}
    ]

# Display chat history
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    elif msg["role"] == "assistant":
        st.chat_message("assistant").write(msg["content"])

# Input box for user prompt
if prompt := st.chat_input("Type your message or paste a link..."):
    st.session_state["messages"].append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # If user pasted a link
    if prompt.startswith("http://") or prompt.startswith("https://"):
        webpage_text = fetch_webpage_text(prompt)
        st.write("🔎 Fetched webpage content... summarizing...")
        user_prompt = f"Here is the webpage content:\n\n{webpage_text}\n\nPlease summarize or explain this."
    else:
        user_prompt = prompt

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=st.session_state["messages"] + [{"role": "user", "content": user_prompt}]
        )
        reply = response.choices[0].message.content
        st.session_state["messages"].append({"role": "assistant", "content": reply})
        st.chat_message("assistant").write(reply)

    except Exception as e:
        st.error(f"⚠️ Error: {e}")

