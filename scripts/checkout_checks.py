import asyncio,json,re
from pathlib import Path
from playwright.async_api import async_playwright
D=Path('evidence/browser');out=[]
async def main():
 async with async_playwright() as p:
  b=await p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);c=await b.new_context(viewport={'width':390,'height':844},is_mobile=True);page=await c.new_page()
  async def ready():
   await page.wait_for_timeout(4500)
   for sel in ['.age-gate__btn--primary','.mkt-popup__close']:
    l=page.locator(sel)
    if await l.count() and await l.first.is_visible():await l.first.click()
  async def snap(step):
   data=await page.evaluate('''()=>({url:location.href,text:document.body.innerText,links:[...document.querySelectorAll('a[href]')].map(x=>({href:x.href,text:x.innerText})),inputs:[...document.querySelectorAll('input,select')].map(x=>({tag:x.tagName,type:x.type,value:x.type==='email'||x.type==='tel'?'':x.value,placeholder:x.placeholder,required:x.required,options:x.tagName==='SELECT'?[...x.options].map(o=>({text:o.text,value:o.value})):null})),buttons:[...document.querySelectorAll('button')].map(x=>({text:x.innerText,disabled:x.disabled,aria:x.getAttribute('aria-label')}))})''');data['step']=step;out.append(data);await page.screenshot(path=str(D/f'checkout-{step}.png'));(D/'checkout-checks.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
  try:
   await page.goto('https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia',wait_until='domcontentloaded');await ready();await page.get_by_role('button',name='ADD TO CART',exact=True).click();await ready();await page.locator('a[href="/cart"]').first.click();await ready();await page.locator('a[href*="checkout"]').first.click();await ready();await snap('initial')
   selects=page.locator('select')
   for country in ['United States','Canada','Brazil']:
    opts=await selects.first.locator('option').evaluate_all('(xs)=>xs.map(x=>({text:x.text,value:x.value}))');option=next(o for o in opts if o['text']==country);await selects.first.select_option(option['value']);await page.wait_for_timeout(2000);await snap(country.replace(' ','-'))
   await ready();await page.get_by_role('button',name=re.compile('Use coupon')).click();await snap('coupon-open')
   # No order submit, personal information, payment, contact or subscription action is performed.
   link=page.locator('a[href="/cart"]')
   if await link.count():await link.first.click();await ready()
   remove=page.get_by_role('button',name=re.compile('remove',re.I))
   if await remove.count():await remove.first.click()
  except Exception as e:out.append({'step':'error','error':str(e)});print(str(e))
  await b.close();(D/'checkout-checks.json').write_text(json.dumps(out,ensure_ascii=False,indent=2));print([r['step'] for r in out])
asyncio.run(main())
