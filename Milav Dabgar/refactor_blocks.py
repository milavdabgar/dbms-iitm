import os
import re

files = ["Lec 9.1.tex", "Lec 9.2.tex", "Lec 9.3.tex", "Lec 9.4.tex", "Lec 9.5.tex"]

for filename in files:
    with open(filename, "r") as f:
        content = f.read()
    
    new_lines = []
    lines = content.split('\n')
    
    in_frame = False
    current_frame_title = ""
    in_block = False
    block_type_to_use = None
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        frame_match = re.search(r'\\begin{frame}(?:\[.*?\])?{(.*?)}', line)
        if frame_match:
            current_frame_title = frame_match.group(1).lower()
            in_frame = True
        
        if r'\end{frame}' in line:
            in_frame = False
            current_frame_title = ""
            
        block_match = re.search(r'\\begin{block}{(.*?)}', line)
        if block_match:
            block_title = block_match.group(1)
            
            combined_title = (current_frame_title + " " + block_title).lower()
            
            if "example" in combined_title:
                block_type_to_use = "exampleblock"
                btitle = block_title if block_title else "Example"
            elif any(w in combined_title for w in ["deficienc", "disadvantage", "important", "note", "rule", "warning", "caution"]):
                block_type_to_use = "alertblock"
                btitle = block_title if block_title else "Important"
            elif any(w in combined_title for w in ["recap", "objective", "outline", "summary"]):
                block_type_to_use = "block"
                btitle = block_title
            else:
                block_type_to_use = None # Remove block
            
            if block_type_to_use:
                indent = line[:line.find(r'\begin{block}')]
                new_lines.append(f"{indent}\\begin{{{block_type_to_use}}}{{{btitle}}}")
            else:
                pass
            in_block = True
            i += 1
            continue
            
        if r'\end{block}' in line and in_block:
            in_block = False
            if block_type_to_use:
                indent = line[:line.find(r'\end{block}')]
                new_lines.append(f"{indent}\\end{{{block_type_to_use}}}")
            else:
                pass
            i += 1
            continue
        
        # Adjust indentation if we removed the block
        if in_block and not block_type_to_use:
            # removing 4 spaces of indentation
            if line.startswith("    "):
                line = line[4:]
            
        new_lines.append(line)
        i += 1
        
    with open(filename, "w") as f:
        f.write('\n'.join(new_lines))
    print(f"Refactored {filename}")
