import re
from bs4 import BeautifulSoup

def fix_latex_glitches(text):
    text = re.sub(r'\[\/?latex\]', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\\xLeftrightarrow\s*\\text\s*\{([^\}]*)\}', r'\\iff\\text{\1}', text)
    text = text.replace('\\xLeftrightarrow', '\\iff ')
    text = text.replace('\\xRightarrow', '\\implies ')
    text = text.replace('\\xrightarrow', '\\to ')
    text = text.replace('\\<', '<').replace('\\>', '>')

    # Fix 4p -> 4\pi
    text = re.sub(r'(?<=\d)p(?=\s*\\times|\s*\*|\s*t|\s*\\cdot)', r'\\pi', text)

    # Fix $cos^{2}$(4\pi ... t) -> $\cos^{2}(4\pi ... t)$
    text = re.sub(r'\$cos\^\{2\}\$\((.*?)\)', r'$\\cos^{2}(\1)$', text)
    text = re.sub(r'\$cos\^2\$\((.*?)\)', r'$\\cos^{2}(\1)$', text)

    # Fix 1$10^{3}$t or similar broken powers
    text = re.sub(r'1\$10\^\{(\d+)\}\$', r'10^{\1}', text)
    text = re.sub(r'(\d+)\$(\d+)\^\{(\d+)\}\$', r'\1 \\cdot 10^{\3}', text)

    # Fix specific subscript and fraction syntax glitches for R_HP and R_LP
    text = re.sub(r'\\frac\{1\}\{2\\pi R_\{\\text\s*\{HP\}C_\{\\text\s*\{HP\}\s*=', r'\\frac{1}{2\\pi R_{\\text{HP}}C_{\\text{HP}}} =', text)
    text = re.sub(r'\\frac\{1\}\{2\\pi R_\{\\text\s*\{LP\}C_\{\\text\s*\{LP\}\s*=', r'\\frac{1}{2\\pi R_{\\text{LP}}C_{\\text{LP}}} =', text)
    text = re.sub(r'R_\{\\text\s*\{HP\}\s*C_\{\\text\s*\{HP\}?', r'R_{\\text{HP}}C_{\\text{HP}}', text)
    text = re.sub(r'R_\{\\text\s*\{LP\}\s*C_\{\\text\s*\{LP\}?', r'R_{\\text{LP}}C_{\\text{LP}}', text)

    # Fix double closing braces in \text{...}}
    text = re.sub(r'(\\text\{[^\}]*)\}\}', r'\1}', text)
    text = re.sub(r'\\text\{([^}]*)\}\s*\$', r'\\text{\1}$', text)
    text = re.sub(r'\\text\{([^}]*)\$\}', r'\\text{\1}', text)

    return text

def clean_html_to_latex(html_element, image_map):
    if not html_element:
        return ""

    soup = BeautifulSoup(str(html_element), 'html.parser')

    for img in soup.find_all('img'):
        src = img.get('src', '')
        if src.startswith('data:image'):
            src = img.get('data-src') or img.get('data-lazy-src') or ''
        if src.startswith('/'):
            src = "https://practicepaper.in" + src
        if src in image_map and image_map[src]:
            img_file = image_map[src]
            img.replace_with(f"\n\\begin{{center}}\\includegraphics[max width=0.85\\linewidth]{{images/{img_file}}}\\end{{center}}\n")
        else:
            img.decompose()

    for b in soup.find_all(['b', 'strong']):
        b_txt = b.get_text()
        b.replace_with(f"\\textbf{{{b_txt}}}")
    for i in soup.find_all(['i', 'em']):
        i_txt = i.get_text()
        i.replace_with(f"\\textit{{{i_txt}}}")
    for br in soup.find_all('br'):
        br.replace_with("\n")
    for p in soup.find_all('p'):
        p.replace_with(f"\n{p.get_text()}\n")

    html_str = str(soup)

    # Pre-clean html string math tags
    html_str = re.sub(r'(\d+)\$(\d+)\^\{(\d+)\}\$', r'\1 \\cdot 10^{\3}', html_str)

    latex_blocks = []

    def replace_latex(m):
        code = m.group(1).strip()
        if code.startswith('\\[') and code.endswith('\\]'):
            code = code[2:-2].strip()

        code = code.replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&').replace('&nbsp;', ' ')
        code = code.replace('\\lt', '<').replace('\\gt', '>').replace('\\<', '<').replace('\\>', '>')
        code = fix_latex_glitches(code)

        has_env = any(env in code for env in ['aligned', 'array', 'matrix', 'cases', 'split', 'pmatrix', 'bmatrix', 'tabular'])
        needs_aligned = ('&' in code or '\\\\' in code) and not has_env

        if needs_aligned:
            code = f"\\begin{{aligned}}\n{code}\n\\end{{aligned}}"

        multiline = ('\n' in code) or ('\\begin{' in code) or ('\\int' in code and '\\limits' in code) or (len(code) > 80)

        if has_env or needs_aligned or multiline:
            fmt = f"\n\\[\n{code}\n\\]\n"
        else:
            fmt = f"${code}$"

        latex_blocks.append(fmt)
        return f"___LATEX_BLOCK_{len(latex_blocks)-1}___"

    processed = re.sub(r'\[latex\](.*?)\[/latex\]', replace_latex, html_str, flags=re.DOTALL | re.IGNORECASE)

    soup2 = BeautifulSoup(processed, 'html.parser')
    text = soup2.get_text()

    for idx, blk in enumerate(latex_blocks):
        text = text.replace(f"___LATEX_BLOCK_{idx}___", blk)

    # Global cleanup on final text
    text = fix_latex_glitches(text)
    text = re.sub(r'\\textbf([A-Za-z0-9]+)', r'\\textbf{\1}', text)
    text = re.sub(r'\\mathbf([A-Za-z0-9]+)', r'\\mathbf{\1}', text)

    parts = re.split(r'(\$.*?\$|\\\[.*?\\\]|\\begin\{.*?\}.*?\\end\{.*?\})', text, flags=re.DOTALL)
    new_parts = []
    for p in parts:
        if p.startswith('$') or p.startswith('\\[') or p.startswith('\\begin'):
            new_parts.append(p)
        else:
            p_esc = p.replace('%', '\\%').replace('#', '\\#')
            p_esc = re.sub(r'(?<!\\)_', '\\_', p_esc)
            p_esc = p_esc.replace('\\\\&', '\\\\ \\&')
            p_esc = re.sub(r'(?<!\\)&', '\\&', p_esc)
            p_esc = p_esc.replace('\\therefore', '$\\therefore$')
            p_esc = re.sub(r'(\\frac\{[^\}]*\}\{[^\}]*\})', r'$\1$', p_esc)
            new_parts.append(p_esc)

    text = "".join(new_parts)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()
