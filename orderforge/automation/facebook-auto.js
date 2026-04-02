#!/usr/bin/env node
/**
 * Orderforge Facebook Business Page Creator — FULLY AUTONOMOUS
 * Uses Puppeteer to automate Facebook Business Page creation
 * Only stops for captcha/verification
 */

const puppeteer = require('puppeteer');
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function ask(question) {
  return new Promise(resolve => rl.question(question, resolve));
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

(async () => {
  console.log('🚀 Orderforge Facebook Business Page Creator — AUTONOMOUS MODE\n');
  console.log('I will click everything and fill everything.');
  console.log('I will ONLY stop if I hit a captcha or verification wall.\n');

  const browser = await puppeteer.launch({
    headless: false,
    slowMo: 150,
    executablePath: '/usr/bin/brave-browser',
    args: [
      '--start-maximized',
      '--disable-blink-features=AutomationControlled',
      '--no-sandbox',
      '--disable-setuid-sandbox',
      '--disable-dev-shm-usage'
    ]
  });

  try {
    const page = await browser.newPage();
    
    await page.setViewport({ width: 1366, height: 768 });
    
    // Set user agent to look more like a real browser
    await page.setUserAgent('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36');
    
    console.log('🌐 Opening Facebook Page creation...');
    await page.goto('https://www.facebook.com/pages/create/', { waitUntil: 'networkidle2', timeout: 60000 });
    
    await sleep(5000);
    
    console.log('📋 Step 1: Finding "Business or Brand" button...');
    
    // Try multiple selectors for the Business or Brand button
    const businessButtonSelectors = [
      'div[role="button"]',
      'span:contains("Business or Brand")',
      '[data-testid="BUSINESS"]',
      'button',
      'div[tabindex="0"]'
    ];
    
    let clicked = false;
    for (const selector of businessButtonSelectors) {
      try {
        const buttons = await page.$$(selector);
        for (const button of buttons) {
          const text = await page.evaluate(el => el.textContent, button);
          if (text && (text.includes('Business') || text.includes('Brand'))) {
            await button.click();
            console.log('   ✅ Clicked "Business or Brand"');
            clicked = true;
            break;
          }
        }
        if (clicked) break;
      } catch (e) {
        continue;
      }
    }
    
    if (!clicked) {
      console.log('   ⚠️ Could not auto-click. Waiting for you to click...');
      await ask('   Click "Business or Brand" then press Enter → ');
    }
    
    await sleep(3000);
    
    console.log('\n📝 Step 2: Filling Page Information...');
    
    // Page Name
    console.log('   Entering Page Name...');
    try {
      const nameInput = await page.$('input[placeholder*="Name"], input[name*="name"], input[type="text"]');
      if (nameInput) {
        await nameInput.click();
        await nameInput.type('Orderforge', { delay: 100 });
        console.log('   ✅ Entered "Orderforge"');
      }
    } catch (e) {
      console.log('   ⚠️ Could not find name input');
    }
    
    await sleep(2000);
    
    // Category
    console.log('   Entering Category...');
    try {
      const categoryInput = await page.$('input[placeholder*="Category"], input[aria-label*="Category"]');
      if (categoryInput) {
        await categoryInput.click();
        await categoryInput.type('Shopping and Retail', { delay: 100 });
        await sleep(2000);
        await page.keyboard.press('ArrowDown');
        await sleep(500);
        await page.keyboard.press('Enter');
        console.log('   ✅ Selected category');
      }
    } catch (e) {
      console.log('   ⚠️ Could not find category input');
    }
    
    await sleep(2000);
    
    console.log('\n➡️  Step 3: Clicking Create Page...');
    
    // Find and click Create Page button
    try {
      const buttons = await page.$$('div[role="button"], button');
      for (const button of buttons) {
        const text = await page.evaluate(el => el.textContent || el.innerText, button);
        if (text && (text.includes('Create') || text.includes('Page'))) {
          await button.click();
          console.log('   ✅ Clicked Create Page');
          break;
        }
      }
    } catch (e) {
      console.log('   ⚠️ Could not auto-click Create Page');
    }
    
    await sleep(5000);
    
    // Check for captcha
    const pageContent = await page.content();
    if (pageContent.includes('captcha') || pageContent.includes('security check') || pageContent.includes('verify')) {
      console.log('\n🛑 HUMAN WALL: Captcha or verification detected!');
      console.log('   Please solve the captcha in the browser window.');
      await ask('   Press Enter after solving captcha → ');
    }
    
    console.log('\n✅ Autonomous steps complete!');
    console.log('\n📝 If you reach the About section, copy-paste this:');
    console.log('─'.repeat(60));
    console.log('Orderforge makes practical digital tools and 3D-printed accessories for desks, workshops, gaming setups, storage, and small service businesses.');
    console.log('');
    console.log('No decorative nonsense. Just systems that help people look organized and move faster.');
    console.log('');
    console.log('🛒 Shop: payhip.com/orderforge');
    console.log('─'.repeat(60));
    
    console.log('\n🖼️  Upload these files for photos:');
    console.log('   Profile: orderforge/assets/orderforge-logo.svg');
    console.log('   Cover: orderforge/assets/orderforge-cover.svg');
    
    console.log('\n⏹️  Browser will remain open. Close it when done.');
    
    // Keep alive
    await new Promise(() => {});
    
  } catch (error) {
    console.error('❌ Error:', error);
    console.log('\nBrowser staying open for debugging.');
    await new Promise(() => {});
  }
})();
