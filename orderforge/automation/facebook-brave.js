#!/usr/bin/env node
/**
 * Orderforge Facebook Business Page Creator — BRAVE BROWSER VERSION
 * Uses Puppeteer with Brave browser
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
  console.log('🚀 Orderforge Facebook Business Page Creator — BRAVE MODE\n');
  console.log('Using Brave browser.\n');

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
    
    await page.setUserAgent('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36');
    
    console.log('🌐 Opening Facebook Page creation...');
    await page.goto('https://www.facebook.com/pages/create/', { waitUntil: 'networkidle2', timeout: 60000 });
    
    await sleep(5000);
    
    console.log('📋 Step 1: Click "Business or Brand"');
    console.log('   ⚠️ Waiting for you to click it...');
    await ask('   Click "Business or Brand" in Brave, then press Enter → ');
    
    await sleep(3000);
    
    console.log('\n📝 Step 2: Filling Page Information...');
    
    // Page Name
    console.log('   Entering "Orderforge"...');
    try {
      const nameInput = await page.$('input[placeholder*="Name"], input[type="text"]');
      if (nameInput) {
        await nameInput.click();
        await nameInput.type('Orderforge', { delay: 100 });
        console.log('   ✅ Name entered');
      }
    } catch (e) {
      console.log('   ⚠️ Could not enter name automatically');
    }
    
    await sleep(2000);
    
    // Category
    console.log('   Entering Category...');
    try {
      const categoryInput = await page.$('input[placeholder*="Category"], input[aria-label*="Category"]');
      if (categoryInput) {
        await categoryInput.click();
        await categoryInput.type('Shopping', { delay: 100 });
        await sleep(2000);
        await page.keyboard.press('ArrowDown');
        await sleep(500);
        await page.keyboard.press('Enter');
        console.log('   ✅ Category selected');
      }
    } catch (e) {
      console.log('   ⚠️ Could not enter category automatically');
    }
    
    await sleep(2000);
    
    console.log('\n➡️  Step 3: Click "Create Page"');
    console.log('   ⚠️ Waiting for you to click it...');
    await ask('   Click "Create Page" button, then press Enter → ');
    
    await sleep(5000);
    
    // Check for captcha
    const pageContent = await page.content();
    if (pageContent.includes('captcha') || pageContent.includes('security') || pageContent.includes('verify') || pageContent.includes('Are you')) {
      console.log('\n🛑 HUMAN WALL: Verification detected!');
      await ask('   Solve it in Brave, then type "done" → ');
    }
    
    console.log('\n✅ Form submission complete!');
    console.log('\n📝 COPY-PASTE this for About section:');
    console.log('─'.repeat(60));
    console.log('Orderforge makes practical digital tools and 3D-printed accessories for desks, workshops, gaming setups, storage, and small service businesses.');
    console.log('');
    console.log('No decorative nonsense. Just systems that help people look organized and move faster.');
    console.log('');
    console.log('🛒 Shop: payhip.com/orderforge');
    console.log('─'.repeat(60));
    
    console.log('\n🖼️  PROFILE PHOTO:');
    console.log('   Upload: /home/matt/.openclaw/workspace/orderforge/assets/orderforge-logo.svg');
    
    console.log('\n🖼️  COVER PHOTO:');
    console.log('   Upload: /home/matt/.openclaw/workspace/orderforge/assets/orderforge-cover.svg');
    
    console.log('\n⏹️  Browser staying open. Press Ctrl+C here when done.');
    
    await new Promise(() => {});
    
  } catch (error) {
    console.error('❌ Error:', error);
    await new Promise(() => {});
  }
})();
