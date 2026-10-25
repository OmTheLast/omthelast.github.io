#!/usr/bin/env python3
"""Check the static portfolio, without downloading model weights or running demos."""
import argparse
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import subprocess
from urllib.parse import urljoin, urlparse, unquote
from concurrent.futures import ThreadPoolExecutor

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = 'https://ompatnaik.com'

class Document(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.ids, self.links, self.errors = set(), [], []
        self.h1 = self.main = 0
        self.description = self.canonical = self.og_image = False
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            if a['id'] in self.ids: self.errors.append('duplicate id: '+a['id'])
            self.ids.add(a['id'])
        if tag == 'h1': self.h1 += 1
        if tag == 'main': self.main += 1
        if tag == 'meta' and a.get('name') == 'description': self.description = bool(a.get('content'))
        if tag == 'meta' and a.get('property') == 'og:image': self.og_image = bool(a.get('content'))
        if tag == 'link' and a.get('rel') == 'canonical': self.canonical = bool(a.get('href'))
        if tag == 'img' and not all(a.get(k) for k in ('alt','width','height')):
            self.errors.append('image missing alt text or dimensions')
        if tag == 'a' and a.get('target') == '_blank' and not ('noopener' in a.get('rel','') or 'noreferrer' in a.get('rel','')):
            self.errors.append('unsafe new-tab link')
        key = 'href' if tag in ('a','link') else 'src' if tag in ('img','script') else None
        if key and a.get(key) and a.get('rel') not in ('preconnect','dns-prefetch'):
            self.links.append(a[key])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--external', action='store_true', help='GET linked external URLs, following redirects')
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    files = [ROOT/'index.html', ROOT/'projects.html'] + [ROOT/x/'index.html' for x in ('jee','tokenizers','hinglish')] + sorted((ROOT/'projects').glob('*/index.html'))
    docs = {f:Document(f) for f in files}
    errors, external, count = [], set(), 0
    for f,d in docs.items():
        errors.extend(f'{f.relative_to(ROOT)}: {e}' for e in d.errors)
        if not (d.h1 == d.main == 1 and d.description and d.canonical and d.og_image):
            errors.append(str(f.relative_to(ROOT))+': missing document structure or metadata')
        for href in d.links:
            if href.startswith('mailto:'): continue
            u = urlparse(urljoin(ORIGIN+'/'+str(f.relative_to(ROOT)),href))
            target = ROOT/unquote(u.path.lstrip('/'))
            if target.is_dir(): target /= 'index.html'
            # Separately deployed project apps on the same custom domain are external to this checkout.
            if u.netloc != 'ompatnaik.com' or (href.startswith('https://') and not target.exists()):
                external.add(u._replace(fragment='').geturl()); continue
            count += 1
            if not target.is_file(): errors.append(f'{f.relative_to(ROOT)}: broken local link {href}')
            elif u.fragment and target.suffix == '.html':
                dest = docs.get(target) or Document(target)
                if unquote(u.fragment) not in dest.ids: errors.append(f'{f.relative_to(ROOT)}: missing anchor {href}')
    for item in json.loads((ROOT/'assets/research/sources.json').read_text()):
        path=ROOT/'assets/research'/item['file']
        if hashlib.sha256(path.read_bytes()).hexdigest() != item['sha256']:
            errors.append('changed source figure: '+item['file'])
    if (ROOT/'CNAME').read_text().strip() != 'ompatnaik.com': errors.append('CNAME changed')
    deployment = json.loads((ROOT/'llamajee/deployment.json').read_text())
    for name, expected in deployment['sha256'].items():
        if hashlib.sha256((ROOT/'llamajee'/name).read_bytes()).hexdigest() != expected:
            errors.append('solver deployment hash mismatch: '+name)
    results=[]
    if args.external:
        def check(url):
            p=subprocess.run(['curl','--silent','--show-error','--location','--max-time','30','--retry','1','--output','/dev/null','--write-out','%{http_code} %{url_effective}',url],capture_output=True,text=True)
            code,_,final=p.stdout.partition(' ')
            return {'url':url,'status':int(code or '0'),'final':final,'error':p.stderr.strip()}
        with ThreadPoolExecutor(max_workers=5) as pool: results=list(pool.map(check,sorted(external)))
        errors.extend(f"External HTTP {r['status']}: {r['url']}" for r in results if not 200<=r['status']<400)
    report={'pages':len(files),'local_references':count,'external_urls':len(external),'external_results':results,'errors':errors}
    if args.report: args.report.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='external_results'},indent=2))
    raise SystemExit(bool(errors))

if __name__ == '__main__': main()
