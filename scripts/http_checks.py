import json,urllib.request,urllib.error
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
urls=['http://echobae.com/','https://www.echobae.com/','http://www.echobae.com/','https://echobae.com/robots.txt','https://echobae.com/sitemap.xml','https://echobae.com/audit-nonexistent-20261013','https://echobae.com/p/audit-nonexistent-20261013','https://echobae.com/api/v1/content/runtime-blocks','https://echobae.com/search?q=silicone','https://echobae.com/search?q=audit-no-result-20261013','https://echobae.com/checkout','https://echobae.com/terms-and-conditions']
class NoRedirect(urllib.request.HTTPRedirectHandler):
 def redirect_request(self,*a):return None
def fetch(u):
 try:
  try:r=urllib.request.build_opener(NoRedirect).open(u,timeout=25)
  except urllib.error.HTTPError as e:r=e
  with r:body=r.read();data={'url':u,'status':r.code,'headers':dict(r.headers),'body':body.decode('utf-8',errors='replace')[:150000]}
  return data
 except Exception as e:return {'url':u,'error':str(e)}
with ThreadPoolExecutor(max_workers=3) as ex:out=list(ex.map(fetch,urls))
# Googlebot UA checks are requests with a spoofed UA, not proof of verified Googlebot access.
for u in ['https://echobae.com/','https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia']:
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Googlebot/2.1 (+http://www.google.com/bot.html)'}),timeout=25) as r:out.append({'url':u,'ua':'Googlebot (spoofed)','status':r.status,'bytes':len(r.read())})
 except Exception as e:out.append({'url':u,'ua':'Googlebot (spoofed)','error':str(e)})
Path('evidence/http-checks.json').write_text(json.dumps(out,ensure_ascii=False,indent=2));print([(x['url'],x.get('status'),x.get('headers',{}).get('location'),x.get('error')) for x in out])
