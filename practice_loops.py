#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 14:43:31 2026

@author: usaid
"""

highlights = [ 
    "Small steps make a big difference." , 
    "Learning takes practice." ,
    "Good questions lead to better understanding."
]
from pathlib import Path
output_path = Path(__file__).parent / "practice_highlights.md"
with open(output_path, "w", encoding = "utf-8" ) as file :
    
 for highlight in highlights:
    excerpt = f"""## Excerpt
> {highlight}

**Chapter:**
**Page / Location:**

---

"""
    file.write(excerpt)
print("Saved all highlights")
    
    
     
