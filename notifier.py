import os
import requests

TOPIC = os.getenv("NTFY_TOPIC", "...")

def notify(title, message):
    print(f"title = {title!r}")
    print(f"headers = {{'Title': {title!r}, 'Priority': '5', 'Tags': 'warning,books'}}")

    response = requests.post(
        f"https://ntfy.sh/{TOPIC}",
        data=message.encode("utf-8"),
        headers={
            "Title": title,
            "Priority": "5",
            "Tags": "warning,books"
        }
    )

    response.raise_for_status()