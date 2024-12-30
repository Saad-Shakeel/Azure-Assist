# Azure Assist Chatbot

## Overview
Azure Assist Chatbot is an intelligent virtual assistant designed to handle queries specifically related to Microsoft Azure. Built using Python and the Streamlit platform, the chatbot leverages the **Gemini-1.5-Flash** model to deliver accurate and context-aware responses. 

The chatbot uses a **system prompt** to enforce a strict operational scope, ensuring it only responds to questions related to Microsoft Azure. If a user's query is unrelated to Azure, the chatbot politely declines to answer, maintaining focus on its domain of expertise. 

To safeguard against prompt injection attacks (malicious attempts to alter the chatbot’s behavior through user inputs), we integrate **Lakera Guard**, a robust security framework for language models.

---

## Key Features

1. **Gemini-1.5-Flash Model**:
   - The chatbot is powered by the Gemini-1.5-Flash model, offering state-of-the-art language understanding and generation.
   - Obtain the LLM API from [Google AI Studio](https://aistudio.google.com/apikey) and store it in the `API_KEYS.py` file under the variable name `Gemeni_API`.

2. **Prompt Injection Protection**:
   - To safeguard against prompt injection attacks that could alter the chatbot's behavior, the project integrates **Lakera Guard**.
   - Acquire the Lakera Guard API key from [Lakera Guard's website](https://platform.lakera.ai/account/api-keys) and store it in the `API_KEYS.py` file under the variable name `LAKERA_GUARD_API_KEY`.

3. **Streamlit Application**:
   - Built on Streamlit, enabling an intuitive and interactive user interface for the chatbot.

---

## Setup Instructions

### Prerequisites

- Python 3.8 or higher installed on your system.
- Basic familiarity with Python and Streamlit.

### Installation Steps

1. **Install Dependencies**:  
   Install the required Python packages using the `requirements.txt` file:
   pip install -r requirements.txt

2. **Add API Keys**:  
   - Open the `API_KEYS.py` file in your project directory.
   - Add the following API keys:
     ```python
     Gemeni_API = "<your-gemini-api-key>"
     LAKERA_GUARD_API_KEY = "<your-lakera-guard-api-key>"
     ```

4. **Run the Application**:  
   Start the Streamlit chatbot application by running:
   ```
   python -m streamlit run main.py
   ```

