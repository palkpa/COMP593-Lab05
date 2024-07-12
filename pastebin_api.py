import requests

def create_paste(title, body_text, expiration='1M', public=False):
    """
    Creates a new PasteBin paste.

    Args:
        title (str): Title of the paste.
        body_text (str): Content of the paste.
        expiration (str): Expiration time for the paste (e.g., '10M' for 10 minutes, '1M' for 1 month).
        public (bool): Whether the paste should be publicly listed.

    Returns:
        str: URL of the newly created paste if successful, None otherwise.
    """
    print("Creating a new PasteBin paste...")

    PASTEBIN_API_KEY = 'U92yUvAhCHLRHzBnnPqAPGPjN2_4l_3P'
    PASTEBIN_API_URL = 'https://pastebin.com/doc_api'

    payload = {
        'api_dev_key': PASTEBIN_API_KEY,
        'api_option': 'paste',
        'api_paste_code': body_text,
        'api_paste_name': title,
        'api_paste_expire_date': expiration,
        'api_paste_private': 1 if not public else 0,
    }

    response = requests.post(PASTEBIN_API_URL, data=payload)

    if response.status_code == 200:
        print("Paste created successfully.")
        return response.text
    else:
        print("Failed to create paste.")
        return None
