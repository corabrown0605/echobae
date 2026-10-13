import asyncio,json,hashlib
from pathlib import Path
from playwright.async_api import async_playwright
D=Path('evidence/browser')
paths=['/','/products','/collections/new-arrival','/collections/best-value','/collections/best-sellers','/p/159cm-lifelike-silicone-sex-doll-lydia','/p/149cm-white-hair-silicone-doll-siwei','/p/170cm-realistic-silicone-sex-doll-jiachen','/p/demo-sh-030','/blog','/blog/tpe-vs-silicone-sex-doll','/blog/what-are-the-most-realistic-sex-dolls','/blog/silicone-sex-doll-buying-guide','/custom-made','/contact-us','/pages/help','/customer-reviews','/shipping-policy','/return-refund-policy','/privacy-policy','/payment-method','/faq','/about-us','/sex-doll-care','/cart']
async def main():
 async with async_playwright() as p:
  browser=await p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);results=[]
  for device,size in [('desktop',{'width':1440,'height':900}),('mobile',{'width':390,'height':844}),('tablet',{'width':768,'height':1024})]:
   c=await browser.new_context(viewport=size,is_mobile=device=='mobile',has_touch=device!='desktop');page=await c.new_page()
   for path in paths if device!='tablet' else paths[:8]:
    key=hashlib.sha256(path.encode()).hexdigest()[:10];responses=[];failures=[];console=[];errors=[]
    await page.close();page=await c.new_page();page.on('response',lambda r:responses.append({'url':r.url,'status':r.status,'type':r.request.resource_type}));page.on('requestfailed',lambda r:failures.append({'url':r.url,'error':r.failure}));page.on('console',lambda m:console.append({'type':m.type,'text':m.text}) if m.type in ['error','warning'] else None);page.on('pageerror',lambda e:errors.append(str(e)))
    try:
     r=await page.goto('https://echobae.com'+path,wait_until='domcontentloaded',timeout=45000);await page.wait_for_timeout(1800)
     age=page.get_by_role('button',name='I am 18 or older',exact=True)
     if await age.count():
      await page.screenshot(path=str(D/f'{device}-{key}-age.png'));await age.click();await page.wait_for_timeout(500)
     await page.screenshot(path=str(D/f'{device}-{key}.png'))
     height=await page.evaluate('document.documentElement.scrollHeight')
     for y in range(0,min(height,22000),size['height']):await page.evaluate('(y)=>window.scrollTo(0,y)',y);await page.wait_for_timeout(80)
     await page.wait_for_timeout(600);await page.evaluate('window.scrollTo(0,0)')
     data=await page.evaluate('''()=>({title:document.title,text:document.body.innerText,headings:[...document.querySelectorAll('h1,h2,h3')].map(x=>({tag:x.tagName,text:x.textContent,visible:!!x.getClientRects().length})),canonical:[...document.querySelectorAll('link[rel="canonical"]')].map(x=>x.href),meta:[...document.querySelectorAll('meta')].map(x=>({name:x.name||x.getAttribute('property'),content:x.content})),images:[...document.images].map(x=>({url:x.currentSrc||x.src,alt:x.getAttribute('alt'),natural:[x.naturalWidth,x.naturalHeight],render:[x.getBoundingClientRect().width,x.getBoundingClientRect().height],loading:x.loading,srcset:x.srcset,sizes:x.sizes,fit:getComputedStyle(x).objectFit,position:getComputedStyle(x).objectPosition,fetchPriority:x.fetchPriority})),links:[...document.querySelectorAll('a[href]')].map(x=>({href:x.href,text:x.innerText,aria:x.getAttribute('aria-label')})),buttons:[...document.querySelectorAll('button')].map(x=>({text:x.innerText,aria:x.getAttribute('aria-label'),disabled:x.disabled})),inputs:[...document.querySelectorAll('input,select,textarea')].map(x=>({tag:x.tagName,type:x.type,name:x.name,placeholder:x.placeholder,required:x.required,options:x.tagName==='SELECT'?[...x.options].map(o=>o.text):undefined})),schemas:[...document.querySelectorAll('script[type="application/ld+json"]')].map(x=>x.textContent),overflow:document.documentElement.scrollWidth>innerWidth,resources:performance.getEntriesByType('resource').map(x=>({url:x.name,transfer:x.transferSize,decoded:x.decodedBodySize,duration:x.duration,initiator:x.initiatorType})),cookies:document.cookie.split(';').map(x=>x.split('=')[0].trim()).filter(Boolean),localStorageKeys:Object.keys(localStorage)})''')
     data.update(url=page.url,path=path,device=device,viewport=size,status=r.status,responses=responses,failures=failures,console=console,pageErrors=errors,screenshot=f'evidence/browser/{device}-{key}.png');results.append(data);print(device,path,r.status,flush=True)
    except Exception as e:results.append({'path':path,'device':device,'error':str(e)});print('ERROR',device,path,str(e),flush=True)
    (D/'deep.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
   await c.close()
  await browser.close()
asyncio.run(main())
