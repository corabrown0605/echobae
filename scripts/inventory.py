import json,csv
from collections import Counter
from pathlib import Path
D=Path('evidence');rows=json.loads((D/'crawl.json').read_text());urls=json.loads((D/'discovered.json').read_text())
def kind(u):
 path=u.split('echobae.com')[-1]
 if path=='/':return '首页'
 if path.startswith('/p/'):return '商品详情'
 if path.startswith('/collections/') or path.startswith('/c/') or path.startswith('/products'):return '分类/列表/筛选'
 if path.startswith('/blog/') or path.startswith('/blogs/'):return '博客文章'
 if path.startswith('/blog'):return '博客列表/筛选'
 if path.startswith('/account'):return '账户'
 if path.startswith('/cart'):return '购物车'
 if path.startswith('/checkout'):return '结账'
 return '内容/政策/支持'
with open('URL_INVENTORY.csv','w',encoding='utf-8-sig',newline='') as f:
 w=csv.writer(f);w.writerow(['URL','页面类型','HTTP状态','Title','H1','Canonical','Robots','Schema类型','证据']);by={r['url']:r for r in rows}
 def types(s):
  if isinstance(s,list):return sum((types(x) for x in s),[])
  if isinstance(s,dict):return ([s['@type']] if '@type' in s else [])+types(s.get('@graph',[]))
  return []
 for u in urls:
  r=by.get(u,{});w.writerow([u,kind(u),r.get('status','未检查'),r.get('title',''),' | '.join(h[1] for h in r.get('headings',[]) if h[0]=='h1'),' | '.join(r.get('canonical',[])),' | '.join(m.get('content','') for m in r.get('meta',[]) if m.get('name')=='robots'),str(types(r.get('schemas',[]))),r.get('html','')])
Path('URL_INVENTORY.md').write_text('# URL 清单（公开链接发现，不代表后台全部 URL）\n\n发现 '+str(len(urls))+' 个 URL，完成基础检查 '+str(len(rows))+' 个。\n\n'+ '\n'.join('- '+k+'：'+str(v) for k,v in Counter(kind(u) for u in urls).items())+'\n\n完整清单见 [URL_INVENTORY.csv](URL_INVENTORY.csv)。\n\n'+ '\n'.join('- '+u for u in urls),encoding='utf-8')
print(len(urls),len(rows),Counter(kind(u) for u in urls))
