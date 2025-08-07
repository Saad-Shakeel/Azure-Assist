
# Azure Assist 🌐

Azure Assist is a Streamlit-powered chatbot designed to help users master Microsoft Azure. It leverages Google Gemini for conversational AI and integrates Lakera Guard for input safety, ensuring responses are focused exclusively on Azure topics.

## Features
- **Azure-Only Specialist**: Answers only Azure-related queries, with off-topic redirection.
- **Gemini AI Integration**: Uses Google Gemini (via `google.generativeai`) for natural language responses.
- **Lakera Guard Safety**: All user inputs are checked for safety before generating a response.
- **Modern UI**: Custom media buttons for LinkedIn, GitHub, and Gmail contact.
- **Session Management**: Start new chat sessions and maintain chat history.

## Getting Started

### Prerequisites
- Python 3.12+
- [Streamlit](https://streamlit.io/)
- Google Gemini API Key
- Lakera Guard API Key

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Saad-Shakeel/Azure-Assist.git
   cd Azure-Assist
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Add your API keys to Streamlit secrets:
   - Create a `.streamlit/secrets.toml` file:
     ```toml
     GEMINI_API_KEY = "your-gemini-api-key"
     LAKERA_GUARD_API_KEY = "your-lakera-guard-api-key"
     ```

### Running the App
```bash
streamlit run main.py
```

## Usage
- Enter your Azure-related questions in the chat input.
- The bot will respond with concise, clear answers and may include links to official Azure documentation.
- Off-topic questions are politely redirected.
- Use the "Start New Chat" button to reset the session.

## File Structure
- `main.py` — Streamlit app entry point
- `Lakera_Guard.py` — Lakera Guard API integration
- `media_btns.py` — Custom social/contact buttons
- `logo.png` — App icon
- `requirements.txt` — Python dependencies


## License
MIT
