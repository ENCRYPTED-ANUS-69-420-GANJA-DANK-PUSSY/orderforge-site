from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

out = Path('/home/matt/.openclaw/workspace/orderforge/products/workshop-starter-pack/build/orderforge-workshop-starter-cover.png')
out.parent.mkdir(parents=True, exist_ok=True)
img = Image.new('RGB', (1600, 900), '#f5f5f4')
d = ImageDraw.Draw(img)
d.rounded_rectangle((90, 90, 1510, 810), radius=28, fill='#ffffff', outline='#d6d3d1', width=4)
try:
    font_big = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 78)
    font_mid = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 34)
    font_small = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 28)
    font_brand = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 40)
except Exception:
    font_big = font_mid = font_small = font_brand = None

d.text((140, 180), 'ORDERFORGE', fill='#57534e', font=font_brand)
d.text((140, 300), 'Workshop Starter Pack', fill='#111827', font=font_big)
d.text((140, 410), 'Printable tools for garages, benches, hardware bins, and workshop cleanup.', fill='#374151', font=font_mid)
d.rounded_rectangle((140, 500, 560, 700), radius=18, fill='#f9fafb', outline='#d1d5db', width=3)
d.text((175, 535), 'Included', fill='#111827', font=font_mid)
d.text((175, 590), '• Tool inventory', fill='#4b5563', font=font_small)
d.text((175, 628), '• Bin labels', fill='#4b5563', font=font_small)
d.text((175, 666), '• Pegboard planner', fill='#4b5563', font=font_small)
d.rounded_rectangle((640, 500, 1460, 700), radius=18, fill='#111827')
d.text((690, 585), 'Stop losing tools to workshop entropy.', fill='#ffffff', font=font_mid)
d.text((690, 640), 'Digital download • Clean, practical, printable', fill='#d1d5db', font=font_small)
img.save(out)
print(out)
