import requests
from fastapi import HTTPException

FACEBOOK_GRAPH_URL = "https://graph.facebook.com/me"

def get_user_data(access_token:str):
    """
    Validates the access token and retrieves the user's Facebook data (ID, name, email).
    """
    params = {
        'access_token': access_token,
        'fields': 'id,name,email'
    }
    
    response = requests.get(FACEBOOK_GRAPH_URL, params=params)

    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Invalid access token or error fetching data from Facebook.")
        
    return response.json()
