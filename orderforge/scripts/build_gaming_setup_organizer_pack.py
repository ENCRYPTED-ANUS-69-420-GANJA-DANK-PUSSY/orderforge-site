from pathlib import Path
from html import escape

root = Path('/home/matt/.openclaw/workspace/orderforge/products/gaming-setup-organizer-pack')
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
    ('setup-layout-planner.html', 'Setup Layout Planner', '''<p class="muted">Map monitor, console, controller, and accessory placement before the cable nest takes over.</p><div class="box"><p>Main display</p><div class="line"></div><p>Console / PC placement</p><div class="line"></div><p>Audio gear</p><div class="line"></div><p>Charging zone</p><div class="line"></div><p>Quick-access storage</p><div class="line"></div></div>'''),
    ('cable-map-sheet.html', 'Cable Map Sheet', '''<p class="muted">Track power, HDMI, USB, and charging routes.</p><div class="box"><p class="small">Cable / Device / Route / Hidden? / Replace?</p><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div></div>'''),
    ('accessory-inventory.html', 'Accessory Inventory', '''<p class="muted">Controllers, docks, headsets, chargers, capture gear — all the little expensive bits.</p><div class="box"><p class="small">Accessory / Storage spot / Used daily? / Missing part?</p><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div></div>'''),
    ('charging-station-plan.html', 'Charging Station Plan', '''<div class="grid"><div class="box"><h3>Devices to charge</h3><ul><li>Controller 1</li><li>Controller 2</li><li>Headset</li><li>Phone</li><li>Portable battery</li></ul></div><div class="box"><h3>Charging zone notes</h3><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div></div></div>'''),
    ('daily-reset-checklist.html', 'Daily Reset Checklist', '''<div class="box"><ul><li>Put controller back on dock / stand</li><li>Reset headset / accessories</li><li>Tidy visible cables</li><li>Clear drink wrappers / clutter</li><li>Put handheld devices back in place</li><li>Prep primary setup for next session</li></ul></div>'''),
    ('streaming-addons-sheet.html', 'Streaming / Add-ons Sheet', '''<p class="muted">Optional planning sheet for streamers or recording setups.</p><div class="box"><p>Mic / boom arm</p><div class="line"></div><p>Camera / lighting</p><div class="line"></div><p>Capture card</p><div class="line"></div><p>Scene or desk issues</p><div class="line"></div></div>'''),
]

for filename, title, body in pages:
    html = f'<!doctype html><html><head><meta charset="utf-8"><title>{escape(title)}</title><style>{style}</style></head><body><div class="page"><h1>{escape(title)}</h1>{body}<footer>Orderforge · Gaming Setup Organizer Pack</footer></div></body></html>'
    (out / filename).write_text(html, encoding='utf-8')

combined = ['<!doctype html><html><head><meta charset="utf-8"><title>Orderforge Gaming Setup Organizer Pack</title><style>'+style+'</style></head><body>']
combined.append('<div class="page"><h1>Orderforge Gaming Setup Organizer Pack</h1><p class="muted">Printable tools for cleaner gaming desks, console setups, charging zones, and accessory storage.</p><div class="box"><h3>Included</h3><ul><li>Setup Layout Planner</li><li>Cable Map Sheet</li><li>Accessory Inventory</li><li>Charging Station Plan</li><li>Daily Reset Checklist</li><li>Streaming / Add-ons Sheet</li></ul></div><footer>Orderforge</footer></div>')
for _, title, body in pages:
    combined.append(f'<div class="page"><h1>{escape(title)}</h1>{body}<footer>Orderforge · Gaming Setup Organizer Pack</footer></div>')
combined.append('</body></html>')
(out / 'Orderforge-Gaming-Setup-Organizer-Pack.html').write_text(''.join(combined), encoding='utf-8')
(out / 'README.txt').write_text('Orderforge Gaming Setup Organizer Pack\n\nOpen the combined HTML file in any browser and print the pages you want. Individual printable sheets are included in this folder as separate HTML files.\n', encoding='utf-8')
print('built', out)
