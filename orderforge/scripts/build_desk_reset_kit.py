from pathlib import Path
from html import escape

root = Path('/home/matt/.openclaw/workspace/orderforge/products/desk-reset-kit')
out = root / 'build'
out.mkdir(parents=True, exist_ok=True)

style = '''
body { font-family: Arial, Helvetica, sans-serif; color: #1a1a1a; max-width: 900px; margin: 40px auto; padding: 0 24px; }
h1, h2, h3 { color: #111827; }
.page { page-break-after: always; margin-bottom: 48px; }
.muted { color: #6b7280; }
.box { border: 1px solid #d1d5db; border-radius: 8px; padding: 14px; margin: 12px 0; }
.line { border-bottom: 1px solid #d1d5db; height: 28px; margin: 8px 0; }
.grid { display: grid; grid-template-columns: 1fr 1fr; gap: 18px; }
.small { font-size: 14px; }
ul { line-height: 1.7; }
footer { margin-top: 24px; font-size: 12px; color: #6b7280; }
'''

pages = [
    ('desk-layout-planner.html', 'Desk Layout Planner', '''<p class="muted">Map your setup before you reorganize it.</p>
<div class="grid">
<div class="box"><h3>Zones</h3><ul><li>Main work zone</li><li>Cable zone</li><li>Charging zone</li><li>Storage zone</li><li>Quick-access zone</li></ul></div>
<div class="box"><h3>Current Problems</h3><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div></div>
</div>
<div class="box"><h3>New Layout Plan</h3><p>Monitor position</p><div class="line"></div><p>Keyboard / mouse</p><div class="line"></div><p>Charging area</p><div class="line"></div><p>Cable route</p><div class="line"></div><p>Storage placement</p><div class="line"></div></div>
<div class="box"><h3>Notes</h3><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div></div>'''),
    ('cable-label-sheet.html', 'Cable Label Sheet', '''<p class="muted">Label your setup so future-you suffers less.</p>
<div class="box"><h3>Suggested labels</h3><ul><li>Monitor</li><li>Laptop charger</li><li>Phone charger</li><li>USB hub</li><li>Audio interface</li><li>Headphones</li><li>Microphone</li><li>Lighting</li><li>Printer</li><li>Misc 1</li><li>Misc 2</li><li>Misc 3</li></ul></div>
<div class="box"><h3>Cable cleanup notes</h3><p>Remove</p><div class="line"></div><p>Bundle</p><div class="line"></div><p>Reroute</p><div class="line"></div><p>Replace</p><div class="line"></div></div>'''),
    ('device-inventory-sheet.html', 'Device Inventory Sheet', '''<p class="muted">Track what actually lives on your desk.</p>
<div class="box"><h3>Inventory</h3><p class="small">Item / Purpose / Power needed / Keep-Move-Remove</p><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div></div>'''),
    ('workspace-reset-checklist.html', 'Workspace Reset Checklist', '''<div class="grid"><div class="box"><h3>Daily reset</h3><ul><li>Put loose items back</li><li>Return accessories to their zones</li><li>Clear trash and dishes</li><li>Tidy stray cables</li><li>Put chargers back in place</li><li>Wipe key surfaces</li></ul></div><div class="box"><h3>Weekly reset</h3><ul><li>Review what is piling up</li><li>Remove items that do not belong</li><li>Re-label confusing storage</li><li>Re-route problem cables</li><li>Check charging clutter</li><li>Clean dust from main surfaces</li></ul></div></div>'''),
    ('drawer-category-planner.html', 'Drawer Category Planner', '''<div class="box"><h3>Drawer 1</h3><p>Purpose</p><div class="line"></div><p>Contents</p><div class="line"></div><p>Items to remove</p><div class="line"></div><p>Better categories</p><div class="line"></div></div><div class="box"><h3>Drawer 2</h3><p>Purpose</p><div class="line"></div><p>Contents</p><div class="line"></div><p>Items to remove</p><div class="line"></div><p>Better categories</p><div class="line"></div></div><div class="box"><h3>Drawer 3</h3><p>Purpose</p><div class="line"></div><p>Contents</p><div class="line"></div><p>Items to remove</p><div class="line"></div><p>Better categories</p><div class="line"></div></div>'''),
    ('daily-weekly-reset-sheet.html', 'Daily + Weekly Reset Sheet', '''<div class="grid"><div class="box"><h3>Daily</h3><ul><li>Clear surface</li><li>Put accessories back</li><li>Tidy visible cables</li><li>Empty clutter tray</li><li>Prep tomorrow\'s essentials</li></ul></div><div class="box"><h3>Weekly</h3><ul><li>Review storage pain points</li><li>Remove non-essential items</li><li>Clean under monitor and desk edges</li><li>Refresh labels if needed</li><li>Note accessories worth replacing with better holders or mounts</li></ul></div></div>'''),
]

for filename, title, body in pages:
    html = f'''<!doctype html><html><head><meta charset="utf-8"><title>{escape(title)}</title><style>{style}</style></head><body><div class="page"><h1>{escape(title)}</h1>{body}<footer>Orderforge · Desk Reset Kit</footer></div></body></html>'''
    (out / filename).write_text(html, encoding='utf-8')

combined = ['<!doctype html><html><head><meta charset="utf-8"><title>Orderforge Desk Reset Kit</title><style>'+style+'</style></head><body>']
combined.append('<div class="page"><h1>Orderforge Desk Reset Kit</h1><p class="muted">A practical printable toolkit for organizing desks, cables, drawers, and everyday workspace clutter.</p><div class="box"><h3>Included</h3><ul><li>Desk Layout Planner</li><li>Cable Label Sheet</li><li>Device Inventory Sheet</li><li>Workspace Reset Checklist</li><li>Drawer Category Planner</li><li>Daily + Weekly Reset Sheet</li></ul></div><footer>Orderforge</footer></div>')
for _, title, body in pages:
    combined.append(f'<div class="page"><h1>{escape(title)}</h1>{body}<footer>Orderforge · Desk Reset Kit</footer></div>')
combined.append('</body></html>')
(out / 'Orderforge-Desk-Reset-Kit.html').write_text(''.join(combined), encoding='utf-8')

(out / 'README.txt').write_text('Orderforge Desk Reset Kit\n\nOpen the combined HTML file in any browser and print the pages you want. Individual printable sheets are included in this folder as separate HTML files.\n', encoding='utf-8')

cover = '''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900"><rect width="1600" height="900" fill="#f5f5f4"/><rect x="90" y="90" width="1420" height="720" rx="28" fill="#ffffff" stroke="#d6d3d1" stroke-width="4"/><text x="140" y="210" font-family="Arial, Helvetica, sans-serif" font-size="42" fill="#57534e">ORDERFORGE</text><text x="140" y="330" font-family="Arial, Helvetica, sans-serif" font-size="88" font-weight="700" fill="#111827">Desk Reset Kit</text><text x="140" y="410" font-family="Arial, Helvetica, sans-serif" font-size="34" fill="#374151">Printable tools for desks, cables, drawers, and workspace cleanup.</text><rect x="140" y="500" width="420" height="170" rx="20" fill="#f9fafb" stroke="#d1d5db"/><text x="175" y="560" font-family="Arial, Helvetica, sans-serif" font-size="30" fill="#111827">Included</text><text x="175" y="610" font-family="Arial, Helvetica, sans-serif" font-size="26" fill="#4b5563">• Layout planner</text><text x="175" y="648" font-family="Arial, Helvetica, sans-serif" font-size="26" fill="#4b5563">• Cable labels</text><text x="175" y="686" font-family="Arial, Helvetica, sans-serif" font-size="26" fill="#4b5563">• Reset checklists</text><rect x="640" y="500" width="820" height="170" rx="20" fill="#111827"/><text x="690" y="585" font-family="Arial, Helvetica, sans-serif" font-size="34" fill="#ffffff">Make clutter less stupid.</text><text x="690" y="635" font-family="Arial, Helvetica, sans-serif" font-size="24" fill="#d1d5db">Digital download • Clean, practical, printable</text></svg>'''
(out / 'cover.svg').write_text(cover, encoding='utf-8')
print('built', out)
