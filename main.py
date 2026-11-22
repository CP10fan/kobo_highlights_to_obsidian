#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 14:13:11 2026

@author: usaid
"""
book_title = "My First Book"
highlight = "Small steps make a big difference."
chapter = "Chapter 1"

excerpt = f"""## Excerpt

> {highlight}

**Chapter:** {chapter}
**Page / Location:**

---

"""
print(excerpt)

from pathlib import Path
output_path = Path(__file__).parent / "sample_highlights.md"
# Path(__file__).parent finds the folder containing main.py
# / "sample_highlights.md" builds the destination file path.
with open(output_path, "w", encoding="utf-8") as file:
    file.write(excerpt)
# "w" is write mode, creates or replaces the file of its contents if it already exists.
# encoding="utf-8" supports characters such as curly quotes.
# with closes the file automatically when the indented code finishes.
# file.write(excerpt) saves your formatted text
