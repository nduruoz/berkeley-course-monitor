import time
import subprocess

while True:
    print("Checking Berkeley...")

    subprocess.run(["python", "monitor.py"])

    print("Waiting 60 seconds...\n")

    time.sleep(60)
    