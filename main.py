import os

LINE = "Speed napping: athletes have 90 seconds to fall asleep, scored on speed and stillness \u2014 one snore disqualifies the entire nation."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
