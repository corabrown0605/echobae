import asyncio,json
from pathlib import Path
from playwright.async_api import async_playwright
async def main():
 async with async_playwright() as p:
  b=await p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);c=await b.new_context(viewport={'width':1440,'height':900});page=await c.new_page();out=[]
  for path in ['/products','/collections/new-arrival','/collections/best-value','/collections/best-sellers','/blog','/custom-made']:
   try:
    r=await page.goto('https://echobae.com'+path,wait_until='domcontentloaded',timeout=45000);await page.wait_for_timeout(2000)
    if await page.get_by_role('button',name='I am 18 or older',exact=True).count():await page.get_by_role('button',name='I am 18 or older',exact=True).click()
    data=await page.evaluate('''()=>({url:location.href,title:document.title,text:document.body.innerText,links:[...document.querySelectorAll('a[href]')].map(x=>({href:x.href,text:x.innerText})),buttons:[...document.querySelectorAll('button')].map(x=>x.innerText),inputs:[...document.querySelectorAll('input')].map(x=>({type:x.type,placeholder:x.placeholder,name:x.name}))})''');data['status']=r.status;out.append(data)
   except Exception as e:out.append({'path':path,'error':str(e)})
  await b.close();Path('evidence/browser-discovery.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
asyncio.run(main())
