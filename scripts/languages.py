"""Strict build-time translation: changed English copy requires a reviewed German entry.

No client-side translation, browser-language redirects, cookies or saved preference.
Both locales share layouts, identifiers, assets and source facts.
"""
from html import escape
from html.parser import HTMLParser
from pathlib import Path
import json
import posixpath
import re
from urllib.parse import urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[1]
SITE = 'https://amit-tech-datascience.github.io/Amit-Portfolio/'
CATALOG = ROOT/'scripts/de.json'
TRANSLATED_ATTRIBUTES = {'alt', 'aria-label', 'title'}

class GermanHTML(HTMLParser):
    def __init__(self, path, catalog, collect=False):
        super().__init__(convert_charrefs=True)
        self.path, self.catalog, self.collect = path, catalog, collect
        self.output, self.missing, self.strings = [], set(), set()

    def translate(self, value):
        text=value.strip()
        if not text or not any(c.isalpha() for c in text):
            # Decimal punctuation is visible text only; never alter URLs or geometry.
            return re.sub(r'(?<=\d)\.(?=\d)', ',', value)
        self.strings.add(text)
        if text not in self.catalog:
            self.missing.add(text)
            return value
        return value.replace(text, self.catalog[text], 1)

    def url(self, value):
        u=urlsplit(value)
        if u.scheme or u.netloc or not u.path: return value
        target=posixpath.normpath(posixpath.join(posixpath.dirname(self.path),u.path))
        if target.endswith('.html'): target='de/'+target
        new=posixpath.relpath(target,posixpath.dirname('de/'+self.path))
        return urlunsplit(('', '', new, u.query, u.fragment))

    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        for key,value in list(a.items()):
            if value is None: continue
            if key in TRANSLATED_ATTRIBUTES: a[key]=self.translate(value)
            if tag=='meta' and key=='content' and (a.get('name')=='description' or a.get('property') in {'og:title','og:description'}): a[key]=self.translate(value)
            if key in {'href','src'}: a[key]=self.url(value)
        if tag=='html': a['lang']='de'
        # The navigation's primary download follows the current page language.
        if tag=='a' and a.get('class')!='textlink' and a.get('href','').endswith('Amit-Amit-Resume-EN.pdf'):
            a['href']=a['href'].replace('Amit-Amit-Resume-EN.pdf','Amit-Amit-Lebenslauf-DE.pdf')
        self.output.append('<'+tag+''.join(' '+key+(f'="{escape(value,quote=True)}"' if value is not None else '') for key,value in a.items())+'>')

    def handle_startendtag(self,tag,attrs): self.handle_starttag(tag,attrs)
    def handle_endtag(self,tag): self.output.append('</'+tag+'>')
    def handle_data(self,data): self.output.append(escape(self.translate(data),quote=False))
    def handle_decl(self,decl): self.output.append('<!'+decl+'>')
    def handle_comment(self,data): self.output.append('<!--'+data+'-->')

def add_navigation(html,path,lang):
    current=('de/' if lang=='de' else '')+path
    en=posixpath.relpath(path,posixpath.dirname(current))
    de=posixpath.relpath('de/'+path,posixpath.dirname(current))
    label='Sprache: Deutsch' if lang=='de' else 'Language: English'
    menu=f'''<details class="language-menu"><summary>{label}</summary><div class="language-options"><a href="{en}" data-language="en" lang="en" hreflang="en"{' aria-current="true"' if lang=='en' else ''}>English</a><a href="{de}" data-language="de" lang="de" hreflang="de"{' aria-current="true"' if lang=='de' else ''}>Deutsch</a></div></details>'''
    html=html.replace('</nav></header>',menu+'</nav></header>')
    metadata=f'<link rel="canonical" href="{SITE+current}"><link rel="alternate" hreflang="en" href="{SITE+path}"><link rel="alternate" hreflang="de" href="{SITE}de/{path}"><link rel="alternate" hreflang="x-default" href="{SITE+path}"><meta property="og:locale" content="{"de_DE" if lang=="de" else "en_GB"}">'
    return html.replace('</head>',metadata+'</head>')

def render_languages(pages):
    catalog=json.loads(CATALOG.read_text(encoding='utf-8'))
    result={}
    missing=set()
    used=set()
    for path,html in pages.items():
        parser=GermanHTML(path,catalog)
        parser.feed(html)
        missing.update(parser.missing)
        used.update(parser.strings)
        result[path]=add_navigation(html,path,'en')
        result['de/'+path]=add_navigation(''.join(parser.output),path,'de')
    if missing: raise ValueError('German translations missing; update scripts/de.json before building:\n'+ '\n'.join(sorted(missing)))
    obsolete=set(catalog)-used
    empty=[key for key,value in catalog.items() if not isinstance(value,str) or not value.strip()]
    if obsolete or empty: raise ValueError(f'Clean up German catalogue. Obsolete: {sorted(obsolete)!r}; empty: {empty!r}')
    return result
