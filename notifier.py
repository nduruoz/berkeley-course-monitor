import os
import requests

TOPIC = os.getenv("NTFY_TOPIC")

def notify(title, message):
    headers = {
        "Title": title,
        "Priority": "5",
        "Tags": "warning,books",
    }

    print("Before requests.post", flush=True)

    response = requests.post(
        f"https://ntfy.sh/{TOPIC}",
        data=message.encode("utf-8"),
        headers=headers,
    )

    print("After requests.post", flush=True)

    response.raise_for_status()