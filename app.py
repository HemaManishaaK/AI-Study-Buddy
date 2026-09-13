import os
import streamlit as st
from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

st.set_page_config(page_title="AI Study Buddy", page_icon="📚")

st.title("📚 AI Study Buddy")
st.write("Learn any topic using Generative AI.")

if not api_key:
    st.error("GEMINI_API_KEY is not set. Add it to your .env file.")
    st.stop()

client = genai.Client(api_key=api_key)

topic = st.text_input("Enter a topic", placeholder="Example: Neural Networks")

option = st.selectbox(
    "Choose what you want",
    ["Explain Topic", "Generate Notes", "Generate Quiz"]
)

if st.button("Generate"):
    if not topic:
        st.warning("Please enter a topic.")
    else:
        if option == "Explain Topic":
            prompt = f"Explain {topic} in simple beginner-friendly language with a small example."

        elif option == "Generate Notes":
            prompt = f"Create short, clear study notes for {topic}. Use headings and bullet points."

        else:
            prompt = f"Create 5 multiple-choice questions about {topic}. Give four options for each question and clearly mention the correct answer."

        with st.spinner("Generating..."):
            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=prompt
            )

        st.subheader("AI Response")
        st.write(response.text)
