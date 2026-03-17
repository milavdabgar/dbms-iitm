import os
import re

files = ["Lec 9.1.tex", "Lec 9.2.tex", "Lec 9.3.tex", "Lec 9.4.tex", "Lec 9.5.tex"]

for file in files:
    with open(file, "r") as f:
        content = f.read()
    
    # We want to replace basic blocks with nothing, or exampleblock/alertblock based on context.
    # We will do this via regex. A basic block looks like:
    # \begin{block}{...} (often empty {})
    # ...
    # \end{block}
    
    # Actually, first let's just count how many we have to see what we are dealing with.
    blocks = re.findall(r'\\begin{block}', content)
    print(f"{file} has {len(blocks)} blocks.")
