import os
from PIL import Image
from src.config import IMAGES_DIR

_image_cache = {}
_img_counter = 0

async def download_image(client, img_url):
    global _img_counter
    if not img_url or img_url.startswith('data:image'):
        return None

    full_url = "https://practicepaper.in" + img_url if img_url.startswith('/') else img_url

    if full_url in _image_cache:
        return _image_cache[full_url]

    try:
        r = await client.get(full_url, follow_redirects=True)
        if r.status_code == 200:
            _img_counter += 1
            ext = ".png"
            if ".jpg" in full_url.lower() or ".jpeg" in full_url.lower():
                ext = ".jpg"
            elif ".webp" in full_url.lower():
                ext = ".webp"

            filename = f"img_{_img_counter}{ext}"
            filepath = os.path.join(IMAGES_DIR, filename)

            with open(filepath, "wb") as f:
                f.write(r.content)

            if ext == ".webp":
                try:
                    im = Image.open(filepath)
                    png_filename = f"img_{_img_counter}.png"
                    png_filepath = os.path.join(IMAGES_DIR, png_filename)
                    im.save(png_filepath, "PNG")
                    filename = png_filename
                except Exception as e:
                    print(f"WebP conversion notice for {filename}: {e}")

            _image_cache[full_url] = filename
            return filename
    except Exception as e:
        print(f"Error downloading image {full_url}: {e}")
    return None
