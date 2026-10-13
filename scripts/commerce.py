import asyncio,json,re
from pathlib import Path
from playwright.async_api import async_playwright
D=Path('evidence/browser');results=[]
async def snap(page,label):
 await page.wait_for_timeout(900);await page.screenshot(path=str(D/f'flow-{label}.png'));r=await page.evaluate('''()=>({url:location.href,text:document.body.innerText,buttons:[...document.querySelectorAll('button')].map(x=>({text:x.innerText,aria:x.getAttribute('aria-label')})),inputs:[...document.querySelectorAll('input,select')].map(x=>({tag:x.tagName,type:x.type,name:x.name,placeholder:x.placeholder,aria:x.getAttribute('aria-label'),options:x.tagName==='SELECT'?[...x.options].map(o=>o.text):undefined}))})''');r['step']=label;results.append(r);(D/'commerce.json').write_text(json.dumps(results,ensure_ascii=False,indent=2));print(label,r['url'],flush=True)
 close=page.locator('.mkt-popup__close')
 if await close.count() and await close.first.is_visible():await close.first.click()
async def age(page):
 b=page.get_by_role('button',name='I am 18 or older',exact=True)
 try:
  await b.wait_for(state='visible',timeout=6000);await b.click();await page.wait_for_timeout(400)
 except Exception:pass
async def main():
 async with async_playwright() as p:
  b=await p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);c=await b.new_context(viewport={'width':390,'height':844},is_mobile=True,has_touch=True);page=await c.new_page()
  async def guard(route):
   r=route.request
   if r.method not in ['GET','HEAD','OPTIONS'] and re.search(r'(order|payment|subscribe|newsletter|contact|checkout)',r.url,re.I):
    results.append({'step':'blocked-side-effect','url':r.url,'method':r.method});await route.abort()
   else:await route.continue_()
  await c.route('**/*',guard)
  try:
   await page.goto('https://echobae.com/',wait_until='domcontentloaded');await page.wait_for_timeout(6000);await snap(page,'age-first');await age(page);await snap(page,'age-confirmed');await page.reload(wait_until='domcontentloaded');await snap(page,'age-refresh')
   await page.goto('https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia',wait_until='domcontentloaded');await page.wait_for_timeout(1600);await age(page);await snap(page,'product-base')
   await page.get_by_role('button',name='Next image',exact=True).click();await snap(page,'image-next')
   await page.get_by_role('button',name=re.compile(r'^AI\s*\+\$79.99')).click();await snap(page,'product-upgrade')
   await age(page);await snap(page,'before-add-popup');
   close=page.locator('.mkt-popup button').filter(has_text='×')
   if await close.count():await close.first.click()
   else:
    close=page.locator('.mkt-popup__close')
    if await close.count():await close.first.click()
   await page.get_by_role('button',name='ADD TO CART',exact=True).click();await snap(page,'add-cart')
   await page.goto('https://echobae.com/cart',wait_until='domcontentloaded');await snap(page,'cart')
   plus=page.get_by_role('button',name='+',exact=True)
   if await plus.count():await plus.first.click();await snap(page,'cart-quantity-two')
   # Only navigate to checkout; never submit order, payment or personal data.
   links=await page.locator('a[href*="checkout"]').count()
   if links:await page.locator('a[href*="checkout"]').first.click()
   else:await page.goto('https://echobae.com/checkout',wait_until='domcontentloaded')
   await snap(page,'checkout')
   await page.goto('https://echobae.com/cart',wait_until='domcontentloaded');await snap(page,'return-cart')
   remove=page.get_by_role('button',name=re.compile('remove',re.I))
   if await remove.count():await remove.first.click();await snap(page,'remove-cart')
   for q in ['silicone','Lydia','audit-no-result-20261013']:
    await page.goto('https://echobae.com/search?q='+q,wait_until='domcontentloaded');await snap(page,'search-'+q)
   await page.goto('https://echobae.com/products',wait_until='domcontentloaded');await snap(page,'filters-initial');await page.get_by_role('button',name='Next',exact=True).click();await snap(page,'pagination-next')
   select=page.locator('select')
   if await select.count():
    opts=await select.first.locator('option').evaluate_all('(xs)=>xs.map(x=>({value:x.value,text:x.textContent}))');results.append({'step':'sort-options','options':opts})
    if len(opts)>1:await select.first.select_option(opts[1]['value']);await snap(page,'sort')
  except Exception as e:results.append({'step':'exception','error':str(e)});print(str(e),flush=True)
  await b.close();(D/'commerce.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
asyncio.run(main())
