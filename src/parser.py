import asyncio
import httpx
from bs4 import BeautifulSoup
from src.config import ALL_URLS, HEADERS
from src.downloader import download_image

SIGNALS_KEYWORDS = [
    "signals and systems", "basics of signals and systems", "digital filters",
    "dtfs", "dtft", "dft", "fourier series", "fourier transform",
    "frequency response", "correlation", "lti systems", "sampling",
    "laplace transform", "z-transform", "z transform", "laplace"
]

def parse_question_div(q_div):
    q_num_el = q_div.find('div', class_='question_lable')
    q_num = q_num_el.get_text(strip=True) if q_num_el else "Question"

    q_type_els = q_div.find_all('div', class_='question_type_labal')
    q_type = q_type_els[0].get_text(strip=True) if len(q_type_els) > 0 else ""
    q_marks = q_type_els[1].get_text(strip=True).replace('|', '').strip() if len(q_type_els) > 1 else ""

    q_text_div = q_div.find('div', class_='question_text')

    tags_div = q_div.find('div', class_='year_sub_chap_link')
    tags = [a.get_text(strip=True) for a in tags_div.find_all('a')] if tags_div else []

    options = []
    ans_table = q_div.find('table', class_='answer_table')
    if ans_table:
        for tr in ans_table.find_all('tr'):
            is_correct = (tr.get('data-value') == '1')
            lbl_el = tr.find('div', class_='option_index_number')
            data_el = tr.find('div', class_='option_data')
            lbl = lbl_el.get_text(strip=True) if lbl_el else ""
            options.append({
                'label': lbl,
                'is_correct': is_correct,
                'el': data_el
            })

    exp_div = q_div.find('div', class_='mtq_explanation-text')

    return {
        'num': q_num,
        'type': q_type,
        'marks': q_marks,
        'tags': tags,
        'text_el': q_text_div,
        'options': options,
        'exp_el': exp_div
    }

async def fetch_and_parse(client, base_url):
    page = 1
    matched = []
    while True:
        url = f"{base_url}?page_no={page}"
        try:
            r = await client.get(url, follow_redirects=True, timeout=15.0)
            if r.status_code == 200:
                soup = BeautifulSoup(r.text, 'html.parser')
                qs = soup.find_all('div', class_='question')
                if not qs:
                    break
                for q in qs:
                    tags_div = q.find('div', class_='year_sub_chap_link')
                    tag_texts = [a.get_text(strip=True).lower() for a in tags_div.find_all('a')] if tags_div else []
                    tag_hrefs = [a.get('href', '').lower() for a in tags_div.find_all('a')] if tags_div else []

                    is_match = False
                    if any(kw in base_url.lower() for kw in ['signals', 'laplace', 'z-transform', 'fourier', 'sampling', 'dtfs', 'digital-filters']):
                        is_match = True
                    else:
                        for kw in SIGNALS_KEYWORDS:
                            if any(kw in t for t in tag_texts) or any(kw in h for h in tag_hrefs):
                                is_match = True
                                break

                    if is_match:
                        parsed = parse_question_div(q)
                        matched.append(parsed)
                page += 1
            else:
                break
        except Exception as e:
            print(f"Error crawling {url}: {e}")
            break
    return base_url, matched

async def collect_all_questions():
    async with httpx.AsyncClient(headers=HEADERS, timeout=20.0) as client:
        print(f"Scraping signals questions across {len(ALL_URLS)} candidate URLs with pagination...")
        all_unique = []
        seen_keys = set()
        chunk_size = 5

        for i in range(0, len(ALL_URLS), chunk_size):
            chunk = ALL_URLS[i:i+chunk_size]
            results = await asyncio.gather(*[fetch_and_parse(client, u) for u in chunk])
            for u, questions in results:
                for q in questions:
                    if q['text_el']:
                        key = q['text_el'].get_text(strip=True)[:100]
                        if key not in seen_keys:
                            seen_keys.add(key)
                            all_unique.append(q)

        print(f"Total unique Signals and Systems questions collected: {len(all_unique)}")

        image_map = {}
        for q in all_unique:
            for el in [q['text_el'], q['exp_el']] + [opt['el'] for opt in q['options'] if opt['el']]:
                if el:
                    for img in el.find_all('img'):
                        src = img.get('src', '')
                        if src.startswith('data:image'):
                            src = img.get('data-src') or img.get('data-lazy-src') or ''
                        if src:
                            filename = await download_image(client, src)
                            full_src = "https://practicepaper.in" + src if src.startswith('/') else src
                            image_map[full_src] = filename
                            image_map[src] = filename

        return all_unique, image_map

