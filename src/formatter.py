from src.converter import clean_html_to_latex

LATEX_PREAMBLE = r"""\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[margin=0.75in]{geometry}
\usepackage{amsmath,amssymb,amsfonts,mathtools,extarrows}
\usepackage{graphicx}
\usepackage[export]{adjustbox}
\usepackage{tcolorbox}
\usepackage{enumitem}
\usepackage{xcolor}
\usepackage{hyperref}
\usepackage{booktabs}
\usepackage{array}

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

\title{\Huge\bfseries GATE EC: Signals and Systems\\[0.3em] \Large Previous Year Solved Questions}
\author{\textbf{PracticePaper.in Archive}}
\date{\today}

\begin{document}
\maketitle
\tableofcontents
\newpage

"""

def append_raw_questions_step1(questions, output_path):
    print("Step 1: Appending each scraped question raw first...")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("% --- RAW SCRAPED QUESTIONS (APPENDED FIRST) ---\n\n")
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
    print(f"Step 1 complete! Raw questions written to {output_path}.")

def format_latex_step2(questions, image_map, output_path):
    print("Step 2: Formatting LaTeX properly...")
    latex_doc = [LATEX_PREAMBLE]

    for idx, q in enumerate(questions, 1):
        q_num_str = f"Question {idx}"
        type_str = q['type'] if q['type'] else "Question"
        marks_str = q['marks'] if q['marks'] else ""
        tags_str = ", ".join(q['tags']) if q['tags'] else "Signals and Systems"

        q_text_latex = clean_html_to_latex(q['text_el'], image_map)
        exp_latex = clean_html_to_latex(q['exp_el'], image_map)

        latex_doc.append(f"\\section*{{{q_num_str}: {tags_str}}}")
        latex_doc.append(f"\\addcontentsline{{toc}}{{section}}{{{q_num_str} -- {tags_str}}}")
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
