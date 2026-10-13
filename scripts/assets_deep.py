import json,urllib.request,io,hashlib
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from PIL import Image
D=Path('evidence');rows=json.load(open(D/'browser/deep.json'));urls=[]
for r in rows:
 if r.get('device')!='desktop':continue
 for x in r.get('images',[])[:6]:
  if x['url'].startswith('https://echobae.com/') and x['url'] not in urls:urls.append(x['url'])
for r in rows[:1]:
 for x in r.get('resources',[]):
  if x['initiator'] in ['script','link','css'] and x['url'].startswith('https://echobae.com/') and x['url'] not in urls:urls.append(x['url'])
def fetch(u):
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'Accept-Encoding':'gzip, br'}),timeout=25) as r:data=r.read();out={'url':u,'status':r.status,'bytes':len(data),'headers':dict(r.headers)}
  try:
   im=Image.open(io.BytesIO(data));out.update(dimensions=list(im.size),format=im.format)
  except Exception:pass
  return out
 except Exception as e:return {'url':u,'error':str(e)}
with ThreadPoolExecutor(max_workers=4) as ex:out=list(ex.map(fetch,urls))
(D/'assets-deep.json').write_text(json.dumps(out,indent=2));print('resources',len(out),'failed',sum('error' in r for r in out));print('large',sorted([(r['url'],r.get('bytes',0),r.get('dimensions')) for r in out],key=lambda x:x[1],reverse=True)[:8])
