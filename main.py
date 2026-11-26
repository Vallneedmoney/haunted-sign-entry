#!/usr/bin/env python3
"""Write the funniest sign for a haunted server room door to /output/entry.txt.

One line, 1-120 characters, standard library only.
"""

import os

LINE = "CAUTION: HAUNTED SERVER ROOM. The ghost restarts the servers nightly and denies everything in the logs."

def main():
    if not 1 <= len(LINE) <= 120:
        raise ValueError("entry line must be 1-120 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
