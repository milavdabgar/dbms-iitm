import os
import re
from PIL import Image

tex_files = [f for f in os.listdir('.') if f.endswith('.tex') and 'Lecture 1.' in f]
for tf in tex_files:
    print(f"\n--- Checking {tf} ---")
    with open(tf, 'r') as f:
        content = f.read()

    # Update Title/Subtitle
    content = re.sub(r'\\title\[.*?\]{(.*?):\s*(.*?)}', r'\\title{\1}\n\\subtitle{\2}', content)

    # Update Institute
    content = re.sub(r'\\institute\{.*?\}', r'\\institute{www.milav.in}', content)

    # Find images
    images = re.findall(r'\\includegraphics.*?{(.*?)}', content)
    for img in images:
        path = img
        
        try:
            with Image.open(path) as pi:
                w, h = pi.size
                print(f"{path}: {w}x{h} (Aspect Ratio: {w/h:.2f})")
        except Exception as e:
            print(f"Error opening {path}: {e}")

    # write back
    with open(tf, 'w') as f:
        f.write(content)
