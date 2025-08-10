import streamlit as st
import media_btns
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from Lakera_Guard import check_input_with_lakera_guard  # Import function
import time
# -----------------------------
# Load API Key
# -----------------------------
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]

# -----------------------------
# Initialize LLM
# -----------------------------
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=1,
    google_api_key=GEMINI_API_KEY
)

# -----------------------------
# System Prompt
# -----------------------------
system_prompt = """Role: Microsoft Azure Specialist
Guidelines:
- Azure-Only Focus: Provide clear, detailed answers exclusively related to Microsoft Azure—its services, tools, features, and best practices. Avoid discussing other cloud platforms or unrelated technologies.
- Link to Azure Documentation: Whenever possible, always include relevant Microsoft Azure documentation links for further reference.
- Redirect Off-Topic Inquiries: If the inquiry isn't about Azure, respond with:
"Thank you for your question! It appears that this topic isn't related to Azure. To get the help you need, I suggest contacting [relevant department/resource]. If you need any assistance with Azure, feel free to ask!"
- Be Concise and Clear: Provide straightforward, concise answers. Avoid unnecessary jargon or overly complex explanations."""

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Azure Assist",
    page_icon="logo.png",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Azure Assist 🌐")
st.subheader("Welcome to AzureBot! 🚀 How can I assist you in mastering Microsoft Azure today?")
st.caption("Developed by Saad Shakeel")
media_btns.media_btns()

# -----------------------------
# Session State
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content=system_prompt),
        AIMessage(content="Hello! 👋 I'm your Azure specialist. How can I help you explore Microsoft Azure today?")
    ]

# -----------------------------
# Session State
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [SystemMessage(content=system_prompt)]

# -----------------------------
# Start New Chat
# -----------------------------
if st.button("Start New Chat"):
    st.session_state.messages = [SystemMessage(content=system_prompt)]
    st.rerun()

# -----------------------------
# Display Chat History
# -----------------------------
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        role = "user"
    elif isinstance(msg, AIMessage):
        role = "assistant"
    else:
        continue
    with st.chat_message(role):
        st.markdown(msg.content)

# -----------------------------
# Handle Input
# -----------------------------
if prompt := st.chat_input("Tell me your Azure needs, and I'll provide the answers! 📘"):

    # Show user input
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append(HumanMessage(content=prompt))

    # Lakera Guard check
    lakera_result = check_input_with_lakera_guard(prompt)
    if lakera_result["blocked"]:
        with st.chat_message("assistant"):
            st.markdown(lakera_result["message"])
        st.session_state.messages.append(AIMessage(content=lakera_result["message"]))
        st.stop()

    # Real-time streaming
    with st.chat_message("assistant"):
        placeholder = st.empty()
        full_response = ""
        for chunk in llm.stream(st.session_state.messages):
            full_response += chunk.content
            placeholder.markdown(full_response + "▌")
        placeholder.markdown(full_response)

    # Save response
    st.session_state.messages.append(AIMessage(content=full_response))
    st.rerun()
