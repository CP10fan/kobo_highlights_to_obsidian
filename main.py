#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 14:13:11 2026

@author: usaid
"""

book_title = "My First Book"
highlight = "Small steps make a big difference"
chapter = "Chapter 1"
#My template in obsidian
excerpt = f"""## Excerpt
**Chapter:** {chapter}
**Page / Location:**
> {highlight}

### Thoughts: 

source:
tags: 

---
"""
print(excerpt)

from pathlib import Path
# Path(__file__).parent finds the folder containing main.py
# / "sample_highlights.md" builds the destination file path.
output_path = Path(__file__).parent / "sample_highlights.md"
# "w" is write mode, creates or replaces the file of its contents if it already exists.
# encoding="utf-8" supports characters such as curly quotes.
# with closes the file automatically when the indented code finishes.
with open(output_path, "w", encoding="utf-8") as file:
    file.write(excerpt)
# file.write(excerpt) saves your formatted text