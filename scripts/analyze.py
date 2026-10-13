import json,re,collections
from html.parser import HTMLParser
from pathlib import Path
class Text(HTMLParser):
 def __init__(self):super().__init__();self.skip=0;self.data=[]
 def handle_starttag(self,t,a):
  if t in ['script','style']:self.skip+=1
 def handle_endtag(self,t):
  if t in ['script','style']:self.skip=max(0,self.skip-1)
 def handle_data(self,d):
  if not self.skip and d.strip():self.data.append(d.strip())
rows=json.load(open('evidence/crawl.json'));out={}
for r in rows:
 p=Text();p.feed(Path(r['html']).read_text());out[r['url']]='\n'.join(p.data)
Path('evidence/page-text.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
for path in ['/shipping-policy','/return-refund-policy','/privacy-policy','/payment-method','/faq','/pages/help','/customer-reviews','/p/159cm-lifelike-silicone-sex-doll-lydia','/p/149cm-white-hair-silicone-doll-siwei']:
 print('\nPAGE',path);print(out['https://echobae.com'+path][:12000])
