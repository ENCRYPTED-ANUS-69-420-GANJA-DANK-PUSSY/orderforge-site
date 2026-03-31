from pathlib import Path
from html import escape

root = Path('/home/matt/.openclaw/workspace/orderforge/products/editable-label-pack')
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
    ('bin-label-sheet.html', 'Bin Label Sheet', '''<div class="box"><p class="small">Use for bins, baskets, tubs, and garage storage.</p><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div></div>'''),
    ('drawer-label-sheet.html', 'Drawer Label Sheet', '''<div class="box"><p class="small">Use for desk drawers, kitchen drawers, workshop drawers, and parts storage.</p><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div></div>'''),
    ('cable-tag-sheet.html', 'Cable Tag Sheet', '''<div class="box"><p class="small">Use for power bricks, chargers, monitors, hubs, consoles, and peripherals.</p><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div></div>'''),
    ('tool-label-sheet.html', 'Tool Label Sheet', '''<div class="box"><p class="small">Use for bins, pegboards, organizers, and drawers in a workshop or garage.</p><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div></div>'''),
    ('category-tag-sheet.html', 'Category Tag Sheet', '''<div class="box"><p class="small">Suggested categories:</p><ul><li>Daily Use</li><li>Spare Parts</li><li>Cables</li><li>Charging</li><li>Seasonal</li><li>Cleaning</li><li>Office</li><li>Gaming</li><li>Workshop</li><li>Misc</li></ul></div>'''),
    ('label-planning-sheet.html', 'Label Planning Sheet', '''<div class="grid"><div class="box"><h3>Where labels are needed</h3><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div></div><div class="box"><h3>Which labels should match?</h3><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div></div></div>'''),
]

for filename, title, body in pages:
    html = f'<!doctype html><html><head><meta charset="utf-8"><title>{escape(title)}</title><style>{style}</style></head><body><div class="page"><h1>{escape(title)}</h1>{body}<footer>Orderforge · Editable Label Pack</footer></div></body></html>'
    (out / filename).write_text(html, encoding='utf-8')

combined = ['<!doctype html><html><head><meta charset="utf-8"><title>Orderforge Editable Label Pack</title><style>'+style+'</style></head><body>']
combined.append('<div class="page"><h1>Orderforge Editable Label Pack</h1><p class="muted">Clean printable labels for bins, drawers, cables, tools, and storage categories.</p><div class="box"><h3>Included</h3><ul><li>Bin Label Sheet</li><li>Drawer Label Sheet</li><li>Cable Tag Sheet</li><li>Tool Label Sheet</li><li>Category Tag Sheet</li><li>Label Planning Sheet</li></ul></div><footer>Orderforge</footer></div>')
for _, title, body in pages:
    combined.append(f'<div class="page"><h1>{escape(title)}</h1>{body}<footer>Orderforge · Editable Label Pack</footer></div>')
combined.append('</body></html>')
(out / 'Orderforge-Editable-Label-Pack.html').write_text(''.join(combined), encoding='utf-8')
(out / 'README.txt').write_text('Orderforge Editable Label Pack\n\nOpen the combined HTML file in any browser and print the pages you want. Individual printable sheets are included in this folder as separate HTML files.\n', encoding='utf-8')
print('built', out)
