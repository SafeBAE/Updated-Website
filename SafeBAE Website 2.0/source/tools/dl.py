import os, sys, subprocess, json, time, urllib.parse
B='https://www.safebae.org/wp-content/uploads/'
paths = sys.argv[1:] if len(sys.argv)>1 else [l.strip() for l in sys.stdin if l.strip()]
for p in paths:
    url = p if p.startswith('http') else B+p
    fn = '/home/claude/raw/' + (p.replace('/','__') if not p.startswith('http') else urllib.parse.quote(p.split('//')[1].replace('/','__'),safe='._-'))
    if os.path.exists(fn) and os.path.getsize(fn)>1000: continue
    r = subprocess.run(['curl','-sS','-L','--max-time','60','-o',fn,'-w','%{http_code}',urllib.parse.quote(url,safe=':/?=&%')],capture_output=True,text=True)
    print(r.stdout, p, os.path.getsize(fn) if os.path.exists(fn) else 0)
    time.sleep(0.3)
