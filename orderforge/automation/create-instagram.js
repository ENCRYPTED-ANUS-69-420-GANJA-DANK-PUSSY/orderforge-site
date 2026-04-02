#!/usr/bin/env node
/**
 * Orderforge Instagram Account Creator
 * Uses Puppeteer to automate Instagram signup
 * 
 * Usage: node create-instagram.js
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

(async () => {
  console.log('🚀 Orderforge Instagram Account Creator\n');
  console.log('This will open a browser and walk you through Instagram signup.');
  console.log('You will need to enter verification codes when prompted.\n');

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
  
  // Set viewport
  await page.setViewport({ width: 1366, height: 768 });
  
  // Navigate to Instagram signup
  console.log('🌐 Opening Instagram signup page...');
  await page.goto('https://www.instagram.com/accounts/emailsignup/', { waitUntil: 'networkidle2' });
  
  // Wait for the email/phone toggle
  await page.waitForTimeout(2000);
  
  console.log('\n📧 Step 1: Email Signup');
  
  // Click "Sign up with email" if present
  try {
    const emailButton = await page.$('button[tabindex="0"]');
    if (emailButton) {
      await emailButton.click();
      console.log('   Clicked "Sign up with email"');
    }
  } catch (e) {
    console.log('   Email option already selected or not found');
  }
  
  await page.waitForTimeout(1500);
  
  // Fill email
  console.log('   Entering email: Matthew.Phoenix@mail.com');
  await page.type('input[name="email"]', 'Matthew.Phoenix@mail.com', { delay: 50 });
  
  await page.waitForTimeout(1000);
  
  // Fill full name
  console.log('   Entering full name: Orderforge');
  await page.type('input[name="fullName"]', 'Orderforge', { delay: 50 });
  
  await page.waitForTimeout(1000);
  
  // Fill username - try orderforge first
  console.log('   Entering username...');
  await page.type('input[name="username"]', 'orderforge', { delay: 50 });
  
  await page.waitForTimeout(2000);
  
  // Check if username is taken (look for error message)
  const pageContent = await page.content();
  if (pageContent.includes('not available') || pageContent.includes('taken')) {
    console.log('   ⚠️ Username "orderforge" is taken. Trying alternatives...');
    
    // Clear and try alternatives
    await page.click('input[name="username"]', { clickCount: 3 });
    await page.type('input[name="username"]', 'orderforge_digital', { delay: 50 });
    await page.waitForTimeout(2000);
  }
  
  // Wait for password field
  await page.waitForTimeout(1000);
  
  console.log('\n🔐 Step 2: Password');
  console.log('   Waiting for you to enter password manually...');
  console.log('   (Type password in browser, then press Enter here to continue)');
  
  await ask('\n   Press Enter after you\'ve entered password → ');
  
  await page.waitForTimeout(1000);
  
  // Click Sign Up
  console.log('   Clicking Sign Up button...');
  const signUpButton = await page.$('button[type="submit"]');
  if (signUpButton) {
    await signUpButton.click();
  }
  
  console.log('\n⏳ Waiting for email verification...');
  console.log('   Check Matthew.Phoenix@mail.com for the verification code');
  
  const verificationCode = await ask('\n📨 Enter verification code from email: ');
  
  // Fill verification code
  await page.type('input[type="text"]', verificationCode, { delay: 100 });
  
  await page.waitForTimeout(1000);
  
  // Click Next
  const nextButton = await page.$('button[type="button"]');
  if (nextButton) {
    await nextButton.click();
  }
  
  console.log('\n✅ Account creation initiated!');
  console.log('\nNext steps that may appear:');
  console.log('   - Birthday verification (enter your birthday)');
  console.log('   - Profile photo upload');
  console.log('   - Bio setup');
  console.log('   - Switch to business account');
  
  console.log('\n📝 Bio to copy-paste when you get there:');
  console.log('─'.repeat(50));
  console.log('Digital tools & 3D-printed accessories for small businesses. Practical stuff, no fluff.');
  console.log('');
  console.log('payhip.com/orderforge ↓');
  console.log('─'.repeat(50));
  
  console.log('\n⏹️  Press Ctrl+C in this terminal when you\'re done in the browser');
  console.log('   Or close the browser window');
  
  // Keep browser open
  await new Promise(() => {});
  
})().catch(err => {
  console.error('❌ Error:', err);
  process.exit(1);
});
