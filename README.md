Bank Agent Project (Assignment 04)
AI-Powered Terminal Banking Assistant
This project provides an interactive, terminal-based banking assistant. Users can check balances, transfer funds, apply for loans, and request callbacks all via a simple CLI interface—with account context passed in-memory for seamless operation.

Features
Check Balance: Displays the authenticated user's account balance.

Transfer Funds: Safely transfer funds between accounts (simulated in-memory).

Loan Applications: Receive loan options and submit applications.

Request Callback: Easily send a callback request.

Modular Design: Separated code into main.py, functions.py, context.py, and agents_config.py for clarity and extensibility.

Getting Started
Prerequisites
Python 3.10+

Virtual environment (venv) recommended

Installation Steps
bash
Copy
Edit
# 1. Clone the repository
git clone https://github.com/anusbutt/Agentic_SDK_Assignment_04.git
cd Agentic_SDK_Assignment_04

# 2. Activate virtual environment
python -m venv .venv
# Windows:
.venv\Scripts\activate  
# macOS/Linux:
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
Usage
Run the agent from the terminal:

bash
Copy
Edit
python main.py
Example interaction:

pgsql
Copy
Edit
you: check balance
Your current balance is $1500.75.
The assistant will prompt for user input and respond based on your context setup in main.py.

Project Structure
graphql
Copy
Edit
├── main.py             # Entry point: CLI and streaming logic
├── agents_config.py    # The Traige_Agent configuration (tools + instructions)
├── guardrails.py       # Optional guardrail logic (can be ignored if unused)
├── functions.py        # Core banking functions: balance, transfer, loans, etc.
├── context.py          # Pydantic context models (UserContext, TransferContext...)
├── configuration.py    # Run configuration for the Agent runtime
├── tool.py             # Utility helpers (if any)
├── requirements.txt
└── .gitignore
Recommendations
Add balance persistence or in-memory ledger to retain state between operations.

Build a web interface using FastAPI or Streamlit for a more user-friendly experience.

Integrate a real database backend for production-grade account management.

Use Gemini or OpenAI SDKs if you plan to connect it to a generative AI model.

License
MIT License © 2025 Anus Butt