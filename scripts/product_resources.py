import json,urllib.request,urllib.parse
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
rows=json.load(open('evidence/crawl.json'));tests=[]
for r in rows:
 if '/p/' not in r['url']:continue
 imgs=[i for i in r['images'] if i.get('src') and not i['src'].startswith('data:') and 'Echobae.' not in i.get('alt','')]
 url=urllib.parse.urljoin(r['url'],imgs[0]['src']) if imgs else None;tests.append({'page':r['url'],'url':url})
def check(u):
 if not u:return {'status':'无可检测主图'}
 host=urllib.parse.urlsplit(u).hostname
 if host!='echobae.com':return {'status':'未请求：第三方或内部地址','host':host}
 try:
  with urllib.request.urlopen(urllib.request.Request(u,method='HEAD'),timeout=20) as r:return {'status':r.status,'headers':dict(r.headers),'method':'HEAD'}
 except Exception as e:return {'error':str(e),'method':'HEAD'}
urls=list(dict.fromkeys(t['url'] for t in tests))
with ThreadPoolExecutor(max_workers=4) as ex:results=dict(zip(urls,ex.map(check,urls)))
for t in tests:t.update(results[t['url']])
Path('evidence/product-main-resources.json').write_text(json.dumps(tests,ensure_ascii=False,indent=2));print('pages',len(tests),'unique',len(urls),'status',__import__('collections').Counter(str(t.get('status','error')) for t in tests))
