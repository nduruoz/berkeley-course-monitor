import requests

import os
import requests

TOPIC = os.getenv("NTFY_TOPIC")

def notify(title, message):
    requests.post(
        f"https://ntfy.sh/{TOPIC}",
        data=message.encode("utf-8"),
        headers={
            "Title": title,
            "Priority": "5",
            "Tags": "warning,books"
        }
    )
