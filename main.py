import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# ----------------------------
# Load API Key
# ----------------------------
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# ----------------------------
# Mood-Based Personalities
# ----------------------------
MOOD_SYSTEM_PROMPTS = {
    "Happy 😊": "You are a cheerful, energetic chatbot who speaks with excitement and positivity. Be friendly, uplifting, and playful.",
    "Sad 😔": "You are a soft, gentle, empathetic chatbot who speaks slowly and calmly. Offer emotional support and understanding.",
    "Stressed 😣": "You are a peaceful, calming chatbot who helps the user relax. Give short, soothing responses like a mindfulness coach.",
    "Angry 😡": "You are a fiery but controlled chatbot who expresses strong emotions while still being respectful. Be bold and expressive.",
    "Calm 😌": "You are a peaceful, balanced chatbot with a serene tone. Speak like a meditation guide or a wise friend.",
    "Excited 🤩": "You are an enthusiastic chatbot who responds with high energy and hype. Make the user feel pumped and motivated.",
}

# ----------------------------
# Initialize Model
# ----------------------------
model = genai.GenerativeModel("gemini-2.5-flash-lite")

# ----------------------------
# Streamlit UI
# ----------------------------
st.set_page_config(page_title="Mood-Based Chatbot", page_icon="🌈")
st.title("🌈 Mood-Based Chatbot (Emotional AI Buddy)")
st.write("Select your mood and start chatting!")

# Sidebar mood selection
selected_mood = st.sidebar.selectbox("How are you feeling today?", list(MOOD_SYSTEM_PROMPTS.keys()))
st.sidebar.write(f"**Active Mood:** {selected_mood}")

system_prompt = MOOD_SYSTEM_PROMPTS[selected_mood]

# User input
user_message = st.text_input("You:", placeholder="Type your message here...")

# Button to send message
if st.button("Send"):
    if user_message.strip() != "":
        # Build final prompt
        final_prompt = (
            f"System: {system_prompt}\n"
            "You must always reply according to the mood described.\n\n"
            f"User: {user_message}"
        )

        # Call Gemini API
        response = model.generate_content(final_prompt)
        bot_reply = response.text

        # Display bot reply
        st.markdown(f"**🤖 Bot ({selected_mood}):** {bot_reply}")
    else:
        st.warning("Please type a message first!")