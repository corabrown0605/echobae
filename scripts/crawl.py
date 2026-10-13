import urllib.request,urllib.parse,json,re,time,hashlib,concurrent.futures
from html.parser import HTMLParser
from pathlib import Path
BASE='https://echobae.com'; D=Path('evidence'); D.mkdir(exist_ok=True)
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.meta=[];self.canonical=[];self.images=[];self.headings=[];self.title='';self.text=[];self.schemas=[];self.active=[];self.ld=None
 def handle_starttag(self,t,attrs):
  a=dict(attrs)
  if t=='a' and a.get('href'):self.links.append(a['href'])
  if t=='meta':self.meta.append(a)
  if t=='link' and a.get('rel')=='canonical':self.canonical.append(a.get('href'))
  if t=='img':self.images.append(a)
  if t in ['title','h1','h2','h3']:self.active.append([t,''])
  if t=='script' and a.get('type')=='application/ld+json':self.ld=''
 def handle_data(self,d):
  if self.active:self.active[-1][1]+=d
  if self.ld is not None:self.ld+=d
  if d.strip():self.text.append(d.strip())
 def handle_endtag(self,t):
  if self.active and self.active[-1][0]==t:
   tag,value=self.active.pop();value=' '.join(value.split())
   if tag=='title':self.title=value
   else:self.headings.append([tag,value])
  if t=='script' and self.ld is not None:
   try:self.schemas.append(json.loads(self.ld))
   except Exception as e:self.schemas.append({'parseError':str(e),'raw':self.ld})
   self.ld=None

def fetch(url):
 start=time.time();key=hashlib.sha256(url.encode()).hexdigest()[:12]
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 EchobaeReadOnlyAudit/1.0','Accept-Encoding':'identity'})
  try:r=urllib.request.urlopen(req,timeout=30)
  except urllib.error.HTTPError as e:r=e
  with r: body=r.read();status=r.code;headers=dict(r.headers);final=r.url
  (D/'html'/f'{key}.html').write_bytes(body)
  p=Parser();p.feed(body.decode('utf-8',errors='replace'))
  return dict(url=url,final=final,status=status,seconds=round(time.time()-start,3),bytes=len(body),headers=headers,title=p.title,meta=p.meta,headings=p.headings,canonical=p.canonical,schemas=p.schemas,images=p.images,links=p.links,html=f'evidence/html/{key}.html')
 except Exception as e:return dict(url=url,error=str(e))
def normalized(href,current):
 u=urllib.parse.urlsplit(urllib.parse.urljoin(current,href))
 if u.hostname not in ['echobae.com','www.echobae.com'] or u.scheme not in ['http','https']:return None
 if any(s in u.path for s in ['/api/','/_nuxt/','logout','/media/']):return None
 if re.search(r'\.(webp|png|jpg|svg|pdf)$',u.path):return None
 return urllib.parse.urlunsplit(('https','echobae.com',u.path or '/',u.query,''))
out=json.loads((D/'crawl.json').read_text()) if (D/'crawl.json').exists() else [];seen={r['url'] for r in out};todo=[u for u in json.loads((D/'discovered.json').read_text()) if u not in seen] if (D/'discovered.json').exists() else [BASE+'/']
while todo and len(seen)<350:
 batch=[u for u in todo[:8] if u not in seen];todo=todo[8:];seen.update(batch)
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex: rows=list(ex.map(fetch,batch))
 for r in rows:
  out.append(r)
  for href in r.get('links',[]):
   u=normalized(href,r['url'])
   if u and u not in seen and u not in todo:todo.append(u)
 (D/'crawl.json').write_text(json.dumps(out,ensure_ascii=False,indent=2));(D/'discovered.json').write_text(json.dumps(sorted(seen|set(todo)),indent=2))
 print('checked',len(out),'pending',len(todo),flush=True)
print('done',len(out))
