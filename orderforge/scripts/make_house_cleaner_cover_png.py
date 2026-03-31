from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

out = Path('/home/matt/.openclaw/workspace/orderforge/products/house-cleaner-starter-pack/build/orderforge-house-cleaner-cover.png')
out.parent.mkdir(parents=True, exist_ok=True)
img = Image.new('RGB', (1600, 900), '#f5f5f4')
d = ImageDraw.Draw(img)
d.rounded_rectangle((90, 90, 1510, 810), radius=28, fill='#ffffff', outline='#d6d3d1', width=4)
try:
    font_big = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 76)
    font_mid = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 34)
    font_small = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 28)
    font_brand = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 40)
except Exception:
    font_big = font_mid = font_small = font_brand = None

d.text((140, 180), 'ORDERFORGE', fill='#57534e', font=font_brand)
d.text((140, 295), 'House Cleaner\nStarter Pack', fill='#111827', font=font_big, spacing=10)
d.text((140, 455), 'Templates, scripts, and printable tools for small cleaning businesses.', fill='#374151', font=font_mid)
d.rounded_rectangle((140, 530, 560, 730), radius=18, fill='#f9fafb', outline='#d1d5db', width=3)
d.text((175, 565), 'Includes', fill='#111827', font=font_mid)
d.text((175, 620), '• Quotes + invoices', fill='#4b5563', font=font_small)
d.text((175, 658), '• Review scripts', fill='#4b5563', font=font_small)
d.text((175, 696), '• Flyer + referral copy', fill='#4b5563', font=font_small)
d.rounded_rectangle((640, 530, 1460, 730), radius=18, fill='#111827')
d.text((690, 610), 'Built for operators, not AI slop merchants.', fill='#ffffff', font=font_mid)
d.text((690, 665), 'Digital download • Practical • Fast to use', fill='#d1d5db', font=font_small)
img.save(out)
print(out)
