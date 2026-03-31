from pathlib import Path
from html import escape

root = Path('/home/matt/.openclaw/workspace/orderforge/products/workshop-starter-pack')
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
    ('tool-inventory-sheet.html', 'Tool Inventory Sheet', '''<p class="muted">Track what you own before it vanishes into workshop entropy.</p><div class="box"><h3>Inventory</h3><p class="small">Tool / Type / Storage location / Condition / Replace or keep</p><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div></div>'''),
    ('hardware-bin-labels.html', 'Hardware Bin Labels', '''<p class="muted">Sort the tiny metal chaos before it breeds.</p><div class="box"><h3>Suggested label categories</h3><ul><li>Screws</li><li>Nuts</li><li>Bolts</li><li>Washers</li><li>Anchors</li><li>Electrical</li><li>Spare Parts</li><li>Fasteners</li><li>Bits & Blades</li><li>Adhesives</li></ul></div><div class="box"><h3>Custom labels</h3><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div></div>'''),
    ('pegboard-layout-planner.html', 'Pegboard Layout Planner', '''<p class="muted">Plan what hangs where before you start drilling regret into the wall.</p><div class="grid"><div class="box"><h3>Priority tools</h3><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div></div><div class="box"><h3>Fast-access zone</h3><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div></div></div><div class="box"><h3>Layout notes</h3><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div></div>'''),
    ('maintenance-log.html', 'Maintenance Log', '''<p class="muted">Keep a simple log for sharpening, battery swaps, calibration, and upkeep.</p><div class="box"><p class="small">Date / Tool or machine / Task performed / Next action</p><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div></div>'''),
    ('project-parts-tracker.html', 'Project Parts Tracker', '''<p class="muted">Prevent half-finished project bins from becoming archaeological sites.</p><div class="box"><h3>Project name</h3><div class="line"></div><h3>Needed parts</h3><div class="line"></div><div class="line"></div><div class="line"></div><h3>Missing items</h3><div class="line"></div><div class="line"></div><h3>Status notes</h3><div class="line"></div><div class="line"></div></div>'''),
    ('storage-map-sheet.html', 'Storage Map Sheet', '''<p class="muted">Map shelves, drawers, and bins so you stop rebuying things you already own.</p><div class="grid"><div class="box"><h3>Zone A</h3><div class="line"></div><div class="line"></div><div class="line"></div></div><div class="box"><h3>Zone B</h3><div class="line"></div><div class="line"></div><div class="line"></div></div></div><div class="grid"><div class="box"><h3>Zone C</h3><div class="line"></div><div class="line"></div><div class="line"></div></div><div class="box"><h3>Zone D</h3><div class="line"></div><div class="line"></div><div class="line"></div></div></div>'''),
]

for filename, title, body in pages:
    html = f'''<!doctype html><html><head><meta charset="utf-8"><title>{escape(title)}</title><style>{style}</style></head><body><div class="page"><h1>{escape(title)}</h1>{body}<footer>Orderforge · Workshop Starter Pack</footer></div></body></html>'''
    (out / filename).write_text(html, encoding='utf-8')

combined = ['<!doctype html><html><head><meta charset="utf-8"><title>Orderforge Workshop Starter Pack</title><style>'+style+'</style></head><body>']
combined.append('<div class="page"><h1>Orderforge Workshop Starter Pack</h1><p class="muted">Printable workshop organization tools for makers, garages, benches, and hardware chaos.</p><div class="box"><h3>Included</h3><ul><li>Tool Inventory Sheet</li><li>Hardware Bin Labels</li><li>Pegboard Layout Planner</li><li>Maintenance Log</li><li>Project Parts Tracker</li><li>Storage Map Sheet</li></ul></div><footer>Orderforge</footer></div>')
for _, title, body in pages:
    combined.append(f'<div class="page"><h1>{escape(title)}</h1>{body}<footer>Orderforge · Workshop Starter Pack</footer></div>')
combined.append('</body></html>')
(out / 'Orderforge-Workshop-Starter-Pack.html').write_text(''.join(combined), encoding='utf-8')
(out / 'README.txt').write_text('Orderforge Workshop Starter Pack\n\nOpen the combined HTML file in any browser and print the pages you want. Individual printable sheets are included in this folder as separate HTML files.\n', encoding='utf-8')
print('built', out)
