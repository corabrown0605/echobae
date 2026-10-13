import asyncio,json
from pathlib import Path
from playwright.async_api import async_playwright
async def main():
 async with async_playwright() as p:
  b=await p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);c=await b.new_context(viewport={'width':390,'height':844},is_mobile=True);page=await c.new_page();out=[]
  for path in ['/search?q=silicone','/search?q=Lydia','/search?q=audit-no-result-20261013','/p/audit-nonexistent-20261013','/checkout','/products?tag=smart-home','/products?tag=bestseller']:
   r=await page.goto('https://echobae.com'+path,wait_until='domcontentloaded');await page.wait_for_timeout(2400)
   data=await page.evaluate('''()=>({url:location.href,text:document.body.innerText,inputs:[...document.querySelectorAll('input,select')].map(x=>({tag:x.tagName,name:x.name,type:x.type,placeholder:x.placeholder,options:x.tagName==='SELECT'?[...x.options].map(o=>({value:o.value,text:o.text})):undefined})),buttons:[...document.querySelectorAll('button')].map(x=>({text:x.innerText,aria:x.getAttribute('aria-label')})),links:[...document.querySelectorAll('a[href]')].map(x=>({href:x.href,text:x.innerText}))})''');data['status']=r.status;out.append(data)
  await b.close();Path('evidence/browser/search-checks.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
asyncio.run(main())
