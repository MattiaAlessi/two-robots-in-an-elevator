"""Write the robot's elevator small talk to /output/entry.txt.

One funny line, under 200 characters, that one robot says to another while
they ride an elevator together. The program writes the same bytes every run.
"""

import os

LINE = "Nice LEDs. Are those for status, or just for morale?"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as out:
        out.write(LINE)


if __name__ == "__main__":
    main()
