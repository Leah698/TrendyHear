#!/usr/bin/env python3
import argparse,json,pathlib,shutil,subprocess,tempfile,time,urllib.request
p=argparse.ArgumentParser();p.add_argument('--octo',required=True);p.add_argument('--port',type=int,default=8490);args=p.parse_args()
root=pathlib.Path(__file__).resolve().parents[1]
work=pathlib.Path(tempfile.mkdtemp(prefix='trendyhear-091-checks-'))
shutil.copytree(root/'bundle',work/'bundle')
main=(root/'bundle/main.splash').read_text();needle='start_timeout(0.05,|| boot())'
assert main.count(needle)==1
(work/'bundle/main.splash').write_text(main.replace(needle,(root/'tests/decisions-0.9.1.splash').read_text()))
manifest=json.loads((root/'bundle/manifest.json').read_text());manifest['agent']=None;manifest['requires']=[];manifest.pop('host_api',None)
manifest['integrity']={'bundle_blake3':''}
(work/'bundle/manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
# Refuse an occupied port rather than interact with another window.
import socket
with socket.socket() as probe: probe.bind(('127.0.0.1',args.port))
log=(work/'runtime.log').open('w')
process=subprocess.Popen([args.octo,'run',str(work/'bundle'),'--port',str(args.port),'--app-data',str(work/'state'),'--hidden'],stdout=log,stderr=subprocess.STDOUT)
result=work/'state/skystream.trendyhear/checks-091.json'
try:
 deadline=time.monotonic()+45
 while not result.exists() and time.monotonic()<deadline and process.poll() is None:time.sleep(.2)
 if not result.exists():raise RuntimeError('No results; inspect '+str(work/'runtime.log'))
 checks=json.loads(result.read_text());print(json.dumps(checks,ensure_ascii=False,indent=2));print('Evidence:',work)
 if not all(v is True for v in checks.values()):raise RuntimeError('A native check failed')
finally:
 if process.poll() is None:
  try:urllib.request.urlopen(f'http://127.0.0.1:{args.port}/quit',timeout=3).read()
  except Exception:process.terminate()
  try:process.wait(timeout=5)
  except subprocess.TimeoutExpired:process.kill()
 log.close()
