import os
import re
from PIL import Image

tex_files = [f for f in os.listdir('.') if f.endswith('.tex') and 'Lecture 1.' in f]
for tf in tex_files:
    print(f"\n--- Processing {tf} ---")
    with open(tf, 'r') as f:
        content = f.read()

    # Apply fixes for missing ../ in path if they point directly to the artifact folder
    content = re.sub(r'\\includegraphics(.*?){\s*(Lecture 1\.\d+.*?_artifacts/.*?)\s*}', r'\\includegraphics\1{../\2}', content)

    # Let's write it down so we can read line by line
    with open(tf, 'w') as f:
        f.write(content)

    with open(tf, 'r') as f:
        lines = f.readlines()

    new_lines = []
    
    for line in lines:
        match = re.search(r'\\includegraphics.*?{(.*?)}', line)
        if match:
            path = match.group(1)
            try:
                # Let's try to open relative to the current working dir ('Milav Dabgar')
                with Image.open(path) as pi:
                    new_lines.append(line) # image exists
            except Exception as e:
                print(f"Removing broken image line: {path} because {e}")
                # Don't append line
        else:
            new_lines.append(line)

    with open(tf, 'w') as f:
        f.writelines(new_lines)

