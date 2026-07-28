import re
from bs4 import BeautifulSoup

def balance_delimiters(code):
    # Check count of \left vs \right
    left_matches = re.findall(r'\\left[\(\[\{\.]', code)
    right_matches = re.findall(r'\\right[\)\]\}\.]', code)

    if len(left_matches) != len(right_matches):
        # Strip \left and \right prefixes to prevent unmatched delimiter fatal errors
        code = re.sub(r'\\left\s*([\(\[\{\.])', r'\1', code)
        code = re.sub(r'\\right\s*([\)\}\]\.])', r'\1', code)
        code = code.replace('\\left', '').replace('\\right', '')
    return code

def fix_latex_glitches(text):
    text = re.sub(r'\[\/?latex\]', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\\xLeftrightarrow\s*\\text\s*\{([^\}]*)\}', r'\\iff\\text{\1}', text)
    text = text.replace('\\xLeftrightarrow', '\\iff ')
    text = text.replace('\\xRightarrow', '\\implies ')
    text = text.replace('\\xrightarrow', '\\to ')
    text = text.replace('\\<', '<').replace('\\>', '>')

    # Fix Control Systems common math notations
    text = text.replace('w_n', '\\omega_n').replace('omega_n', '\\omega_n')
    text = text.replace('w_c', '\\omega_c').replace('omega_c', '\\omega_c')
    text = text.replace('w_p', '\\omega_p').replace('omega_p', '\\omega_p')
    text = text.replace('zeta', '\\zeta')

    # Fix 4p -> 4\pi
    text = re.sub(r'(?<=\d)p(?=\s*\\times|\s*\*|\s*t|\s*\\cdot)', r'\\pi', text)

    # Fix $cos^{2}$(4\pi ... t) -> $\cos^{2}(4\pi ... t)$
    text = re.sub(r'\$cos\^\{2\}\$\((.*?)\)', r'$\\cos^{2}(\1)$', text)
    text = re.sub(r'\$cos\^2\$\((.*?)\)', r'$\\cos^{2}(\1)$', text)
    text = re.sub(r'\$sin\^\{2\}\$\((.*?)\)', r'$\\sin^{2}(\1)$', text)
    text = re.sub(r'\$sin\^2\$\((.*?)\)', r'$\\sin^{2}(\1)$', text)

    # Fix 1$10^{3}$t or similar broken powers
    text = re.sub(r'1\$10\^\{(\d+)\}\$', r'10^{\1}', text)
    text = re.sub(r'(\d+)\$(\d+)\^\{(\d+)\}\$', r'\1 \\cdot 10^{\3}', text)

    # Fix missing closing brace in \text{...= or P_{\text{...=
    text = re.sub(r'([A-Za-z0-9_]+)_\{\\text\{([A-Za-z0-9]+)\s*([=+\-\*\\\/])', r'\1_{\\text{\2}} \3', text)
    text = re.sub(r'\\text\{([A-Za-z0-9]+)\s*([=+\-\*\\\/])', r'\\text{\1} \2', text)

    # Fix broken \left.{\right.} patterns
    text = text.replace('\\left.{', '{').replace('\\right.}', '}')
    text = re.sub(r'\\right\\(?!\w)', r'\\right.', text)
    text = re.sub(r'\\left\\(?!\w)', r'\\left.', text)

    # Fix unclosed \boxed{...
    text = re.sub(r'\\boxed\{([^{}\n]*?)(?=\\]|\n|\$)', r'\\boxed{\1}', text)

    # Fix double/extra closing braces in \text{...}}
    text = re.sub(r'(\\text\{[^\}]*)\}\}', r'\1}', text)
    text = re.sub(r'\\text\{([^}]*)\}\s*\$', r'\\text{\1}$', text)
    text = re.sub(r'\\text\{([^}]*)\$\}', r'\\text{\1}', text)

    # Fix double backslash before ampersand
    text = text.replace('\\\\&', '\\&')

    text = balance_delimiters(text)
    return text

def clean_html_to_latex(html_element, image_map):
    if not html_element:
        return ""

    soup = BeautifulSoup(str(html_element), 'html.parser')

    for img in soup.find_all('img'):
        raw_src = img.get('src')
        src = str(raw_src[0] if isinstance(raw_src, list) else (raw_src or ''))
        if src.startswith('data:image'):
            raw_lazy = img.get('data-src') or img.get('data-lazy-src')
            src = str(raw_lazy[0] if isinstance(raw_lazy, list) else (raw_lazy or ''))
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

        # Balance unclosed { in math block
        open_braces = code.count('{')
        close_braces = code.count('}')
        if open_braces > close_braces:
            code += '}' * (open_braces - close_braces)
        elif close_braces > open_braces:
            diff = close_braces - open_braces
            for _ in range(diff):
                if code.endswith('}'):
                    code = code[:-1].rstrip()

        code = balance_delimiters(code)

        multiline = ('\n' in code) or ('\\begin{' in code) or ('\\int' in code and '\\limits' in code) or (len(code) > 80)

        if has_env or needs_aligned or multiline:
            fmt = f"\n\\[\n{code}\n\\]\n"
        else:
            fmt = f"${code}$"

        latex_blocks.append(fmt)
        return f"QQQLLATEXBLOCK{len(latex_blocks)-1}QQQ"

    processed = re.sub(r'\[latex\](.*?)\[/latex\]', replace_latex, html_str, flags=re.DOTALL | re.IGNORECASE)

    soup2 = BeautifulSoup(processed, 'html.parser')
    text = soup2.get_text()

    # Convert fill-in-the-blank underscores (e.g. ______) to \underline{\hspace{1.5cm}}
    text = re.sub(r'_{2,}', r'\\underline{\\hspace{1.5cm}}', text)

    # Escape remaining single underscores outside LATEX_BLOCK placeholders
    parts = re.split(r'(QQQLLATEXBLOCK\d+QQQ)', text)
    greek_symbols = [
        r'\\zeta', r'\\omega', r'\\theta', r'\\phi', r'\\pi', r'\\alpha', r'\\beta',
        r'\\gamma', r'\\sigma', r'\\lambda', r'\\delta', r'\\Omega', r'\\times'
    ]
    greek_pattern = re.compile(r'(' + '|'.join(greek_symbols) + r')\b')

    for idx in range(0, len(parts), 2):
        p_txt = parts[idx]
        p_txt = p_txt.replace('_', '\\_')
        p_txt = p_txt.replace('&', '\\&')
        p_txt = p_txt.replace('\\\\&', '\\&')
        p_txt = greek_pattern.sub(r'$\1$', p_txt)
        p_txt = re.sub(r'(\d+)\^\{\\circ\}', r'$\1^{\\circ}$', p_txt)
        p_txt = re.sub(r'(\d+)\^\\circ', r'$\1^{\\circ}$', p_txt)
        parts[idx] = p_txt
    text = "".join(parts)

    for idx, block in enumerate(latex_blocks):
        text = text.replace(f"QQQLLATEXBLOCK{idx}QQQ", block)

    text = fix_latex_glitches(text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()
