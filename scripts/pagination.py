import asyncio,json
from pathlib import Path
from playwright.async_api import async_playwright
async def main():
 async with async_playwright() as p:
  b=await p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);c=await b.new_context();page=await c.new_page();out=[];seen=set()
  await page.goto('https://echobae.com/products',wait_until='domcontentloaded')
  for n in range(1,13):
   await page.wait_for_timeout(2000)
   for sel in ['.age-gate__btn--primary','.mkt-popup__close']:
    l=page.locator(sel)
    if await l.count() and await l.first.is_visible():await l.first.click()
   urls=await page.locator('a[href*="/p/"]').evaluate_all('(xs)=>[...new Set(xs.map(x=>x.href))]');out.append({'page':n,'urls':urls,'url':page.url});seen.update(urls);print(n,len(urls),flush=True)
   btn=page.get_by_role('button',name='Next',exact=True)
   if not await btn.count() or await btn.is_disabled():break
   await btn.click()
   try:await page.wait_for_function("(old)=>document.querySelector('a[href*=\"/p/\"]')?.href!==old",arg=urls[0] if urls else '',timeout=12000)
   except Exception:pass
  D=Path('evidence');(D/'pagination.json').write_text(json.dumps(out,indent=2));old=set(json.load(open(D/'discovered.json')));(D/'discovered.json').write_text(json.dumps(sorted(old|seen),indent=2));await b.close()
asyncio.run(main())
