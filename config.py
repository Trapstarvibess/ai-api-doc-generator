import os
from dotenv import load_dotenv

load_dotenv()

def get_openrouter_key():
    # Streamlit secrets will override .env if available
    return os.getenv("OPENROUTER_API_KEY") or os.environ.get("OPENROUTER_API_KEY")
