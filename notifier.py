import requests

TOPIC = "duru-berkeley-course-8fe9kc"

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
    