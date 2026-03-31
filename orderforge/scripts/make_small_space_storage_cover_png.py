from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
out = Path('/home/matt/.openclaw/workspace/orderforge/products/small-space-storage-bundle/build/orderforge-small-space-storage-cover.png')
out.parent.mkdir(parents=True, exist_ok=True)
img = Image.new('RGB', (1600, 900), '#f5f5f4')
d = ImageDraw.Draw(img)
d.rounded_rectangle((90, 90, 1510, 810), radius=28, fill='#ffffff', outline='#d6d3d1', width=4)
try:
    big = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 76)
    mid = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 34)
    small = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 28)
    brand = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 40)
except Exception:
    big = mid = small = brand = None
d.text((140,180),'ORDERFORGE',fill='#57534e',font=brand)
d.text((140,300),'Small Space\nStorage Bundle',fill='#111827',font=big,spacing=8)
d.text((140,455),'Printable tools for cramped rooms, drawers, bins, and shelf chaos.',fill='#374151',font=mid)
d.rounded_rectangle((140,530,560,730),radius=18,fill='#f9fafb',outline='#d1d5db',width=3)
d.text((175,565),'Included',fill='#111827',font=mid)
d.text((175,620),'• Drawer labels',fill='#4b5563',font=small)
d.text((175,658),'• Declutter checklists',fill='#4b5563',font=small)
d.text((175,696),'• Shelf and bin planners',fill='#4b5563',font=small)
d.rounded_rectangle((640,530,1460,730),radius=18,fill='#111827')
d.text((690,610),'Make cramped spaces less stupid.',fill='#ffffff',font=mid)
d.text((690,665),'Digital download • Clean • Practical',fill='#d1d5db',font=small)
img.save(out)
print(out)
