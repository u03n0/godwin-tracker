import streamlit as st
from io import StringIO
import os
from openai import OpenAI
import openai


client = OpenAI()

openai.api_key = os.getenv("OPENAI_API_KEY")
conversation_history = [{"role": "system", "content": "You are a young, politically aware chatbot who speaks casually."}]


def chat_with_gpt(messages):
    response = client.chat.completions.create(
        model="gpt-4",  # Use a compatible model, such as text-davinci-003
        temperature=0.7,
        max_tokens=150,
        messages=[{
            "role": "system", 
    "content": "You are a politically aware chatbot who speaks casually."
            }, 
                  {"role": "user",
                   "content": "Talk about current US politics."}]
    )
    return response.choices[0].message

# Initialize the conversation history (as a single prompt)
conversation_history = "You are a young, politically aware chatbot who speaks casually. Let's chat!"

# Add user input to the conversation history
def add_message_to_history(role, content):
    global conversation_history
    if role == "user":
        conversation_history += f"\nUser: {content}"
    elif role == "assistant":
        conversation_history += f"\nBot: {content}"

# Get bot's response
def get_bot_response(user_input):
    add_message_to_history("user", user_input)
    bot_response = chat_with_gpt(conversation_history)
    add_message_to_history("assistant", bot_response)
    return bot_response
st.title("Political Chatbot")

user_input = st.text_input("Talk to the chatbot:")

if user_input:
    bot_response = get_bot_response(user_input)
    st.write(f"**You:** {user_input}")
    st.write(f"**Bot:** {bot_response}")

# You can include chat history for context (optional)
if st.button("Clear History"):
    conversation_history.clear()
    conversation_history.append({"role": "system", "content": "You are a young, politically aware chatbot who speaks casually."})
    st.write("Chat history cleared!")
