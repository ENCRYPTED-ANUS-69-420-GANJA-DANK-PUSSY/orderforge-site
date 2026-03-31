from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

out = Path('/home/matt/.openclaw/workspace/orderforge/products/desk-reset-kit/build/orderforge-desk-reset-cover.png')
out.parent.mkdir(parents=True, exist_ok=True)
img = Image.new('RGB', (1600, 900), '#f5f5f4')
d = ImageDraw.Draw(img)

d.rounded_rectangle((90, 90, 1510, 810), radius=28, fill='#ffffff', outline='#d6d3d1', width=4)
d.text((140, 160), 'ORDERFORGE', fill='#57534e', font=ImageFont.load_default(size=32) if hasattr(ImageFont, 'load_default') else None)
# fallback sizing handled by default font; use basic layout blocks too
try:
    font_big = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 82)
    font_mid = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 34)
    font_small = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 28)
    font_brand = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 40)
except Exception:
    font_big = font_mid = font_small = font_brand = None

d.text((140, 180), 'ORDERFORGE', fill='#57534e', font=font_brand)
d.text((140, 300), 'Desk Reset Kit', fill='#111827', font=font_big)
d.text((140, 410), 'Printable tools for desks, cables, drawers, and workspace cleanup.', fill='#374151', font=font_mid)

d.rounded_rectangle((140, 500, 560, 690), radius=18, fill='#f9fafb', outline='#d1d5db', width=3)
d.text((175, 535), 'Included', fill='#111827', font=font_mid)
d.text((175, 590), '• Layout planner', fill='#4b5563', font=font_small)
d.text((175, 628), '• Cable labels', fill='#4b5563', font=font_small)
d.text((175, 666), '• Reset checklists', fill='#4b5563', font=font_small)

d.rounded_rectangle((640, 500, 1460, 690), radius=18, fill='#111827')
d.text((690, 575), 'Make clutter less stupid.', fill='#ffffff', font=font_mid)
d.text((690, 630), 'Digital download • Clean, practical, printable', fill='#d1d5db', font=font_small)

img.save(out)
print(out)
