import asyncio
import httpx
from bs4 import BeautifulSoup
from src.config import ALL_URLS, HEADERS
from src.downloader import download_image

EMFT_KEYWORDS = [
    "electromagnetics", "basics of electromagnetics", "maxwell",
    "electrostatics", "magnetostatics", "transmission lines", "smith chart",
    "uniform plane waves", "plane waves", "waveguides", "optical fiber",
    "antennas", "radiation", "dipole", "monopole", "poynting"
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

async def fetch_topic_pages(client, base_url):
    page = 1
    questions = []
    while page <= 50:
        url = f'{base_url}?page_no={page}'
        try:
            r = await client.get(url, timeout=10.0)
            if r.status_code == 200:
                soup = BeautifulSoup(r.text, 'html.parser')
                qs = soup.find_all('div', class_='question')
                if not qs:
                    break
                for q in qs:
                    questions.append(parse_question_div(q))
                page += 1
            else:
                break
        except Exception:
            break
    return questions

async def collect_all_questions():
    async with httpx.AsyncClient(headers=HEADERS, follow_redirects=True, timeout=15.0) as client:
        primary_url = 'https://practicepaper.in/gate-ec/electromagnetics'
        all_qs = await fetch_topic_pages(client, primary_url)

        res_other = await asyncio.gather(*[fetch_topic_pages(client, u) for u in ALL_URLS if u != primary_url])
        seen = set([q['text_el'].get_text(strip=True)[:100] for q in all_qs if q['text_el']])

        for page_qs in res_other:
            for q in page_qs:
                if q['text_el']:
                    key = q['text_el'].get_text(strip=True)[:100]
                    if key not in seen:
                        seen.add(key)
                        all_qs.append(q)

        print(f"Total unique Electromagnetics questions collected: {len(all_qs)}")

        image_urls = set()
        for q in all_qs:
            for el in [q['text_el'], q['exp_el']] + [opt['el'] for opt in q['options'] if opt['el']]:
                if el:
                    for img in el.find_all('img'):
                        src = img.get('src', '')
                        if src.startswith('data:image'):
                            src = img.get('data-src') or img.get('data-lazy-src') or ''
                        if src:
                            full_src = "https://practicepaper.in" + src if src.startswith('/') else src
                            image_urls.add(full_src)

        sem = asyncio.Semaphore(25)
        async def dl(url):
            async with sem:
                return url, await download_image(client, url)

        img_results = await asyncio.gather(*[dl(url) for url in image_urls])
        image_map = dict(img_results)

        return all_qs, image_map
