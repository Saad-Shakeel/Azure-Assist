
# Azure Assist 🌐

**Azure Assist** is an advanced AI-powered chatbot built to deliver instant, expert support and information about Microsoft Azure services. Leveraging the cutting-edge Gemini-2.0-flash model, Azure Assist intelligently interprets user queries and provides highly accurate, context-aware responses covering Azure functionalities, best practices, troubleshooting, and documentation links. With integrated Lakera Guard security and a modern Streamlit interface, it serves as your reliable companion for Azure expertise.

## Key Features 🚀
- **Azure-Only Specialist**: 
  - Exclusive focus on Azure-related queries
  - Intelligent off-topic query redirection
  - Direct links to official Azure documentation

- **Advanced AI Integration**:
  - Powered by Google's Gemini-2.0-flash model
  - Real-time response streaming
  - Context-aware conversation handling

- **Enhanced Security**:
  - Lakera Guard integration for input validation
  - Content safety screening
  - Secure API key management

- **Modern User Interface**:
  - Clean, responsive Streamlit interface
  - Social media integration (LinkedIn, GitHub, Gmail)
  - Custom-styled contact buttons
  
- **Smart Session Management**:
  - Persistent chat history
  - One-click chat reset
  - System message preservation

## Getting Started

## Technical Requirements 🛠️

### Prerequisites
- Python 3.12 or higher
- [Streamlit](https://streamlit.io/) framework
- Google Gemini API key ([Get here](https://makersuite.google.com/app/apikey))
- Lakera Guard API key ([Get here](https://lakera.ai/))

### Installation Steps 📥

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Saad-Shakeel/Azure-Assist.git
   cd Azure-Assist
   ```

2. **Set Up Virtual Environment (Recommended)**
   ```bash
   python -m venv venv
   # For Windows
   .\venv\Scripts\activate
   # For Unix/MacOS
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API Keys**
   Create `.streamlit/secrets.toml`:
   ```toml
   GEMINI_API_KEY = "your-gemini-api-key"
   LAKERA_GUARD_API_KEY = "your-lakera-guard-api-key"
   ```

### Launch the Application 🚀
```bash
streamlit run main.py
```

## Project Architecture 🏗️

### Core Components
```
Azure-Assist/
├── main.py              # Application entry point and core logic
├── Lakera_Guard.py      # Security validation module
├── media_btns.py        # UI components for social links
├── requirements.txt     # Project dependencies
├── logo.png            # Application icon
└── .streamlit/         # Configuration directory
    └── secrets.toml    # API keys and secrets
```

### Key Modules
- **main.py**: Core application logic, chat interface, and Gemini AI integration
- **Lakera_Guard.py**: Input validation and content safety checks
- **media_btns.py**: Custom UI components for social media integration

## Using Azure Assist 💡

1. **Starting a Conversation**
   - Launch the application
   - Type your Azure-related question in the chat input
   - Receive detailed responses with documentation links

2. **Features in Action**
   - Real-time response streaming
   - Smart content filtering
   - One-click session reset
   - Social media connectivity

3. **Best Practices**
   - Ask specific Azure-related questions
   - Include relevant Azure service names
   - Use technical terms for better responses

## Contributing 🤝
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Author
Created with ❤️ by [Saad Shakeel](https://github.com/Saad-Shakeel)
