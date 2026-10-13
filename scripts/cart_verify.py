import asyncio,json,re
from pathlib import Path
from playwright.async_api import async_playwright
D=Path('evidence/browser');out=[]
async def main():
 async with async_playwright() as p:
  b=await p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);c=await b.new_context(viewport={'width':390,'height':844},is_mobile=True);page=await c.new_page();net=[]
  page.on('response',lambda r:net.append({'url':r.url,'status':r.status,'type':r.request.resource_type}))
  async def dismiss():
   for sel in ['.age-gate__btn--primary','.mkt-popup__close']:
    l=page.locator(sel)
    if await l.count() and await l.first.is_visible():await l.first.click();await page.wait_for_timeout(300)
  async def snap(label):
   await page.wait_for_timeout(4500);await dismiss();await page.screenshot(path=str(D/f'verify-{label}.png'));data=await page.evaluate('''()=>({url:location.href,text:document.body.innerText,buttons:[...document.querySelectorAll('button')].map(x=>({text:x.innerText,aria:x.getAttribute('aria-label')})),inputs:[...document.querySelectorAll('input,select')].map(x=>({type:x.type,name:x.name,placeholder:x.placeholder,options:x.tagName==='SELECT'?[...x.options].map(x=>x.text):null})),storageKeys:Object.keys(localStorage)})''');data.update(step=label);out.append(data);(D/'cart-verify.json').write_text(json.dumps(out,ensure_ascii=False,indent=2));print(label,flush=True)
  try:
   await page.goto('https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia',wait_until='domcontentloaded');await snap('base')
   await page.get_by_role('button',name=re.compile(r'^AI\s*\+\$79.99')).click();await snap('upgrade')
   await page.get_by_role('button',name='ADD TO CART',exact=True).click();await snap('added')
   await page.locator('a[href="/cart"]').first.click();await snap('client-cart')
   print('cart buttons',await page.locator('button').all_text_contents(),flush=True)
   plus=page.get_by_role('button',name=re.compile('increase|increment',re.I))
   if not await plus.count():plus=page.get_by_role('button',name='+',exact=True)
   if await plus.count():await plus.first.click();await snap('quantity-two')
   await page.reload(wait_until='domcontentloaded');await snap('reload-cart')
   checkout=page.locator('a[href*="checkout"]')
   if await checkout.count():await checkout.first.click()
   else:await page.goto('https://echobae.com/checkout',wait_until='domcontentloaded')
   await snap('checkout');await page.wait_for_timeout(15000);await snap('checkout-wait')
   await page.goto('https://echobae.com/cart',wait_until='domcontentloaded');await snap('return')
   remove=page.get_by_role('button',name=re.compile('remove',re.I))
   if await remove.count():await remove.first.click();await snap('removed')
  except Exception as e:out.append({'step':'error','error':str(e)});print(str(e),flush=True)
  (D/'cart-verify.json').write_text(json.dumps(out,ensure_ascii=False,indent=2));(D/'cart-network.json').write_text(json.dumps(net,indent=2));await b.close()
asyncio.run(main())
