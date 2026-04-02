#!/usr/bin/env node
/**
 * Orderforge Facebook Business Page Creator
 * Uses Puppeteer to automate Facebook Business Page creation
 * 
 * Usage: node create-facebook.js
 * Then enter verification codes when prompted
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
  console.log('🚀 Orderforge Facebook Business Page Creator\n');
  console.log('This will open a browser and create your Facebook Business Page.');
  console.log('You will need to handle verification if prompted.\n');

  const browser = await puppeteer.launch({
    headless: false,
    slowMo: 100,
    args: [
      '--start-maximized',
      '--disable-blink-features=AutomationControlled',
      '--no-sandbox',
      '--disable-setuid-sandbox'
    ]
  });

  const page = await browser.newPage();
  
  await page.setViewport({ width: 1366, height: 768 });
  
  // Navigate to Facebook Page Creation
  console.log('🌐 Opening Facebook Page creation...');
  await page.goto('https://www.facebook.com/pages/create/', { waitUntil: 'networkidle2' });
  
  await sleep(3000);
  
  console.log('\n📋 Step 1: Select "Business or Brand"');
  console.log('   Click the "Business or Brand" option in the browser');
  
  await ask('\n   Press Enter after clicking "Business or Brand" → ');
  
  await sleep(2000);
  
  console.log('\n📝 Step 2: Page Information');
  
  // Page Name
  console.log('   Entering Page Name: Orderforge');
  await page.type('input[placeholder="Page Name"]', 'Orderforge', { delay: 50 });
  
  await sleep(1000);
  
  // Category
  console.log('   Selecting Category: Shopping & Retail');
  const categoryInput = await page.$('input[aria-label="Category"]');
  if (categoryInput) {
    await categoryInput.type('Shopping', { delay: 50 });
    await sleep(1500);
    // Press down and enter to select
    await page.keyboard.press('ArrowDown');
    await sleep(500);
    await page.keyboard.press('Enter');
  }
  
  await sleep(1000);
  
  console.log('\n➡️  Step 3: Continue');
  console.log('   Click the "Create Page" button in the browser');
  
  await ask('\n   Press Enter after clicking "Create Page" → ');
  
  await sleep(3000);
  
  console.log('\n📝 Step 4: About Section');
  console.log('   When you get to the About section, copy-paste this:');
  console.log('─'.repeat(60));
  console.log('Orderforge makes practical digital tools and 3D-printed accessories for desks, workshops, gaming setups, storage, and small service businesses.');
  console.log('');
  console.log('No decorative nonsense. Just systems that help people look organized and move faster.');
  console.log('');
  console.log('🛒 Shop digital products: payhip.com/orderforge');
  console.log('📦 Physical products coming soon (3D printed in Vancouver)');
  console.log('─'.repeat(60));
  
  console.log('\n🖼️  Step 5: Profile Photo');
  console.log('   Upload: orderforge/assets/orderforge-logo.svg (or PNG version)');
  console.log('   Navigate to it using the file picker');
  
  await ask('\n   Press Enter after uploading profile photo → ');
  
  console.log('\n🖼️  Step 6: Cover Photo');
  console.log('   Upload: orderforge/assets/orderforge-cover.svg (820x312)');
  console.log('   Navigate to it using the file picker');
  
  await ask('\n   Press Enter after uploading cover photo → ');
  
  console.log('\n✅ Facebook Page creation steps complete!');
  console.log('\nNext steps that may appear:');
  console.log('   - Invite friends (skip for now)');
  console.log('   - Add action button (add "Shop Now" linking to payhip.com/orderforge)');
  console.log('   - Add WhatsApp (optional)');
  console.log('   - Enable Instagram Shopping (connect your IG account later)');
  
  console.log('\n📝 When you get to add a button:');
  console.log('   - Select "Shop" or "Learn More"');
  console.log('   - URL: https://payhip.com/orderforge');
  
  console.log('\n⏹️  Press Ctrl+C in this terminal when you\'re done');
  console.log('   Or close the browser window');
  
  // Keep browser open
  await new Promise(() => {});
  
})().catch(err => {
  console.error('❌ Error:', err);
  process.exit(1);
});
