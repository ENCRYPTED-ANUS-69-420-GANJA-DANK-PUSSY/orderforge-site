from pathlib import Path
from html import escape

root = Path('/home/matt/.openclaw/workspace/orderforge/products/small-space-storage-bundle')
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
    ('room-zone-planner.html', 'Room Zone Planner', '''<p class="muted">Break a cramped room into usable zones before everything becomes one giant junk drawer.</p><div class="grid"><div class="box"><h3>Zone 1</h3><div class="line"></div><div class="line"></div><div class="line"></div></div><div class="box"><h3>Zone 2</h3><div class="line"></div><div class="line"></div><div class="line"></div></div></div><div class="grid"><div class="box"><h3>Zone 3</h3><div class="line"></div><div class="line"></div><div class="line"></div></div><div class="box"><h3>Zone 4</h3><div class="line"></div><div class="line"></div><div class="line"></div></div></div>'''),
    ('drawer-labels.html', 'Drawer Labels', '''<p class="muted">Simple labels for drawers, bins, and shelves.</p><div class="box"><ul><li>Daily Use</li><li>Bathroom</li><li>Kitchen Tools</li><li>Cables</li><li>Chargers</li><li>Paperwork</li><li>Cleaning</li><li>Seasonal</li><li>Spare Parts</li><li>Misc</li></ul></div><div class="box"><h3>Custom labels</h3><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div></div>'''),
    ('declutter-checklist.html', 'Declutter Checklist', '''<div class="box"><h3>Questions to ask</h3><ul><li>Do I use this weekly?</li><li>Does this have a clear home?</li><li>Would I buy it again?</li><li>Can it be stored vertically or elsewhere?</li><li>Is it just taking up visible space?</li></ul></div><div class="box"><h3>Remove / donate / relocate</h3><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div></div>'''),
    ('bin-inventory-sheet.html', 'Bin Inventory Sheet', '''<p class="muted">Track what is actually inside bins and boxes so you stop opening six containers to find one cable.</p><div class="box"><p class="small">Bin / Shelf / Contents / Frequency of use / Move?</p><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div></div>'''),
    ('small-space-reset-sheet.html', 'Small Space Reset Sheet', '''<div class="grid"><div class="box"><h3>Daily reset</h3><ul><li>Clear flat surfaces</li><li>Put loose items back</li><li>Empty visible clutter basket</li><li>Reset charging area</li></ul></div><div class="box"><h3>Weekly reset</h3><ul><li>Recheck crowded zones</li><li>Rotate low-use items out</li><li>Relabel anything confusing</li><li>Remove one unnecessary item from each area</li></ul></div></div>'''),
    ('shelf-map-sheet.html', 'Shelf Map Sheet', '''<p class="muted">Assign shelves and cubbies before they become decorative chaos platforms.</p><div class="grid"><div class="box"><h3>Shelf A</h3><div class="line"></div><div class="line"></div><div class="line"></div></div><div class="box"><h3>Shelf B</h3><div class="line"></div><div class="line"></div><div class="line"></div></div></div><div class="grid"><div class="box"><h3>Shelf C</h3><div class="line"></div><div class="line"></div><div class="line"></div></div><div class="box"><h3>Shelf D</h3><div class="line"></div><div class="line"></div><div class="line"></div></div></div>'''),
]

for filename, title, body in pages:
    html = f'<!doctype html><html><head><meta charset="utf-8"><title>{escape(title)}</title><style>{style}</style></head><body><div class="page"><h1>{escape(title)}</h1>{body}<footer>Orderforge · Small Space Storage Bundle</footer></div></body></html>'
    (out / filename).write_text(html, encoding='utf-8')

combined = ['<!doctype html><html><head><meta charset="utf-8"><title>Orderforge Small Space Storage Bundle</title><style>'+style+'</style></head><body>']
combined.append('<div class="page"><h1>Orderforge Small Space Storage Bundle</h1><p class="muted">Printable tools for making cramped rooms, shelves, drawers, and bins less chaotic.</p><div class="box"><h3>Included</h3><ul><li>Room Zone Planner</li><li>Drawer Labels</li><li>Declutter Checklist</li><li>Bin Inventory Sheet</li><li>Small Space Reset Sheet</li><li>Shelf Map Sheet</li></ul></div><footer>Orderforge</footer></div>')
for _, title, body in pages:
    combined.append(f'<div class="page"><h1>{escape(title)}</h1>{body}<footer>Orderforge · Small Space Storage Bundle</footer></div>')
combined.append('</body></html>')
(out / 'Orderforge-Small-Space-Storage-Bundle.html').write_text(''.join(combined), encoding='utf-8')
(out / 'README.txt').write_text('Orderforge Small Space Storage Bundle\n\nOpen the combined HTML file in any browser and print the pages you want. Individual printable sheets are included in this folder as separate HTML files.\n', encoding='utf-8')
print('built', out)
