# Orderforge Site Deployment

## Quick Options

### Option 1: Netlify Drop (Fastest)
1. Go to https://app.netlify.com/drop
2. Drag the `orderforge/site/` folder onto the page
3. Done. You'll get a random URL like `random-name.netlify.app`
4. Optional: Add custom domain in Netlify settings

### Option 2: GitHub Pages (Free)
1. Create repo on GitHub
2. Push the `site/` folder contents to `main` branch
3. Settings → Pages → Source: Deploy from branch → main
4. Site will be at `username.github.io/repo-name`

### Option 3: Cloudflare Pages (Free)
1. Go to https://pages.cloudflare.com
2. Connect GitHub repo
3. Set build output to `/site`
4. Deploy

### Option 4: Vercel (Free)
1. `npx vercel ./site` from workspace root
2. Follow prompts
3. Done

### Option 5: Any Web Host
Upload contents of `orderforge/site/` folder to public_html or www folder via FTP/SFTP.

---

## Custom Domain Setup

Once deployed, point a domain:
1. Buy domain (Namecheap, Cloudflare, Google Domains, etc.)
2. Add CNAME record pointing to hosting provider
3. Configure in hosting dashboard

For Netlify/Vercel/Cloudflare Pages, they handle SSL automatically.

---

## Files to Deploy

Just upload everything in:
```
orderforge/site/
├── index.html
├── style.css
├── favicon.svg
└── orderforge-about-image.png
```

That's it. No build step needed.