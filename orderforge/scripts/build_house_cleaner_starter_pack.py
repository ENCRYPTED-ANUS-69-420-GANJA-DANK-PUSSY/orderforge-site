from pathlib import Path
from html import escape

root = Path('/home/matt/.openclaw/workspace/orderforge/products/house-cleaner-starter-pack')
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
    ('quote-template.html', 'Quote Template', '''<p class="muted">Simple quote sheet for residential cleaning jobs.</p><div class="box"><p>Business name</p><div class="line"></div><p>Client name</p><div class="line"></div><p>Address</p><div class="line"></div><p>Service type</p><div class="line"></div><p>Quote amount</p><div class="line"></div><p>Notes / add-ons</p><div class="line"></div><div class="line"></div></div>'''),
    ('invoice-template.html', 'Invoice Template', '''<p class="muted">Clean, simple invoice layout for one-off or recurring cleaning jobs.</p><div class="box"><p>Invoice number</p><div class="line"></div><p>Date</p><div class="line"></div><p>Client</p><div class="line"></div><p>Service completed</p><div class="line"></div><p>Amount due</p><div class="line"></div><p>Payment method</p><div class="line"></div></div>'''),
    ('pricing-sheet-builder.html', 'Pricing Sheet Builder', '''<p class="muted">Map standard services and upsells before customers start asking weirdly specific questions.</p><div class="grid"><div class="box"><h3>Core services</h3><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div></div><div class="box"><h3>Add-ons</h3><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div></div></div><div class="box"><h3>Travel / minimums / policy notes</h3><div class="line"></div><div class="line"></div><div class="line"></div></div>'''),
    ('service-checklist.html', 'Service Checklist', '''<p class="muted">Use this as a client-facing or internal checklist.</p><div class="grid"><div class="box"><h3>Kitchen</h3><ul><li>Counters</li><li>Sink</li><li>Appliances</li><li>Cabinet fronts</li><li>Floor</li></ul></div><div class="box"><h3>Bathrooms</h3><ul><li>Toilet</li><li>Sink</li><li>Mirror</li><li>Shower / tub</li><li>Floor</li></ul></div></div><div class="grid"><div class="box"><h3>Living areas</h3><ul><li>Dust surfaces</li><li>Vacuum</li><li>Baseboards spot-check</li><li>Tidy visible clutter</li></ul></div><div class="box"><h3>Bedrooms</h3><ul><li>Dust surfaces</li><li>Vacuum / sweep</li><li>Make beds (optional)</li><li>Trash</li></ul></div></div>'''),
    ('review-request-templates.html', 'Review Request Templates', '''<p class="muted">Short customer follow-up scripts that don\'t sound like a robot with a spray bottle.</p><div class="box"><h3>SMS</h3><p class="small">Hi [Name], thanks again for booking with [Business Name]. If you were happy with the clean, a quick review would help a lot: [link]</p></div><div class="box"><h3>Email</h3><p class="small">Subject: Quick favor after your cleaning appointment</p><p class="small">Hi [Name], thanks again for having us over. If everything looked great, we\'d really appreciate a quick review here: [link]. It helps more than you\'d think.</p></div></div>'''),
    ('referral-card-copy.html', 'Referral Card Copy', '''<p class="muted">Simple wording for a printable referral card or handout.</p><div class="box"><h3>Front</h3><p class="small">Love a clean house? Pass this on.</p><p class="small">[Business Name]</p><p class="small">Reliable home cleaning for busy people.</p></div><div class="box"><h3>Back</h3><p class="small">Book your first clean and mention this card for [offer].</p><p class="small">Phone: ________</p><p class="small">Website / booking link: ________</p></div>'''),
    ('before-after-content-prompts.html', 'Before / After Content Prompts', '''<p class="muted">Prompts and captions for basic social proof posts.</p><div class="box"><ul><li>Before / after of kitchen counters + sink</li><li>Bathroom refresh close-up</li><li>Quick reel: 3 things cleaned in 20 seconds</li><li>Caption: “A small reset makes the whole house feel better.”</li><li>Caption: “Not glamorous. Just reliably clean.”</li><li>Caption: “Busy week? We handle the part nobody wants to do.”</li></ul></div>'''),
    ('flyer-template.html', 'Promo Flyer Template', '''<p class="muted">Simple local promo flyer structure.</p><div class="box"><h3>Headline</h3><div class="line"></div><h3>Subhead</h3><div class="line"></div><h3>What\'s included</h3><div class="line"></div><div class="line"></div><div class="line"></div><h3>Offer / CTA</h3><div class="line"></div><h3>Contact info</h3><div class="line"></div></div>'''),
]

for filename, title, body in pages:
    html = f'''<!doctype html><html><head><meta charset="utf-8"><title>{escape(title)}</title><style>{style}</style></head><body><div class="page"><h1>{escape(title)}</h1>{body}<footer>Orderforge · House Cleaner Starter Pack</footer></div></body></html>'''
    (out / filename).write_text(html, encoding='utf-8')

combined = ['<!doctype html><html><head><meta charset="utf-8"><title>Orderforge House Cleaner Starter Pack</title><style>'+style+'</style></head><body>']
combined.append('<div class="page"><h1>Orderforge House Cleaner Starter Pack</h1><p class="muted">Practical templates and scripts for solo cleaners and small residential cleaning businesses.</p><div class="box"><h3>Included</h3><ul><li>Quote Template</li><li>Invoice Template</li><li>Pricing Sheet Builder</li><li>Service Checklist</li><li>Review Request Templates</li><li>Referral Card Copy</li><li>Before / After Content Prompts</li><li>Promo Flyer Template</li></ul></div><footer>Orderforge</footer></div>')
for _, title, body in pages:
    combined.append(f'<div class="page"><h1>{escape(title)}</h1>{body}<footer>Orderforge · House Cleaner Starter Pack</footer></div>')
combined.append('</body></html>')
(out / 'Orderforge-House-Cleaner-Starter-Pack.html').write_text(''.join(combined), encoding='utf-8')
(out / 'README.txt').write_text('Orderforge House Cleaner Starter Pack\n\nOpen the combined HTML file in any browser and print the pages you want. Individual printable sheets are included in this folder as separate HTML files.\n', encoding='utf-8')
(out / 'social-captions.txt').write_text('''House Cleaner Starter Pack social captions\n\n1. A clean house is nice. A reliable cleaning system is better.\n2. Busy people don\'t need more guilt. They need one less chore.\n3. Before and after content works best when the result is obvious, not over-filtered.\n4. A repeatable quote + invoice + review system saves time every single week.\n5. Small service businesses do better when they look organized, even before they scale.\n''', encoding='utf-8')
print('built', out)
