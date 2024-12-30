import streamlit as st
import requests

# Initialize Lakera Guard client
LAKERA_GUARD_API_KEY = st.secrets["LAKERA_GUARD_API_KEY"]
lakera_client = requests.Session()
lakera_client.headers.update({
    'Authorization': f'Bearer {LAKERA_GUARD_API_KEY}'
})
# Function to check input with Lakera Guard
def check_input_with_lakera_guard(user_question: str):
    # Step 1: Send the user question to Lakera Guard
    response = lakera_client.post(
        "https://api.lakera.ai/v2/guard",
        json={
            "messages": [
                {
                    "role": "user",
                    "content": user_question
                }
            ],
            "breakdown": True
        }
    )
    guard_response = response.json()
    
    # Step 2: Check if Lakera Guard flagged the content as inappropriate
    if guard_response.get("flagged"):
        return "Warning: Attempting to access restricted or protected data without proper credentials is against our security policy. Please contact your system administrator if you require legitimate access to this information."
    
    # Step 3: If safe, pass the input to the chat model for response generation
    chat_session = st.session_state.chat_session
    return chat_session.send_message(user_question).text
