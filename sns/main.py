import asyncio
import os
import sys
import subprocess

MODULE_DIR = os.path.dirname(os.path.abspath(__file__))
if MODULE_DIR not in sys.path:
    sys.path.insert(0, MODULE_DIR)

from src.config import OUTPUT_TEX, IMAGES_DIR, BASE_DIR
from src.parser import collect_all_questions
from src.formatter import append_raw_questions_step1, format_latex_step2

async def run_pipeline():
    os.makedirs(IMAGES_DIR, exist_ok=True)

    print("Step 1 & 2: Scraping all questions and downloading images...")
    questions, image_map = await collect_all_questions()

    raw_output_path = os.path.join(BASE_DIR, "raw_questions.txt")
    append_raw_questions_step1(questions, raw_output_path)

    print("Step 3: Formatting LaTeX document...")
    format_latex_step2(questions, image_map, OUTPUT_TEX)

    print("Step 4: Compiling PDF with pdflatex...")
    try:
        cmd = ["/Library/TeX/texbin/pdflatex", "-interaction=nonstopmode", "sns-pyq.tex"]
        res = subprocess.run(cmd, cwd=BASE_DIR, capture_output=True, text=True)
        if res.returncode == 0:
            print("PDF compiled successfully! Output: sns-pyq.pdf")
        else:
            print("pdflatex completed with warnings/errors. Running second pass...")
            subprocess.run(cmd, cwd=BASE_DIR, capture_output=True, text=True)
            print("Second pass complete.")
    except Exception as e:
        print(f"Error running pdflatex: {e}")

def main():
    asyncio.run(run_pipeline())

if __name__ == "__main__":
    main()
