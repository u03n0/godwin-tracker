from openai import OpenAI

client = OpenAI(api_key='mykey')



def chat_with_gpt(messages):
    response = client.chat.completions.create(model="gpt-4",
    messages=messages,
    temperature=0.7,
    max_tokens=150)
    return response.choices[0].message.content

convesation_history = [{"role": "system", "content": "You are a young, politically aware chatbot
                        who speaks casually."}]

def add_message_to_history(role, content):
    convesation_history.append({"role": role, "content": content})

def get_bot_response(user_input):
    add_message_to_history("user", user_input)
    bot_response = chat_with_gpt(convesation_history)
    add_message_to_history("assistant", bot_response)
    return bot_response


