import os
import re
import sys

def convert_md_to_beamer(md_filepath, tex_filepath):
    with open(md_filepath, 'r') as f:
        content = f.read()

    slides_raw = re.split(r'!\[Image\]\((.*?)\)', content)
    
    ignore_texts = [
        "Module 01",
        "Partha Pratim Das",
        "Objectives &amp; Outline",
        "Objectives & Outline",
        "Why Databases?",
        "Know Your Course",
        "Course Outline",
        "Course Text Book",
        "Module Summary",
        "Department of Computer Science and Engineering Indian Institute of Technology, Kharagpur ppd@cse.iitkgp.ac.in",
        "Database Management Systems Module 01: Course Overview",
        "Database Management Systems",
        "·"
    ]
    
    preamble = r"""\documentclass[aspectratio=169, xcolor=dvipsnames]{beamer}

% --- Theme Setup ---
\usetheme{Madrid}
\usecolortheme{default}

% --- Packages ---
\usepackage{graphicx}
\usepackage{xcolor}
\usepackage{booktabs}
\usepackage{hyperref}
\usepackage{adjustbox}
\usepackage{amssymb} % for \triangleright
\usepackage{longtable}

% --- Title Information ---
\title[Course Overview]{Module 01: Course Overview}
\author{Milav Dabgar}
\institute{Diploma in ICT}
\date{\today}

\begin{document}

% Title Slide
\begin{frame}
    \titlepage
\end{frame}

"""
    
    out_lines = [preamble]
    base_dir = os.path.dirname(md_filepath)

    for i in range(1, len(slides_raw), 2):
        img_path = slides_raw[i]
        slide_text = slides_raw[i+1]
        
        lines = slide_text.split('\n')
        clean_lines = []
        for line in lines:
            line_stripped = line.strip()
            if not line_stripped:
                continue
                
            skip = False
            for ign in ignore_texts:
                if line_stripped == ign or line_stripped == ign.replace("&amp;", "&"):
                    skip = True
                    break
            
            if line_stripped in ['.', ',', '◦', '· · ·', '|']:
                skip = True
                
            # Ignore markdown table dashed lines temporarily for simpler rendering
            if line_stripped.startswith("|---"):
                skip = True
                
            if skip:
                continue
                
            clean_lines.append(line_stripped)
            
        full_img_path = os.path.join(base_dir, img_path)
        img_exists = os.path.exists(full_img_path)
        
        if not clean_lines and not img_exists:
            continue 
            
        out_lines.append(r"\begin{frame}")
        
        title_added = False
        in_itemize = False
        in_table = False
        
        for line in clean_lines:
            if line.startswith("## ") and not title_added:
                title = line[3:].strip()
                out_lines[-1] = r"\begin{frame}{" + title + "}"
                title_added = True
                continue
                
            if line.startswith("## ") and title_added:
                if not in_table and not in_itemize:
                    out_lines.append(r"\framesubtitle{" + line[3:].strip() + "}")
                continue
                
            # Basic markdown table support
            if line.startswith("|") and line.endswith("|"):
                if re.match(r"^\|(\s*-+\s*\|)+$", line):
                    continue # Skip separator row
                    
                if not in_table:
                    out_lines.append(r"\begin{center}")
                    out_lines.append(r"\begin{tabular}{|l|l|}") # simple 2 columns approx
                    out_lines.append(r"\hline")
                    in_table = True
                
                row = line.strip("|").split("|")
                # Escape characters in table cells
                row_esc = [cell.strip().replace("&", r"\&").replace("%", r"\%").replace("$", r"\$").replace("#", r"\#").replace("_", r"\_") for cell in row]
                row_tex = " & ".join(row_esc) + r" \\ \hline"
                out_lines.append(row_tex)
                continue
            else:
                if in_table:
                    out_lines.append(r"\end{tabular}")
                    out_lines.append(r"\end{center}")
                    in_table = False

            if line.startswith("- "):
                if not in_itemize:
                    out_lines.append(r"\begin{itemize}")
                    in_itemize = True
                
                item_text = line[2:].strip()
                if item_text.startswith("glyph[triangleright]"):
                    item_text = item_text.replace("glyph[triangleright]", "").strip()
                    item_text = item_text.replace("&", r"\&").replace("%", r"\%").replace("$", r"\$").replace("#", r"\#").replace("_", r"\_")
                    out_lines.append(r"    \item[$\triangleright$] " + item_text)
                else:
                    item_text = item_text.replace("&", r"\&").replace("%", r"\%").replace("$", r"\$").replace("#", r"\#").replace("_", r"\_")
                    out_lines.append(r"    \item " + item_text)
            elif line.startswith("http://") or line.startswith("https://"):
                if in_itemize:
                    out_lines.append(r"\end{itemize}")
                    in_itemize = False
                out_lines.append(r"\url{" + line + r"}")
            else:
                if in_itemize:
                    out_lines.append(r"\end{itemize}")
                    in_itemize = False
                    
                line_tex = line.replace("&", r"\&").replace("%", r"\%").replace("$", r"\$").replace("#", r"\#").replace("_", r"\_")
                out_lines.append(line_tex)
                
        if in_itemize:
            out_lines.append(r"\end{itemize}")
        if in_table:
            out_lines.append(r"\end{tabular}")
            out_lines.append(r"\end{center}")
            
        full_img_path = os.path.join(base_dir, img_path)
        if os.path.exists(full_img_path):
            out_lines.append(r"\vspace{1em}")
            out_lines.append(r"\begin{center}")
            out_lines.append(rf"    \includegraphics[height=0.6\textheight, width=0.8\textwidth, keepaspectratio]{{{img_path}}}")
            out_lines.append(r"\end{center}")
            
        out_lines.append(r"\end{frame}")
        out_lines.append("")
        
    out_lines.append(r"\end{document}")
    
    with open(tex_filepath, 'w') as f:
        f.write('\n'.join(out_lines))
        
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python md_to_beamer.py <input.md> <output.tex>")
        sys.exit(1)
    convert_md_to_beamer(sys.argv[1], sys.argv[2])
