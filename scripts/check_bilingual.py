"""Regression checks for language routing, content parity and translation coverage."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import json
from build import build_home, build_case, sources_page, PROJECTS
from languages import GermanHTML, render_languages, ROOT

class Inspect(HTMLParser):
    def __init__(self,html):
        super().__init__(); self.tags=[]; self.text=[];self.feed(html)
    def handle_starttag(self,tag,attrs): self.tags.append((tag,dict(attrs)))
    def handle_data(self,text): self.text.append(text)

source={'index.html':build_home(),'sources.html':sources_page()}
source.update({f"projects/{p['slug']}.html":build_case(p) for p in PROJECTS})
rendered=render_languages(source)
for path,expected in rendered.items():
    actual=(ROOT/path).read_text(encoding='utf-8')
    assert actual==expected, f'Stale generated page: {path}; run build.py'
    de=path.startswith('de/')
    p=Inspect(actual)
    lang='de' if de else 'en'
    counterpart=path[3:] if de else 'de/'+path
    menus=[a for tag,a in p.tags if tag=='a' and 'data-language' in a]
    assert len(menus)==2, f'{path}: both language choices required'
    for a in menus:
        dest=((ROOT/path).parent/urlsplit(a['href']).path).resolve()
        expected_path=ROOT/(path if a['data-language']==lang else counterpart)
        assert dest==expected_path.resolve(), f'{path}: wrong counterpart {a}'
        assert a['hreflang']==a['lang']==a['data-language']
        assert (a.get('aria-current')=='true')==(a['data-language']==lang)
    alternates={a.get('hreflang'):a['href'] for tag,a in p.tags if tag=='link' and a.get('rel')=='alternate'}
    assert set(alternates)=={'en','de','x-default'}
    assert alternates['x-default']==alternates['en']
    assert '/de/' not in alternates['en']
    for tag,a in p.tags:
        if tag=='a' and 'data-language' not in a:
            u=urlsplit(a.get('href',''))
            if not u.scheme and u.path.endswith('.html'):
                dest=((ROOT/path).parent/u.path).resolve()
                assert dest.is_relative_to(ROOT/'de')==de, f'{path}: internal link changes language'
        if tag=='a' and a.get('class')=='resume-link':
            assert a['href'].endswith('Lebenslauf-DE.pdf' if de else 'Resume-EN.pdf')
    text=' '.join(p.text)
    if path.endswith('index.html'):
        assert 'Resume-EN.pdf' in actual and 'Lebenslauf-DE.pdf' in actual
        assert ('Deutsch (A2)' if de else 'German (A2)') in text
    if '/projects/' in '/'+path:
        has_pcb_table=any('Recorded PCB2' in text or 'Dokumentierte PCB2' in text for text in p.text)
        assert has_pcb_table==path.endswith('/industrial-inspection.html'), f'{path}: unrelated PCB results'
        if path.endswith('/industrial-inspection.html'):
            for key in ['example-detected','example-missed','example-false-alarm']:
                assert any(a.get('id')==key for tag,a in p.tags)
            assert ('2,514928' if de else '2.514928') in text

# A future edit must never silently publish untranslated German body text or alt text.
catalog=json.loads((ROOT/'scripts/de.json').read_text(encoding='utf-8'))
probe=GermanHTML('index.html',catalog)
probe.feed('<p>New untranslated project description</p><img alt="New untranslated image label">')
assert probe.missing=={'New untranslated project description','New untranslated image label'}
js=(ROOT/'assets/site.js').read_text(encoding='utf-8')
assert all(s not in js for s in ['localStorage','sessionStorage','navigator.language','document.cookie'])
print('PASS: 20 current bilingual pages; counterpart links, locale-preserving navigation, English default, language-labelled PDF targets, gallery values and strict translation coverage.')
