from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

out = Path('/home/matt/.openclaw/workspace/orderforge/products/custom-cleaner-starter-kit/orderforge-custom-cleaner-cover.png')
out.parent.mkdir(parents=True, exist_ok=True)
img = Image.new('RGB', (1600, 900), '#f5f5f4')
d = ImageDraw.Draw(img)
d.rounded_rectangle((90, 90, 1510, 810), radius=28, fill='#ffffff', outline='#d6d3d1', width=4)
try:
    font_big = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 74)
    font_mid = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 34)
    font_small = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 28)
    font_brand = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 40)
except Exception:
    font_big = font_mid = font_small = font_brand = None

d.text((140, 180), 'ORDERFORGE', fill='#57534e', font=font_brand)
d.text((140, 290), 'Custom Cleaner\nStarter Kit', fill='#111827', font=font_big, spacing=8)
d.text((140, 455), 'Done-for-you customization for solo cleaners and small cleaning businesses.', fill='#374151', font=font_mid)
d.rounded_rectangle((140, 530, 560, 730), radius=18, fill='#f9fafb', outline='#d1d5db', width=3)
d.text((175, 565), 'Includes', fill='#111827', font=font_mid)
d.text((175, 620), '• Flyer customized', fill='#4b5563', font=font_small)
d.text((175, 658), '• Quote + invoice edited', fill='#4b5563', font=font_small)
d.text((175, 696), '• QR / contact details added', fill='#4b5563', font=font_small)
d.rounded_rectangle((640, 530, 1460, 730), radius=18, fill='#111827')
d.text((690, 605), '24-hour done-for-you add-on.', fill='#ffffff', font=font_mid)
d.text((690, 660), 'Fast, clean, practical — not fake agency theatre.', fill='#d1d5db', font=font_small)
img.save(out)
print(out)
