from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable
)

OUTPUT = "Portfolio/resume.pdf"

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=A4,
    rightMargin=17 * mm,
    leftMargin=17 * mm,
    topMargin=13 * mm,
    bottomMargin=13 * mm
)

navy = colors.HexColor("#17365D")
blue = colors.HexColor("#2874A6")
grey = colors.HexColor("#555555")

styles = getSampleStyleSheet()

name_style = ParagraphStyle(
    "Name",
    parent=styles["Title"],
    fontName="Helvetica-Bold",
    fontSize=21,
    leading=25,
    textColor=navy,
    alignment=TA_CENTER,
    spaceAfter=4
)

contact_style = ParagraphStyle(
    "Contact",
    parent=styles["Normal"],
    fontSize=8.5,
    leading=12,
    alignment=TA_CENTER,
    textColor=grey
)

heading_style = ParagraphStyle(
    "SectionHeading",
    parent=styles["Heading2"],
    fontName="Helvetica-Bold",
    fontSize=11,
    leading=14,
    textColor=blue,
    spaceBefore=8,
    spaceAfter=4
)

body_style = ParagraphStyle(
    "Body",
    parent=styles["BodyText"],
    fontName="Helvetica",
    fontSize=9,
    leading=12.5,
    textColor=colors.HexColor("#222222"),
    spaceAfter=3
)

bullet_style = ParagraphStyle(
    "Bullet",
    parent=body_style,
    leftIndent=12,
    firstLineIndent=-8,
    spaceAfter=2
)

story = []

story.append(Paragraph("SUMIT SHARMA", name_style))
story.append(Paragraph(
    'B.Tech Computer Science and Engineering<br/>'
    'Email: sumitsharma77705@gmail.com<br/>'
    '<link href="https://github.com/sumitsharma7777" '
    'color="#2874A6">GitHub</link> &nbsp;|&nbsp; '
    '<link href="https://www.linkedin.com/in/sumit-sharma-0aa379431/" '
    'color="#2874A6">LinkedIn</link>',
    contact_style
))
story.append(Spacer(1, 7))
story.append(HRFlowable(width="100%", thickness=1, color=navy))

def section(title, content):
    story.append(Paragraph(title, heading_style))
    story.append(Paragraph(content, body_style))

def bullet(content):
    story.append(Paragraph("&bull; " + content, bullet_style))

section(
    "CAREER OBJECTIVE",
    "Computer Science and Engineering student at K.R. Mangalam University, "
    "building practical skills in software development, programming, "
    "web technologies and problem-solving. Interested in developing "
    "reliable applications and growing as a full-stack developer."
)

section("EDUCATION", "")
story.append(Paragraph(
    "<b>B.Tech - Computer Science and Engineering</b><br/>"
    "K.R. Mangalam University",
    body_style
))

section("TECHNICAL SKILLS", "")
story.append(Paragraph(
    "<b>Programming:</b> Python, Java (learning)<br/>"
    "<b>Web Technologies:</b> HTML, CSS, JavaScript (learning)<br/>"
    "<b>Tools:</b> Git, GitHub, Visual Studio Code, macOS Terminal<br/>"
    "<b>Other:</b> Bash scripting, REST APIs, JSON, curl, jq",
    body_style
))

section("PROJECTS", "")
story.append(Paragraph(
    "<b>Developer Ecosystem Portfolio</b> | "
    '<link href="https://github.com/sumitsharma7777/DeveloperPortfolio" '
    'color="#2874A6">GitHub Repository</link>',
    body_style
))
bullet(
    "Organized academic and practical work in a structured GitHub repository."
)
bullet(
    "Created Bash scripts for system information and backup automation."
)
bullet(
    "Used REST APIs to retrieve GitHub profile information and sample "
    "JSONPlaceholder posts; validated JSON responses using jq."
)
bullet(
    "Documented system information, command outputs and a full-stack "
    "development learning roadmap."
)

section("CORE STRENGTHS", "")
story.append(Paragraph(
    "Willingness to learn &nbsp;|&nbsp; Problem-solving &nbsp;|&nbsp; "
    "Practical approach &nbsp;|&nbsp; Continuous improvement",
    body_style
))

section("CAREER INTEREST", "")
story.append(Paragraph(
    "Full-Stack Development, Software Engineering and Web Application Development",
    body_style
))

doc.build(story)
print(f"Resume created successfully: {OUTPUT}")
