import requests
import streamlit as st

# Load API key from Streamlit secrets
LAKERA_GUARD_API_KEY = st.secrets["LAKERA_GUARD_API_KEY"]

# Initialize Lakera Guard HTTP client
lakera_client = requests.Session()
lakera_client.headers.update({
    "Authorization": f"Bearer {LAKERA_GUARD_API_KEY}",
    "Content-Type": "application/json"
})

def check_input_with_lakera_guard(user_question: str) -> dict:
    """
    Checks user input against Lakera Guard for unsafe content.
    
    Returns:
        dict: {"blocked": bool, "message": str}
    """
    try:
        response = lakera_client.post(
            "https://api.lakera.ai/v2/guard",
            json={
                "messages": [
                    {"role": "user", "content": user_question}
                ],
                "breakdown": True
            }
        )
        response.raise_for_status()
        guard_response = response.json()

        flagged = False
        if "results" in guard_response:
            for result in guard_response["results"]:
                if result.get("flagged", False):
                    flagged = True
                    break
        else:
            flagged = guard_response.get("flagged", False)

        if flagged:
            return {"blocked": True, "message": "Your query contains unsafe or restricted content."}
        return {"blocked": False, "message": ""}

    except requests.exceptions.RequestException as e:
        st.error(f"Lakera Guard API error: {e}")
        return {"blocked": False, "message": ""}
