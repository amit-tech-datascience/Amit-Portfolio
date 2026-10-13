"""Create the public two-page resume. Optional dependency: reportlab.

Only professional, publication-approved content belongs in this file.
The source application bundle and its personal records must remain private.
"""
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'assets' / 'Amit-Amit-Resume.pdf'
INK = colors.HexColor('#172e38')
TEAL = colors.HexColor('#116853')
MUTED = colors.HexColor('#52666f')
STYLES = {
    'name': ParagraphStyle('Name',fontName='Helvetica-Bold',fontSize=26,leading=30,textColor=colors.black,spaceAfter=5),
    'subtitle': ParagraphStyle('Subtitle',fontName='Helvetica',fontSize=12,leading=16,textColor=INK,spaceAfter=7),
    'contact': ParagraphStyle('Contact',fontName='Helvetica',fontSize=9,leading=13,textColor=MUTED,spaceAfter=11),
    'section': ParagraphStyle('Section',fontName='Helvetica-Bold',fontSize=11,leading=15,textColor=TEAL,spaceBefore=13,spaceAfter=7,keepWithNext=True),
    'body': ParagraphStyle('Body',fontName='Helvetica',fontSize=10,leading=13.8,textColor=INK,spaceAfter=6),
    'role': ParagraphStyle('Role',fontName='Helvetica-Bold',fontSize=10.2,leading=14,textColor=INK,spaceBefore=8,spaceAfter=2,keepWithNext=True),
    'meta': ParagraphStyle('Meta',fontName='Helvetica',fontSize=9,leading=12.2,textColor=MUTED,spaceAfter=4,keepWithNext=True),
    'bullet': ParagraphStyle('Bullet',fontName='Helvetica',fontSize=10,leading=13.5,textColor=INK,leftIndent=10,firstLineIndent=-8,spaceAfter=3),
}

def p(text,style='body'):
    return Paragraph(text,STYLES[style])

def entry(title,meta,bullets):
    return [p(title,'role'),p(meta,'meta'),*[p('- '+b,'bullet') for b in bullets]]

def footer(canvas,doc):
    canvas.saveState()
    canvas.setFont('Helvetica',8)
    canvas.setFillColor(MUTED)
    canvas.drawString(43,27,'Amit Amit | Public resume | Updated October 2026')
    canvas.drawRightString(A4[0]-43,27,f'{doc.page} / 2')
    canvas.restoreState()

def main():
    OUTPUT.parent.mkdir(exist_ok=True)
    story=[p('Amit Amit','name'),p('Data Scientist | Computer Vision and Applied AI','subtitle'),
      p('Gotha, Germany &nbsp; | &nbsp; <link href="https://www.linkedin.com/in/amit-tech/" color="#116853">linkedin.com/in/amit-tech</link><br/><link href="https://amit-tech-datascience.github.io/Amit-Portfolio/" color="#116853">Portfolio and case studies</link> &nbsp; | &nbsp; <link href="https://github.com/amit-tech-datascience" color="#116853">GitHub: amit-tech-datascience</link> &nbsp; | &nbsp; <link href="https://github.com/ak06645" color="#116853">Earlier work: ak06645</link>','contact'),
      p('Data Scientist at Sedeco Imaging working on camera-based detection, robotic handling and efficient edge deployment. M.Sc. in Data Science from TU Braunschweig, with research experience in scientific machine learning, biomedical data analysis and aerospace applications. Earlier experience in Linux infrastructure, automation and SQL reporting.'),
      p('Technical skills','section'),
      p('<b>Modeling:</b> PyTorch, TensorFlow/Keras, scikit-learn, OpenCV, anomaly detection, segmentation, physics-informed neural networks.<br/><b>Data and engineering:</b> Python, SQL, NumPy, Pandas, Git, Docker, Linux, Django, TypeScript/Next.js.<br/><b>Vision and edge:</b> OpenMV, Raspberry Pi, Luckfox, Hikrobot camera integration.'),
      p('Professional experience','section')]
    story+=entry('Data Scientist | Sedeco Imaging','Gotha, Germany | October 2025 - Present',[
      'Lead the technical design of bottle and can detection workflows and robotic separation using an FR5 arm.',
      'Develop camera-based vision components and deployment solutions for compact platforms including Luckfox, OpenMV and Raspberry Pi, alongside Hikrobot systems.'])
    story+=entry('Student Research Assistant | PLRI, TU Braunschweig','Braunschweig, Germany | November 2022 - September 2025',[
      'Analyzed multi-omics data using network-based methods for NetfLID; supported gene-gene interaction modeling for the Epistasis Disease Atlas.',
      'Built SVM models and visualizations for biomedical collaborators; supported Linux research infrastructure and contributed to an HPC cluster.'])
    story+=entry('Student Research Assistant | German Aerospace Center DLR','Braunschweig, Germany | November 2024 - June 2025',[
      'Developed CNN-based structural wear models using inspection images and environmental data for aircraft component lifecycle assessment.',
      'Investigated data provenance and blockchain approaches for lifecycle assessment; coauthored a conference contribution listed by DLR.'])
    story+=entry('Student Assistant | iBMB, TU Braunschweig','Braunschweig, Germany | March 2023 - November 2024',[
      'Prepared experimental data and developed predictive models, including Random Forests, for materials and fire-safety research.',
      'Built a Django application for internal experimental-data management and researcher access.'])
    story+=entry('Senior Systems Engineer | Infosys','Bengaluru, India | March 2019 - November 2021',[
      'Supported Linux and VMware infrastructure; used SQL for analysis and reporting and Python/Bash scripts for recurring operational tasks.'])
    story += [PageBreak(),p('Selected projects','section')]
    story+=entry('Industrial visual inspection | Personal research','2026 | Python, PyTorch, CUDA | <link href="https://amit-tech-datascience.github.io/Amit-Portfolio/projects/industrial-inspection.html" color="#116853">Case study and recorded examples</link>',[
      'Built a reproducible CLI for data preparation, normal-only calibration, prediction, evaluation and benchmarking; implemented a NumPy baseline and a GPU PatchCore variant.',
      'Compared preprocessing on a PCB2 development split: cropped 512 px input detected 43/50 defects with 1/50 false alarms, versus 36/50 and 3/50 for full-frame 256 px input.',
      'Documented weak transfer to a separate component dataset. Results are exploratory development evidence; an independent acceptance evaluation remains pending.'])
    story+=entry('Physics-informed neural networks | Master\'s thesis','2025 | TensorFlow, Hydra, scientific computing | <link href="https://github.com/muecke-math/Master-Amit-Amit" color="#116853">Repository</link>',[
      'Investigated PINN training for Helmholtz and Allen-Cahn equations using existing frameworks including TensorDiffEq and pinns-tf2.',
      'Implemented experiments exploring collocation, adaptive weighting and optimization, with saved solution, residual and error visualizations.'])
    story+=entry('Landslide segmentation | Collaborative academic project','2023 | UNet, Swin-based UNet, SegFormer | <link href="https://deep-learning-igp-tubs-sose2023.github.io/Group_C/" color="#116853">Team report</link>',[
      'Collaborated with Reiko Lettmoden on multispectral segmentation, comparing architectures, input bands, augmentation and imbalance-aware losses.',
      'The team report records F1 0.756 for augmented UNet with Lovasz loss versus 0.721 baseline, using a local split of a training subset, not the official benchmark test set.'])
    story+=entry('Additional applied AI and research projects','2022 - 2025 | <link href="https://amit-tech-datascience.github.io/Amit-Portfolio/" color="#116853">Portfolio archive</link>',[
      'Speech enhancement: CPC representations and HiFi-GAN in PyTorch; NISQA, PESQ and DNSMOS evaluation against an EffCRN baseline.',
      'Character AI application: Next.js/TypeScript, Express, MongoDB and OpenRouter integration. Earlier work includes equivariant leakage localization and water forecasting.'])
    story += [p('Education','section'),p('<b>M.Sc. Data Science | Technische Universit\u00e4t Braunschweig</b><br/>October 2021 - June 2025','body'),p('<b>B.Tech. Electronics and Communication Engineering</b><br/>Bharati Vidyapeeth\'s College of Engineering, New Delhi | August 2014 - June 2018','body'),
      p('Conference contribution','section'),p('Janko Kreikemeier, Amit Amit and Steffen Opitz. <i>Towards a Circular Future with Structural Life 2.0 and Blockchain-Approach.</i> World Symposium on Materials Sciences and Engineering, Singapore, December 2025. Conference speech; <link href="https://elib.dlr.de/220248/" color="#116853">DLR bibliographic record</link>.'),
      p('Languages','section'),p('English: C1 | German: A2')]
    doc=SimpleDocTemplate(str(OUTPUT),pagesize=A4,rightMargin=43,leftMargin=43,topMargin=35,bottomMargin=42,title='Amit Amit - Data Scientist Resume',author='Amit Amit',subject='Public professional resume',pageCompression=1)
    doc.build(story,onFirstPage=footer,onLaterPages=footer)
    print(OUTPUT)

if __name__=='__main__':
    main()
