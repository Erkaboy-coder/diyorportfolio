from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import KeepTogether, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "Diyorbek_Qadamboyev_CV.pdf"
FONT_DIR = Path("C:/Windows/Fonts")

pdfmetrics.registerFont(TTFont("CVRegular", str(FONT_DIR / "arial.ttf")))
pdfmetrics.registerFont(TTFont("CVBold", str(FONT_DIR / "arialbd.ttf")))

INK = colors.HexColor("#111827")
MUTED = colors.HexColor("#4B5563")
ACCENT = colors.HexColor("#4F46E5")
PALE = colors.HexColor("#EEF2FF")
LINE = colors.HexColor("#D1D5DB")

styles = getSampleStyleSheet()
base = ParagraphStyle("Base", fontName="CVRegular", fontSize=8.2, leading=11.2, textColor=MUTED)
small = ParagraphStyle("Small", parent=base, fontSize=7.4, leading=9.7)
name = ParagraphStyle("Name", fontName="CVBold", fontSize=24, leading=27, textColor=INK, spaceAfter=2)
role = ParagraphStyle("Role", fontName="CVBold", fontSize=11, leading=14, textColor=ACCENT, spaceAfter=5)
section = ParagraphStyle("Section", fontName="CVBold", fontSize=10.5, leading=13, textColor=INK, spaceBefore=7, spaceAfter=4)
heading = ParagraphStyle("Heading", fontName="CVBold", fontSize=8.8, leading=11, textColor=INK)
meta = ParagraphStyle("Meta", fontName="CVRegular", fontSize=7.2, leading=9, textColor=MUTED)
tag = ParagraphStyle("Tag", fontName="CVBold", fontSize=7, leading=9, textColor=ACCENT, alignment=TA_LEFT)


def P(text, style=base):
    return Paragraph(text, style)


def section_title(number, title):
    return KeepTogether([
        P(f'<font color="#4F46E5">{number}</font>  {title}', section),
        Table([[""]], colWidths=[174 * mm], rowHeights=[0.35 * mm],
              style=TableStyle([("BACKGROUND", (0, 0), (-1, -1), LINE)])),
        Spacer(1, 2.5 * mm),
    ])


doc = SimpleDocTemplate(
    str(OUTPUT), pagesize=A4, rightMargin=18 * mm, leftMargin=18 * mm,
    topMargin=14 * mm, bottomMargin=13 * mm,
    title="Diyorbek Qadamboyev — Java Backend Developer CV",
    author="Diyorbek Qadamboyev",
)

story = []

header_left = [
    P("Diyorbek Qadamboyev", name),
    P("JAVA BACKEND DEVELOPER", role),
    P("Spring Boot yordamida xavfsiz, tushunarli va kengaytiriladigan backend tizimlar yarataman. Real loyiha va jamoaviy development tajribasiga egaman.", base),
]
header_right = [
    P("Toshkent, O'zbekiston", small),
    P("+998 93 053 52 03", small),
    P("diyorbekqadamboyev.0208@gmail.com", small),
    P('<link href="https://t.me/Diyorbek_5203" color="#4F46E5">t.me/Diyorbek_5203</link>', small),
    P('<link href="https://github.com/DiyanQadamboyev" color="#4F46E5">github.com/DiyanQadamboyev</link>', small),
]
header = Table([[header_left, header_right]], colWidths=[113 * mm, 61 * mm], hAlign="LEFT")
header.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("BACKGROUND", (1, 0), (1, 0), PALE),
    ("BOX", (1, 0), (1, 0), 0.5, colors.HexColor("#C7D2FE")),
    ("LEFTPADDING", (0, 0), (0, 0), 0), ("RIGHTPADDING", (0, 0), (0, 0), 8),
    ("LEFTPADDING", (1, 0), (1, 0), 9), ("RIGHTPADDING", (1, 0), (1, 0), 7),
    ("TOPPADDING", (0, 0), (0, 0), 0), ("BOTTOMPADDING", (0, 0), (0, 0), 0),
    ("TOPPADDING", (1, 0), (1, 0), 7), ("BOTTOMPADDING", (1, 0), (1, 0), 7),
]))
story.extend([header, Spacer(1, 4 * mm)])

story.append(section_title("01.", "TAJRIBA"))
experience_head = Table([
    [P("Backend Developer — TenzorSoft IT Company", heading), P("Commercial experience", meta)],
], colWidths=[130 * mm, 44 * mm])
experience_head.setStyle(TableStyle([
    ("ALIGN", (1, 0), (1, 0), "RIGHT"), ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
    ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
]))
story.append(experience_head)
exp_items = [
    ("U-GAZ platformasi", "Metan zapravkalar uchun avtomatlashtirilgan platformaning backend modullari va API endpointlarini ishlab chiqdim, testdan o'tkazdim."),
    ("Real-time integratsiya", "WebSocket orqali backend eventlarini qayta ishlab, mijoz interfeysiga real vaqt rejimida yetkazish mexanizmlarini yaratdim."),
    ("Jamoaviy development", "GitLab branch, merge request, code review va CI/CD pipeline jarayonlarida professional jamoa bilan ishladim."),
    ("Navoiy Azot ichki tizimi", "Korxonaning avtomatlashtirilgan platformasi uchun backend servislarini ishlab chiqdim."),
]
exp_rows = []
for i in range(0, len(exp_items), 2):
    row = []
    for title, description in exp_items[i:i + 2]:
        row.append([P(title, heading), P(description, small)])
    exp_rows.append(row)
exp_table = Table(exp_rows, colWidths=[87 * mm, 87 * mm], hAlign="LEFT")
exp_table.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"), ("BOX", (0, 0), (-1, -1), 0.5, LINE),
    ("INNERGRID", (0, 0), (-1, -1), 0.35, LINE),
    ("LEFTPADDING", (0, 0), (-1, -1), 7), ("RIGHTPADDING", (0, 0), (-1, -1), 7),
    ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
]))
story.append(exp_table)

story.append(section_title("02.", "TEXNIK KO'NIKMALAR"))
skills = [
    ("BACKEND", "Java Core · OOP · SOLID · Spring Boot · Spring Security · Hibernate/JPA"),
    ("API & SECURITY", "REST API · JWT · OAuth2 · WebSocket · Swagger/OpenAPI · Exception Handling"),
    ("DATA & TOOLS", "PostgreSQL · SQL · DB Modeling · Git · GitLab CI/CD · Docker · Microservices"),
]
skill_table = Table([[P(a, tag), P(b, small)] for a, b in skills], colWidths=[33 * mm, 141 * mm])
skill_table.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"), ("BACKGROUND", (0, 0), (0, -1), PALE),
    ("BOX", (0, 0), (-1, -1), 0.5, LINE), ("INNERGRID", (0, 0), (-1, -1), 0.35, LINE),
    ("LEFTPADDING", (0, 0), (-1, -1), 6), ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
]))
story.append(skill_table)

story.append(section_title("03.", "LOYIHALAR"))
projects = [
    ("Hospital Admission System", "Spring Boot · Spring Security · PostgreSQL · AWS S3", "Bemorlarni qabul qilish tizimi: JWT autentifikatsiya, WebSocket xabarnomalar va AWS S3 fayl saqlash.", "github.com/DiyanQadamboyev/hospital_admission_project"),
    ("E-Commerce Backend", "Spring Boot · PostgreSQL · REST API", "Mahsulot, buyurtma va foydalanuvchilar uchun kengaytiriladigan API; rolga asoslangan kirish nazorati.", ""),
    ("StudyCenterApp", "Java · PostgreSQL", "O'quvchilar, balans, to'lov va to'lov tarixini boshqarish tizimi.", ""),
]
project_rows = []
for title, tech, description, link in projects:
    cells = [P(title, heading), P(tech, tag), P(description, small)]
    if link:
        cells.append(P(f'<link href="https://{link}" color="#4F46E5">{link}</link>', meta))
    project_rows.append([cells])
projects_table = Table(project_rows, colWidths=[174 * mm])
projects_table.setStyle(TableStyle([
    ("BOX", (0, 0), (-1, -1), 0.5, LINE), ("INNERGRID", (0, 0), (-1, -1), 0.35, LINE),
    ("LEFTPADDING", (0, 0), (-1, -1), 7), ("RIGHTPADDING", (0, 0), (-1, -1), 7),
    ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
]))
story.append(projects_table)

story.append(section_title("04.", "TA'LIM VA TILLAR"))
education = Table([
    [P("Toshkent davlat texnika universiteti", heading), P("Iqtisodiyot — Bakalavr · 2021–2025", small)],
    [P("PDP Academy", heading), P("Foundation → Java Core → Java Backend", small)],
    [P("Tillar", heading), P("O'zbek · Ingliz (B1) · Rus", small)],
], colWidths=[66 * mm, 108 * mm])
education.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"), ("BOX", (0, 0), (-1, -1), 0.5, LINE),
    ("INNERGRID", (0, 0), (-1, -1), 0.35, LINE),
    ("LEFTPADDING", (0, 0), (-1, -1), 6), ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
]))
story.append(education)

doc.build(story)
print(OUTPUT)
