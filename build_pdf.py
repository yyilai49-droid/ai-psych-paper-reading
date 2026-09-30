from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, Frame, KeepTogether, PageBreak, Paragraph, Spacer,
    Table, TableStyle,
)

OUT = Path(__file__).parent.parent / "output" / "pdf" / "AI辅助阅读心理学论文_陶昱安_BSU心理学院.pdf"
FONT = r"C:\Windows\Fonts\msyh.ttc"
pdfmetrics.registerFont(TTFont("MSYH", FONT, subfontIndex=0))
pdfmetrics.registerFont(TTFont("MSYH-Bold", r"C:\Windows\Fonts\msyhbd.ttc", subfontIndex=0))

INK = colors.HexColor("#13203B")
CYAN = colors.HexColor("#087F79")
MINT = colors.HexColor("#DFF5F2")
CORAL = colors.HexColor("#EF7557")
VIOLET = colors.HexColor("#7D68DC")
PALE = colors.HexColor("#F6F8FC")
LINE = colors.HexColor("#DFE5F0")
MUTED = colors.HexColor("#667089")


def p(text, style):
    return Paragraph(text, style)


styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="TitleCN", fontName="MSYH-Bold", fontSize=28, leading=38, textColor=INK, spaceAfter=14))
styles.add(ParagraphStyle(name="Subtitle", fontName="MSYH", fontSize=11.5, leading=18, textColor=MUTED, spaceAfter=20))
styles.add(ParagraphStyle(name="H1CN", fontName="MSYH-Bold", fontSize=19, leading=27, textColor=INK, spaceBefore=10, spaceAfter=10))
styles.add(ParagraphStyle(name="H2CN", fontName="MSYH-Bold", fontSize=13.2, leading=19, textColor=INK, spaceAfter=6))
styles.add(ParagraphStyle(name="BodyCN", fontName="MSYH", fontSize=10.2, leading=17, textColor=INK, spaceAfter=8))
styles.add(ParagraphStyle(name="SmallCN", fontName="MSYH", fontSize=8.6, leading=13, textColor=MUTED))
styles.add(ParagraphStyle(name="PromptCN", fontName="MSYH", fontSize=9.1, leading=15, textColor=INK))
styles.add(ParagraphStyle(name="Kicker", fontName="MSYH-Bold", fontSize=8.5, leading=12, textColor=CYAN, spaceAfter=6))


def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(LINE)
    canvas.line(20 * mm, 282 * mm, 190 * mm, 282 * mm)
    canvas.setFont("MSYH-Bold", 8.6)
    canvas.setFillColor(INK)
    canvas.drawString(20 * mm, 286.4 * mm, "AI × 心理学论文阅读")
    canvas.setFillColor(CORAL)
    canvas.circle(16.5 * mm, 288.5 * mm, 1.5 * mm, fill=1, stroke=0)
    canvas.setStrokeColor(LINE)
    canvas.line(20 * mm, 15 * mm, 190 * mm, 15 * mm)
    canvas.setFont("MSYH", 8)
    canvas.setFillColor(MUTED)
    canvas.drawString(20 * mm, 9.5 * mm, "陶昱安 · BSU 心理学院")
    canvas.drawRightString(190 * mm, 9.5 * mm, f"第 {doc.page} 页")
    canvas.restoreState()


def section_label(text):
    return p(text, styles["Kicker"])


def info_box(title, content, accent=CYAN):
    title_p = ParagraphStyle("box-title", parent=styles["H2CN"], textColor=accent, spaceAfter=4)
    table = Table([[p(title, title_p)], [p(content, styles["BodyCN"])]], colWidths=[170 * mm])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.white),
        ("BOX", (0, 0), (-1, -1), 0.8, LINE),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
    ]))
    return table


story = []
story += [Spacer(1, 24 * mm), section_label("BSU PSYCHOLOGY · RESEARCH LITERACY"), p("让 AI 帮你读懂心理学论文，<br/>但不替你下结论。", styles["TitleCN"]), p("一份面向心理学实证研究、综述、元分析与实验报告的 AI 辅助阅读指南。AI 可以帮助定位、重组、追问与对照；研究者仍需判断设计质量、证据强度与结论边界。", styles["Subtitle"])]
hero = Table([[p("<b>使用原则</b><br/>每一句摘要都要能回到原文；每个解释都要与结果分开；每一项 AI 输出都视为待核对的工作草稿。", styles["BodyCN"]), p("<b>适用范围</b><br/>首读一篇论文、制作组会汇报、形成文献笔记、为综述或开题积累可追溯证据。", styles["BodyCN"])]], colWidths=[83 * mm, 83 * mm], hAlign="LEFT")
hero.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), MINT), ("BOX", (0, 0), (-1, -1), 0.5, MINT), ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.white), ("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 12), ("RIGHTPADDING", (0, 0), (-1, -1), 12), ("TOPPADDING", (0, 0), (-1, -1), 13), ("BOTTOMPADDING", (0, 0), (-1, -1), 13)]))
story += [hero, Spacer(1, 20 * mm), p("核心观点", styles["H1CN"]), p("AI 的最佳角色是“认知支架”，而不是“结论机器”。先明确需要它完成的是定位、解释、比较还是批判，再提出可追溯的问题。", styles["BodyCN"]), info_box("三条工作规则", "<b>证据可追溯：</b>要求页码、段落、图号或表号。<br/><b>事实与推断分开：</b>结果、作者解释、你的外推分别记录。<br/><b>保留人的判断：</b>摘要、方法、主要图表和局限性必须亲自核查。", VIOLET), PageBreak()]

story += [section_label("WORKFLOW"), p("五步，把“读过”变成“读懂”。", styles["H1CN"]), p("建议用 30–45 分钟完成一篇实证论文的首读。不要一上来就要求 AI “总结全文”。", styles["Subtitle"])]
steps = [
    ("1", "画出研究地图", "提取研究问题、理论依据、样本、设计、变量操作化、统计方法与作者的核心假设。"),
    ("2", "说清理论链条", "追问作者为什么预期 A 会影响 B。区分既有证据、作者假设与未被直接检验的环节。"),
    ("3", "锁定关键证据", "围绕每一个结论，定位图表、效应量、区间、统计模型与稳健性分析。"),
    ("4", "反向质询", "要求 AI 扮演审稿人，检查替代解释、样本、测量、因果推断与外部效度。"),
    ("5", "形成可复用笔记", "以“主张—证据—限制—我的问题”四栏记录，留下可用于综述、开题和汇报的材料。"),
]
for n, head, body in steps:
    row = Table([[p(n, ParagraphStyle("n", parent=styles["H2CN"], textColor=colors.white, alignment=TA_CENTER)), p(head, styles["H2CN"]), p(body, styles["BodyCN"])]], colWidths=[12 * mm, 42 * mm, 112 * mm])
    row.setStyle(TableStyle([("BACKGROUND", (0, 0), (0, 0), VIOLET if int(n) % 2 else CYAN), ("BACKGROUND", (1, 0), (-1, 0), colors.white), ("BOX", (0, 0), (-1, -1), .6, LINE), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("LEFTPADDING", (0, 0), (-1, -1), 10), ("RIGHTPADDING", (0, 0), (-1, -1), 10), ("TOPPADDING", (0, 0), (-1, -1), 9), ("BOTTOMPADDING", (0, 0), (-1, -1), 8)]))
    story += [row, Spacer(1, 7 * mm)]
story += [PageBreak()]

story += [section_label("PROMPT LIBRARY"), p("四个提示词，覆盖首读最重要的任务。", styles["H1CN"]), p("将论文 PDF 或相关段落提供给 AI 后使用。务必把方括号中的内容替换为你的论文信息。", styles["Subtitle"])]
prompts = [
    ("研究设计地图", "请作为心理学研究方法助教，基于这篇论文，按“研究问题—理论依据—样本—设计—变量操作化—统计方法—核心结果—作者结论”整理。每项后标注原文页码或图表号；不确定处请明确写“原文未说明”。"),
    ("结果图表解读", "请只根据 Fig./Table [编号] 及其图注，说明：1）图中比较了什么；2）关键效应量、区间与方向；3）可以得出的直接结论；4）不能从该图直接推出的结论。请用中文回答。"),
    ("审稿人式质询", "请以心理学期刊审稿人的视角，评估该研究的内部效度、统计结论效度、构念效度与外部效度。每条批评必须对应具体的方法或结果细节，并区分“作者已处理”与“仍未解决”。"),
    ("形成组会表达", "请将本文整理为 5 分钟组会汇报提纲：研究空缺、研究问题、方法、三条核心结果、一个机制解释、两个局限性、一个与[我的研究主题]相关的问题。避免超出原文证据的表述。"),
]
for i, (head, prompt) in enumerate(prompts):
    story += [info_box(head, prompt, [CYAN, VIOLET, CORAL, CYAN][i]), Spacer(1, 8 * mm)]
story += [PageBreak()]

story += [section_label("EVIDENCE & SAFETY"), p("把 AI 输出放进证据表，而不是直接放进结论。", styles["H1CN"]), p("推荐用“主张—原文证据—边界”三栏，限制不经核查的过度概括。", styles["Subtitle"])]
data = [[p("主张", styles["H2CN"]), p("原文证据", styles["H2CN"]), p("边界", styles["H2CN"])], [p("干预降低焦虑", styles["BodyCN"]), p("主要分析、效应量、CI", styles["BodyCN"]), p("仅限该样本/时间点", styles["BodyCN"])], [p("机制是注意偏向", styles["BodyCN"]), p("中介分析或实验操纵？", styles["BodyCN"]), p("相关不能证明机制", styles["BodyCN"])], [p("可推广到临床人群", styles["BodyCN"]), p("样本构成与纳排标准", styles["BodyCN"]), p("需独立外部验证", styles["BodyCN"])]]
tbl = Table(data, colWidths=[54 * mm, 64 * mm, 48 * mm])
tbl.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), MINT), ("BACKGROUND", (0, 1), (-1, -1), colors.white), ("GRID", (0, 0), (-1, -1), .5, LINE), ("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 9), ("RIGHTPADDING", (0, 0), (-1, -1), 9), ("TOPPADDING", (0, 0), (-1, -1), 9), ("BOTTOMPADDING", (0, 0), (-1, -1), 9)]))
story += [tbl, Spacer(1, 14 * mm), info_box("AI 使用边界", "<b>不要上传：</b>含受试者身份信息、临床敏感信息或未公开数据的材料。<br/><b>不要相信：</b>未经 DOI、作者和期刊核验的 AI 生成参考文献。<br/><b>不要外包：</b>统计复现、诊断判断和研究伦理决策。", CORAL), Spacer(1, 14 * mm), p("引用或汇报前核查", styles["H1CN"]), p("□ 能用一句话说明研究问题与理论预测　□ 核对样本与纳排标准　□ 看过主要图表　□ 知道效应量及其不确定性　□ 区分结果、解释与推断　□ 记录至少一个替代解释", styles["BodyCN"]), Spacer(1, 10 * mm), p("陶昱安｜BSU 心理学院｜yyilai49-droid@users.noreply.github.com", styles["SmallCN"])]

doc = BaseDocTemplate(str(OUT), pagesize=A4, leftMargin=20 * mm, rightMargin=20 * mm, topMargin=23 * mm, bottomMargin=20 * mm)
doc.addPageTemplates([__import__('reportlab.platypus').platypus.PageTemplate(id="main", frames=[Frame(20 * mm, 20 * mm, 170 * mm, 258 * mm, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)], onPage=header_footer)])
doc.build(story)
print(OUT)
