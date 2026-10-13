import asyncio,json
from pathlib import Path
from playwright.async_api import async_playwright
async def main():
 async with async_playwright() as p:
  b=await p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);c=await b.new_context(viewport={'width':390,'height':844});page=await c.new_page();await page.goto('https://echobae.com/',wait_until='domcontentloaded');await page.locator('.age-gate').wait_for(state='visible',timeout=20000);out=[]
  for i in range(12):
   await page.keyboard.press('Tab');out.append(await page.evaluate('''()=>({tag:document.activeElement.tagName,text:document.activeElement.innerText?.slice(0,100),aria:document.activeElement.getAttribute('aria-label'),insideAge:!!document.activeElement.closest('.age-gate')})'''))
  await page.screenshot(path='evidence/browser/age-keyboard.png');await page.locator('.age-gate__btn--primary').click();await page.reload(wait_until='domcontentloaded');await page.wait_for_timeout(5000);state={'ageVisible':await page.locator('.age-gate').count(),'storagePresent':await page.evaluate("localStorage.getItem('ecom-age-gate-verified')!==null")}
  Path('evidence/browser/age-keyboard.json').write_text(json.dumps({'tabs':out,'afterConfirmationReload':state},ensure_ascii=False,indent=2));await b.close();print(out,state)
asyncio.run(main())
