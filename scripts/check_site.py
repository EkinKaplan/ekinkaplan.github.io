"""Check rendered local links, fragments, images and page metadata. No dependencies."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import sys

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.ids, self.errors = [], set(), []
        self.title = self.main = self.viewport = False
        self.h1 = 0
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            if a['id'] in self.ids: self.errors.append('duplicate id ' + a['id'])
            self.ids.add(a['id'])
        if tag == 'title': self.title = True
        if tag == 'main': self.main = True
        if tag == 'h1': self.h1 += 1
        if tag == 'meta' and a.get('name') == 'viewport': self.viewport = True
        if tag == 'img' and not a.get('alt'): self.errors.append('image missing alt text')
        if tag in ('a','link') and 'href' in a: self.links.append(a['href'])
        if tag in ('img','script') and 'src' in a: self.links.append(a['src'])

root = Path(sys.argv[1] if len(sys.argv)>1 else '_site').resolve()
pages = {}
for f in root.rglob('*.html'):
    parser = Page(); text = f.read_text(); parser.feed(text); pages[f] = parser
    if '{{' in text or '{%' in text: parser.errors.append('unrendered Liquid template')
    if not all((parser.title, parser.main, parser.viewport)): parser.errors.append('missing page metadata/landmarks')
    if parser.h1 != 1: parser.errors.append('expected exactly one h1')
errors = []
for f, parser in pages.items():
    errors += [f'{f.relative_to(root)}: {e}' for e in parser.errors]
    for link in parser.links:
        u = urlsplit(link)
        if u.scheme or u.netloc: continue
        if not u.path: target = f
        else:
            target = (root / unquote(u.path).lstrip('/') if u.path.startswith('/') else f.parent / unquote(u.path)).resolve()
            if target.is_dir(): target = target / 'index.html'
        if not target.exists(): errors.append(f'{f.relative_to(root)}: missing {link}')
        elif u.fragment and target in pages and unquote(u.fragment) not in pages[target].ids:
            errors.append(f'{f.relative_to(root)}: missing fragment {link}')
if not pages: errors.append('No built HTML pages found')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print(f'Passed: {len(pages)} pages; local links, fragments, assets, headings, metadata and image alt text.')
