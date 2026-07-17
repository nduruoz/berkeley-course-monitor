import os
import requests

TOPIC = os.getenv("NTFY_TOPIC", "...")

def notify(title, message):
    print("TITLE:", repr(title), flush=True)
    print("TOPIC:", repr(TOPIC), flush=True)

    headers = {
        "Title": title,
        "Priority": "5",
        "Tags": "warning,books"
    }

    print("HEADERS:", repr(headers), flush=True)

    # Stop here for debugging
    raise Exception("Debug stop")