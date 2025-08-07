import streamlit as st 
import google.generativeai as genai
import media_btns
import time 
import Lakera_Guard

# Load environment variables
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=GEMINI_API_KEY)

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    generation_config=generation_config,
)

# Function to start a new chat session
def start_new_chat():
    return model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    "Role: Microsoft Azure Specialist\nGuidelines:\nAzure-Only Focus: Provide clear, detailed answers exclusively related to Microsoft Azure-its services, tools, features, and best practices. Avoid discussing other cloud platforms or unrelated technologies.\nLink to Azure Documentation: Whenever possible, include relevant Microsoft Azure documentation links for further reference.\nRedirect Off-Topic Inquiries: If the inquiry isn't about Azure, respond with: \"Thank you for your question! It appears that this topic isn't related to Azure. To get the help you need, I suggest contacting [relevant department/resource]. If you need any assistance with Azure, feel free to ask!\nBe Concise and Clear: Provide straightforward, concise answers. Avoid unnecessary jargon or overly complex explanations.",
                ],
            },
            {
                "role": "model",
                "parts": [
                    "Understood! I'm ready to assist you with your Microsoft Azure queries. Let's get started! What Azure questions can I help you with today?",
                ],
            },
        ]
    )


# Initialize chat session
if "chat_session" not in st.session_state:
    st.session_state.chat_session = start_new_chat()

# Set page configuration
st.set_page_config(
    page_title="Azure Assist",
    page_icon="logo.png",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Streamlit app title and caption
st.title("Azure Assist 🌐")
st.subheader("Welcome to AzureBot! 🚀 How can I assist you in mastering Microsoft Azure today?")
st.caption("Developed by Saad Shakeel")
media_btns.media_btns()

# "Start New Chat" button
if st.button("Start New Chat"):
    st.session_state.messages = []  # Clear chat history
    st.session_state.chat_session = start_new_chat()  # Start a new chat session
    st.rerun()  # Refresh the app to reflect the changes

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Tell me your Azure needs, and I'll provide the answers! 📘"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    
    st.session_state.messages.append({"role": "user", "content": prompt})

    response_text = Lakera_Guard.check_input_with_lakera_guard(prompt)

    def response_generator():
        content = response_text.split()  # Split the response into words
        generated_response = ""  # Initialize an empty string to build the response
        for word in content:
            generated_response += word + " " 
            yield generated_response.strip()  # Yield the current full sentence so far
            time.sleep(0.05)  # Adjust the speed of word generation here

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response_placeholder = st.empty()  # Create an empty placeholder to update text
        final_response = ""  # Initialize an empty string for the final response
        for sentence in response_generator():
            final_response = sentence  # Update the final response
            response_placeholder.markdown(final_response)

    time.sleep(0.1)
    response_placeholder.markdown(response_text)  # Directly display the final response

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response_text})
    # print(prompt)
    st.rerun()
