from src.converter import clean_html_to_latex

LATEX_PREAMBLE = r"""\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[margin=0.75in]{geometry}
\usepackage{amsmath,amssymb,amsfonts,mathtools,extarrows,esint}
\usepackage{graphicx}
\usepackage[export]{adjustbox}
\usepackage{tcolorbox}
\usepackage{enumitem}
\usepackage{xcolor}
\usepackage{hyperref}
\usepackage{booktabs}
\usepackage{array}
\usepackage{tocloft}

\definecolor{primary}{RGB}{31, 78, 121}
\definecolor{secondary}{RGB}{47, 109, 26}
\definecolor{accent}{RGB}{204, 51, 0}
\definecolor{boxbg}{RGB}{245, 247, 250}

\hypersetup{
    colorlinks=true,
    linkcolor=primary,
    urlcolor=primary,
}

\tcbset{
    solbox/.style={
        colback=boxbg,
        colframe=primary,
        fonttitle=\bfseries,
        coltitle=white,
        boxrule=0.8pt,
        arc=4pt,
        left=8pt,
        right=8pt,
        top=6pt,
        bottom=6pt
    }
}

% Clean Table of Contents styling
\cftsetrmarg{3.5em}
\cftsetpnumwidth{2.5em}
\renewcommand{\cftsecleader}{\cftdotfill{\cftdotsep}}
\renewcommand{\cftsecfont}{\small\normalfont}
\renewcommand{\cftsecpagefont}{\small\bfseries\color{primary}}

\title{\Huge\bfseries GATE EC: Control Systems\\[0.3em] \Large Previous Year Solved Questions Archive}
\author{\textbf{Athena Project Archive}}
\date{\today}

\begin{document}
\maketitle
\tableofcontents
\newpage

"""

def get_clean_topic_and_year(tags):
    year_str = ""
    topic_str = "Control Systems"

    for t in tags:
        t_clean = t.strip()
        if "GATE" in t_clean.upper() or "SET" in t_clean.upper() or any(y in t_clean for y in ["2026","2025","2024","2023","2022","2021","2020","2019","2018","2017","2016","2015","2014","2013","2012","2011","2010","2009","2008","2007","2006","2005","2004","2003","2002","2001"]):
            year_str = t_clean
        else:
            t_lower = t_clean.lower()
            if "block" in t_lower or "sfg" in t_lower or "mason" in t_lower or "basic" in t_lower:
                topic_str = r"Basics, Block Diagrams \& SFGs"
            elif "time" in t_lower or "transient" in t_lower or "steady" in t_lower:
                topic_str = "Time Response Analysis"
            elif "stability" in t_lower or "routh" in t_lower:
                topic_str = r"Stability Analysis \& Routh-Hurwitz"
            elif "root locus" in t_lower:
                topic_str = "Root Locus Technique"
            elif "frequency" in t_lower or "bode" in t_lower or "nyquist" in t_lower or "polar" in t_lower:
                topic_str = "Frequency Response Analysis"
            elif "compensator" in t_lower or "controller" in t_lower or "lead" in t_lower or "lag" in t_lower or "pid" in t_lower:
                topic_str = r"Compensators \& Controllers"
            elif "state" in t_lower or "space" in t_lower or "controllab" in t_lower:
                topic_str = "State Space Analysis"
            else:
                topic_str = t_clean.replace('&', r'\&')

    return topic_str, year_str

def append_raw_questions_step1(questions, output_path):
    print("Step 1: Appending each scraped CS question raw first...")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("% --- RAW SCRAPED CS QUESTIONS (APPENDED FIRST) ---\n\n")
        for idx, q in enumerate(questions, 1):
            f.write(f"% QUESTION {idx}\n")
            f.write(f"% Number: {q['num']}\n")
            f.write(f"% Type: {q['type']} | Marks: {q['marks']}\n")
            f.write(f"% Tags: {', '.join(q['tags'])}\n")
            f.write(f"% Text HTML: {q['text_el']}\n")
            for opt in q['options']:
                f.write(f"% Option {opt['label']} (Correct={opt['is_correct']}): {opt['el']}\n")
            f.write(f"% Explanation HTML: {q['exp_el']}\n\n")
            f.write("-" * 80 + "\n\n")
    print(f"Step 1 complete! Raw CS questions written to {output_path}.")

def format_latex_step2(questions, image_map, output_path):
    print("Step 2: Formatting LaTeX properly for Control Systems...")
    latex_doc = [LATEX_PREAMBLE]

    for idx, q in enumerate(questions, 1):
        q_num_str = f"Question {idx}"
        type_str = q['type'] if q['type'] else "Question"
        marks_str = q['marks'] if q['marks'] else ""

        topic_str, year_str = get_clean_topic_and_year(q['tags'])
        tag_display = f"{topic_str} ({year_str})" if year_str else topic_str
        toc_entry = f"Question {idx}: {topic_str} ({year_str})" if year_str else f"Question {idx}: {topic_str}"

        q_text_latex = clean_html_to_latex(q['text_el'], image_map)
        exp_latex = clean_html_to_latex(q['exp_el'], image_map)

        latex_doc.append(f"\\section*{{{q_num_str}: {tag_display}}}")
        latex_doc.append(f"\\addcontentsline{{toc}}{{section}}{{{toc_entry}}}")
        latex_doc.append(f"\\noindent \\textbf{{\\color{{primary}}{type_str}}} \\hfill \\textbf{{\\color{{secondary}}{marks_str}}}\n\n")
        latex_doc.append(f"\\noindent {q_text_latex}\n\n")

        if q['options']:
            latex_doc.append(r"\begin{enumerate}[label=(\Alph*)]")
            correct_opts = []
            for opt in q['options']:
                opt_latex = clean_html_to_latex(opt['el'], image_map)
                if opt['is_correct']:
                    correct_opts.append(opt['label'])
                    latex_doc.append(f"    \\item \\textbf{{(Correct)}} {opt_latex}")
                else:
                    latex_doc.append(f"    \\item {opt_latex}")
            latex_doc.append(r"\end{enumerate}")
            latex_doc.append(f"\n\\noindent \\textbf{{Correct Answer:}} ({', '.join(correct_opts)})\n")

        if exp_latex:
            latex_doc.append(f"\\begin{{tcolorbox}}[solbox, title=Detailed Solution -- {q_num_str}]")
            latex_doc.append(exp_latex)
            latex_doc.append(r"\end{tcolorbox}")

        latex_doc.append("\n\\vspace{1.5em}\n\\hrule\n\\vspace{1.5em}\n")

    latex_doc.append(r"\end{document}")

    formatted_tex = "\n".join(latex_doc)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(formatted_tex)

    print(f"Step 2 complete! Formatted LaTeX document written to {output_path}.")
