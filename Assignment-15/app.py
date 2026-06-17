import sys
from datetime import datetime

print("=" * 40)
print("Dockerized Python Application")
print("=" * 40)

print(f"Python Version: {sys.version}")

print(
    f"Current Date & Time: "
    f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
)

print("=" * 40)