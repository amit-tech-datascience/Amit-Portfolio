"""Local PDF readability checks, not an ATS-vendor or AI-detector certification.

Optional development dependencies: reportlab, pypdf and pypdfium2.
Use --render DIR for visual review images. Never upload resumes to a scanner here.
"""
import argparse
from io import BytesIO
from pathlib import Path
import re
from pypdf import PdfReader
import pypdfium2 as pdfium
from reportlab.platypus import Paragraph
import build_resume as builder

def compact(text):
    return re.sub(r'\s+','',text)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--render',type=Path)
    args=parser.parse_args()
    builder.validate_translations()
    for language,path in builder.OUTPUTS.items():
        raw=path.read_bytes()
        reader=PdfReader(BytesIO(raw))
        assert not reader.is_encrypted, f'{path.name}: encrypted PDF'
        assert len(reader.pages)==2, f'{path.name}: expected two pages'
        assert len(raw)<2_500_000, f'{path.name}: exceeds Greenhouse documented parsing size limit'
        root=reader.trailer['/Root']
        assert root['/Lang']==('en-GB' if language=='en' else 'de-DE')
        assert '/OpenAction' not in root
        assert all(len(p.images)==0 for p in reader.pages), 'Resume must contain text, not scanned images'
        extracted=[p.extract_text() for p in reader.pages]
        assert extracted[0].startswith('Amit Amit\n'), 'Name must precede footer in reading order'
        assert extracted[1].startswith('Selected projects' if language=='en' else 'Ausgewählte Projekte')
        builder.LANGUAGE=language
        paragraphs=[p.getPlainText() for p in builder.build_story() if isinstance(p,Paragraph)]
        doc=pdfium.PdfDocument(raw)
        second=[]
        for i in range(len(doc)):
            page=doc[i]
            textpage=page.get_textpage()
            second.append(textpage.get_text_range())
            width,height=page.get_size()
            for c in range(textpage.count_chars()):
                left,bottom,right,top=textpage.get_charbox(c)
                assert left>=0 and right<=width+1 and bottom>=0 and top<=height+1, f'{path.name}: text outside page'
            textpage.close()
            if args.render:
                args.render.mkdir(parents=True,exist_ok=True)
                bitmap=page.render(scale=1.6)
                bitmap.to_pil().save(args.render/f'{language}-{i+1}.png')
                bitmap.close()
            page.close()
        doc.close()
        for engine,parts in [('pypdf',extracted),('PDFium',second)]:
            text='\n'.join(parts)
            assert '\ufffd' not in text and '\x00' not in text, f'{engine}: broken text encoding'
            normalized=compact(text)
            position=0
            for paragraph in paragraphs:
                expected=compact(paragraph)
                found=normalized.find(expected,position)
                assert found>=0,f'{path.name}, {engine}: missing or reordered paragraph: {paragraph[:80]}'
                position=found+len(expected)
            for expected in ['linkedin.com/in/amit-tech','amit-tech-datascience.github.io/Amit-Portfolio','github.com/amit-tech-datascience','github.com/ak06645','43/50','1/50','Python','SQL','PyTorch','TensorFlow']:
                assert compact(expected) in normalized, f'{engine}: missing {expected}'
            assert ('German: A2' if language=='en' else 'Deutsch: A2') in text
        annotations=[a.get_object() for p in reader.pages for a in p.get('/Annots',[])]
        assert len(annotations)==9
        for annotation in annotations:
            assert annotation['/A']['/S']=='/URI'
            assert annotation['/A']['/URI'].startswith('https://')
        print(f'PASS {language}: two pages, {len(raw)} bytes, every paragraph extracted in order by pypdf and PDFium; visible profile URLs, no scanned images, nine HTTPS links, correct language and page bounds.')

if __name__=='__main__':
    main()
