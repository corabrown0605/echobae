import asyncio,hashlib,json
from pathlib import Path
from playwright.async_api import async_playwright
async def main():
 async with async_playwright() as p:
  b=await p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);out=[]
  for device,size in [('desktop',{'width':1440,'height':900}),('mobile',{'width':390,'height':844})]:
   c=await b.new_context(viewport=size,is_mobile=device=='mobile');page=await c.new_page()
   for path in ['/','/products','/collections/new-arrival','/p/159cm-lifelike-silicone-sex-doll-lydia','/blog/tpe-vs-silicone-sex-doll','/customer-reviews']:
    await page.goto('https://echobae.com'+path,wait_until='domcontentloaded');await page.wait_for_timeout(6000)
    for sel in ['.age-gate__btn--primary','.mkt-popup__close']:
     l=page.locator(sel)
     if await l.count() and await l.first.is_visible():await l.first.click()
    await page.wait_for_timeout(500);key=hashlib.sha256(path.encode()).hexdigest()[:10];f=f'evidence/browser/{device}-{key}-settled.png';await page.screenshot(path=f);out.append({'url':page.url,'device':device,'viewport':size,'screenshot':f})
   await c.close()
  await b.close();Path('evidence/browser/settled-screens.json').write_text(json.dumps(out,indent=2))
asyncio.run(main())
