# visualize_emotion_curve.py

import json
import matplotlib.pyplot as plt
from datetime import datetime

# Load chat data
with open("sample_chat_data.json", "r") as f:
    data = json.load(f)

# Extract emotion timeline
timestamps = [datetime.fromisoformat(item["timestamp"]) for item in data]
emotions = [item["emotion"] for item in data]
cognitions = [item["cognition"] for item in data]
speakers = [item["speaker"] for item in data]

# Plot
plt.figure(figsize=(10, 5))
plt.plot(timestamps, emotions, marker='o', label="Emotion")
plt.plot(timestamps, cognitions, marker='x', linestyle='--', label="Cognition")
for i, name in enumerate(speakers):
    plt.text(timestamps[i], emotions[i] + 0.05, name, fontsize=9, ha='center')

plt.axhline(0, color='gray', linestyle='--', linewidth=0.5)
plt.title("Emotion & Cognition Over Time")
plt.xlabel("Time")
plt.ylabel("Score")
plt.legend()
plt.tight_layout()
plt.savefig("emotion_curve.png")
plt.show()
