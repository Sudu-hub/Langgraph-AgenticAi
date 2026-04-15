import streamlit as st
from langgraph_backend import chatbot  # assuming chatbot has an invoke() method

# Initialize message history
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

# Display the conversation
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

# Get user input
user_input = st.chat_input('Type here')

if user_input:
    # Add user message
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.text(user_input)

    # Call your backend chatbot
    response = chatbot.invoke(user_input)  # <-- pass input to chatbot

    # Add assistant message
    st.session_state['message_history'].append({'role': 'assistant', 'content': response})
    with st.chat_message('assistant'):
        st.text(response)
