import subprocess,concurrent.futures,json,time
from pathlib import Path
BIN='/workspace/echobae-audit/tools/node_modules/.bin/lighthouse'
pages={'home':'https://echobae.com/','collection':'https://echobae.com/collections/new-arrival','product':'https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia','article':'https://echobae.com/blog/tpe-vs-silicone-sex-doll'}
def run(task):
 name,url,device,n=task;out=Path('evidence/lighthouse')/f'{name}-{device}-{n}'
 cmd=[BIN,url,'--chrome-flags=--headless --no-sandbox','--output=json','--output=html',f'--output-path={out}','--quiet']
 if device=='desktop':cmd+=['--preset=desktop']
 start=time.time()
 try:
  r=subprocess.run(cmd,env={**__import__('os').environ,'CHROME_PATH':'/usr/bin/chromium'},capture_output=True,text=True,timeout=180)
  result={'page':name,'url':url,'device':device,'run':n,'exit':r.returncode,'seconds':time.time()-start,'stderr':r.stderr};out.with_suffix('.log').write_text(json.dumps(result,indent=2));print(name,device,n,'exit',r.returncode,flush=True);return result
 except Exception as e:print(task,str(e),flush=True);return {'page':name,'device':device,'run':n,'error':str(e)}
tasks=[(name,url,device,n) for name,url in pages.items() for device in ['mobile','desktop'] for n in [1,2,3]]
# Sequential runs avoid concurrent Chromium contention; trace collection is retained in Lighthouse reports.
results=[run(task) for task in tasks]
Path('evidence/lighthouse/runs.json').write_text(json.dumps(results,indent=2))
