import asyncio,subprocess,json
from pathlib import Path
from playwright.async_api import async_playwright
async def main():
 async with async_playwright() as p:
  b=await p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--remote-debugging-port=9224']);c=await b.new_context();page=await c.new_page();await page.goto('https://echobae.com/',wait_until='domcontentloaded');await page.locator('.age-gate__btn--primary').wait_for(state='visible',timeout=20000);await page.locator('.age-gate__btn--primary').click();await page.wait_for_timeout(3000)
  # Lighthouse uses Chrome's default context, which differs from the isolated Playwright context; transfer only the consent flag through a normal click in that context.
  default=await p.chromium.connect_over_cdp('http://127.0.0.1:9224');ctx=default.contexts[0];pg=await ctx.new_page();await pg.goto('https://echobae.com/',wait_until='domcontentloaded');await pg.locator('.age-gate__btn--primary').wait_for(state='visible',timeout=20000);await pg.locator('.age-gate__btn--primary').click();await pg.wait_for_timeout(3000)
  for n in [1,2,3]:
   cmd=['/workspace/echobae-audit/tools/node_modules/.bin/lighthouse','https://echobae.com/','--port=9224','--disable-storage-reset','--output=json','--output=html',f'--output-path=evidence/lighthouse/home-accepted-mobile-{n}','--quiet']
   r=await asyncio.to_thread(subprocess.run,cmd,capture_output=True,text=True,timeout=180);Path(f'evidence/lighthouse/home-accepted-mobile-{n}.log').write_text(r.stderr);print(n,r.returncode,flush=True)
  await b.close()
asyncio.run(main())
