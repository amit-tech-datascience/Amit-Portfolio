"""Check generated HTML navigation, assets and baseline accessibility."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1]

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path, self.ids, self.refs, self.errors = path, set(), [], []
        self.h1, self.main, self.title, self.lang = 0, 0, 0, False
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            if a['id'] in self.ids: self.errors.append('duplicate id: '+a['id'])
            self.ids.add(a['id'])
        if tag == 'html': self.lang = a.get('lang') == 'en'
        if tag == 'h1': self.h1 += 1
        if tag == 'main': self.main += 1
        if tag == 'title': self.title += 1
        if tag == 'img' and 'alt' not in a: self.errors.append('image lacks alt')
        if tag == 'svg' and a.get('role') == 'img' and not a.get('aria-label'): self.errors.append('SVG lacks label')
        for key in ('href', 'src'):
            if key in a: self.refs.append(a[key])

pages = {}
for path in [ROOT/'index.html', ROOT/'sources.html', *sorted((ROOT/'projects').glob('*.html'))]:
    page = Page(path)
    page.feed(path.read_text(encoding='utf-8'))
    assert page.h1 == page.main == page.title == 1, f'{path}: expected one h1, main, title'
    assert page.lang, f'{path}: missing language'
    pages[path.resolve()] = page
errors = []
for path, page in pages.items():
    errors.extend(f'{path.name}: {e}' for e in page.errors)
    for ref in page.refs:
        url = urlsplit(ref)
        if url.scheme or url.netloc: continue
        if url.path.startswith('/'): errors.append(f'{path.name}: root-absolute link {ref}')
        target = (path.parent / unquote(url.path)).resolve() if url.path else path
        if not target.is_relative_to(ROOT): errors.append(f'{path.name}: path escapes site {ref}')
        elif not target.exists(): errors.append(f'{path.name}: missing {ref}')
        elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
            errors.append(f'{path.name}: missing fragment {ref}')
assert len(pages) == 9, 'Expected homepage, sources, seven case studies'
assert not errors, '\n'.join(errors)
print(f'PASS: {len(pages)} pages; local links, fragments, assets, IDs, headings, landmarks and illustration labels.')
