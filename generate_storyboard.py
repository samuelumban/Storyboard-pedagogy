"""
Storyboard Template Generator
Kementerian Agama Republik Indonesia - Ditjen Bimas Kristen
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate, Table, TableStyle, Paragraph,
    Spacer, HRFlowable, KeepTogether
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT

PAGE_W, PAGE_H = A4
MARGIN_L = 20 * mm
MARGIN_R = 20 * mm
MARGIN_T = 15 * mm
MARGIN_B = 15 * mm
CONTENT_W = PAGE_W - MARGIN_L - MARGIN_R

BLACK = colors.black
WHITE = colors.white

def make_styles():
    return dict(
        inst_bold = ParagraphStyle("IB",
            fontName="Helvetica-Bold", fontSize=13, leading=16, alignment=TA_CENTER),
        inst_sub  = ParagraphStyle("IS",
            fontName="Helvetica-Bold", fontSize=9,  leading=12, alignment=TA_CENTER),
        inst_addr = ParagraphStyle("IA",
            fontName="Helvetica",      fontSize=8,  leading=10, alignment=TA_CENTER),
        label     = ParagraphStyle("L",
            fontName="Helvetica",      fontSize=8,  leading=10, alignment=TA_LEFT),
        label_bold= ParagraphStyle("LB",
            fontName="Helvetica-Bold", fontSize=8,  leading=10, alignment=TA_LEFT),
        cell_sm   = ParagraphStyle("CS",
            fontName="Helvetica",      fontSize=7.5,leading=10, alignment=TA_LEFT),
        center_sm = ParagraphStyle("CSM",
            fontName="Helvetica-Bold", fontSize=8,  leading=10, alignment=TA_CENTER),
        phase_hdr = ParagraphStyle("PH",
            fontName="Helvetica-Bold", fontSize=9,  leading=11, alignment=TA_LEFT,
            textColor=WHITE),
        phase_box = ParagraphStyle("PB",
            fontName="Helvetica-Bold", fontSize=9,  leading=11, alignment=TA_LEFT),
        stage_lbl = ParagraphStyle("SL",
            fontName="Helvetica-BoldOblique", fontSize=7.5, leading=10,
            alignment=TA_LEFT, textColor=colors.HexColor("#444444")),
        section_title = ParagraphStyle("ST",
            fontName="Helvetica-Bold", fontSize=9, leading=11,
            textColor=WHITE, alignment=TA_CENTER),
    )

def build_header(S, logo_path=None):
    txt_col = [
        Paragraph("KEMENTERIAN AGAMA REPUBLIK INDONESIA", S["inst_bold"]),
        Paragraph("DIREKTORAT JENDERAL BIMBINGAN MASYARAKAT KRISTEN", S["inst_sub"]),
        Paragraph("JL. M.H. Thamrin No.6 Jakarta 10340", S["inst_addr"]),
        Paragraph("https://www.bimaskristen.kemenag.go.id", S["inst_addr"]),
    ]
    if logo_path:
        from reportlab.platypus import Image
        logo = Image(logo_path, width=18*mm, height=18*mm)
        data = [[logo, txt_col]]
    else:
        data = [["", txt_col]]
    col_w = [22*mm, CONTENT_W - 22*mm]
    t = Table(data, colWidths=col_w)
    t.setStyle(TableStyle([
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("LEFTPADDING",   (0,0), (-1,-1), 0),
        ("RIGHTPADDING",  (0,0), (-1,-1), 0),
        ("TOPPADDING",    (0,0), (-1,-1), 0),
        ("BOTTOMPADDING", (0,0), (-1,-1), 0),
    ]))
    return t

def build_meta_table(S, data: dict = None):
    if data is None:
        data = {}
    def row(ll, lv, rl, rv):
        return [
            Paragraph(ll, S["label"]),
            Paragraph(": " + str(lv), S["label"]),
            Paragraph(rl, S["label"]),
            Paragraph(": " + str(rv), S["label"]),
        ]
    rows = [
        row("Judul Materi",          data.get("judul",""),
            "No Dokumen",            data.get("no_dokumen","")),
        row("Fase - Mata Pelajaran",  data.get("fase",""),
            "Tanggal Rilis",         data.get("tanggal_rilis","")),
        row("Tujuan Pembelajaran",    data.get("tujuan",""),
            "Total Durasi",          data.get("total_durasi","")),
        row("Capaian Pembelajaran",   data.get("capaian",""),
            "Ahli Materi",           data.get("ahli_materi","")),
    ]
    col_w = [CONTENT_W * r for r in [0.27, 0.23, 0.27, 0.23]]
    t = Table(rows, colWidths=col_w)
    t.setStyle(TableStyle([
        ("BOX",       (0,0), (-1,-1), 0.5, BLACK),
        ("INNERGRID", (0,0), (-1,-1), 0.5, BLACK),
        ("VALIGN",    (0,0), (-1,-1), "TOP"),
        ("TOPPADDING",    (0,0), (-1,-1), 2),
        ("BOTTOMPADDING", (0,0), (-1,-1), 2),
        ("LEFTPADDING",   (0,0), (-1,-1), 3),
        ("RIGHTPADDING",  (0,0), (-1,-1), 3),
    ]))
    return t

def build_approval_table(S, dibuat=None, diperiksa=None, disetujui=None):
    dibuat    = dibuat    or {"nama": "NAMA", "nip": "NIP."}
    diperiksa = diperiksa or {"nama": "NAMA", "nip": "NIP."}
    disetujui = disetujui or {"nama": "NAMA", "nip": "NIP."}

    header = [
        Paragraph("Dibuat Oleh :",    S["label"]),
        Paragraph("Diperiksa Oleh :", S["label"]),
        Paragraph("Disetujui Oleh :", S["label"]),
    ]
    sig_row = [
        [Spacer(1, 20*mm), Paragraph(dibuat["nama"],    S["label_bold"]), Paragraph(dibuat["nip"],    S["label"])],
        [Spacer(1, 20*mm), Paragraph(diperiksa["nama"], S["label_bold"]), Paragraph(diperiksa["nip"], S["label"])],
        [Spacer(1, 20*mm), Paragraph(disetujui["nama"], S["label_bold"]), Paragraph(disetujui["nip"], S["label"])],
    ]
    col_w = [CONTENT_W / 3] * 3
    t = Table([header, sig_row], colWidths=col_w)
    t.setStyle(TableStyle([
        ("BOX",       (0,0), (-1,-1), 0.5, BLACK),
        ("INNERGRID", (0,0), (-1,-1), 0.5, BLACK),
        ("VALIGN",    (0,0), (-1,-1), "TOP"),
        ("TOPPADDING",    (0,0), (-1,-1), 3),
        ("BOTTOMPADDING", (0,0), (-1,-1), 3),
        ("LEFTPADDING",   (0,0), (-1,-1), 4),
        ("RIGHTPADDING",  (0,0), (-1,-1), 4),
    ]))
    return t

def build_storyboard_title(S):
    t = Table([[Paragraph("S T O R Y B O A R D", S["section_title"])]], colWidths=[CONTENT_W])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), BLACK),
        ("TOPPADDING",    (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
    ]))
    return t

def build_phase_header(S, title: str):
    """White background with black border and bold text — like the original."""
    t = Table([[Paragraph(title, S["phase_box"])]], colWidths=[CONTENT_W])
    t.setStyle(TableStyle([
        ("BOX",           (0,0), (-1,-1), 1, BLACK),
        ("BACKGROUND",    (0,0), (-1,-1), WHITE),
        ("TOPPADDING",    (0,0), (-1,-1), 3),
        ("BOTTOMPADDING", (0,0), (-1,-1), 3),
        ("LEFTPADDING",   (0,0), (-1,-1), 4),
    ]))
    return t

MAIN_ROW_H = 22 * mm
SUB_ROW_H  = 18 * mm

def build_scene_block(S, no: str, step_label: str):
    """One complete scene block."""
    stage_row = [[Paragraph(step_label, S["stage_lbl"])]]
    stage_t = Table(stage_row, colWidths=[CONTENT_W])
    stage_t.setStyle(TableStyle([
        ("LEFTPADDING",   (0,0), (-1,-1), 2),
        ("TOPPADDING",    (0,0), (-1,-1), 2),
        ("BOTTOMPADDING", (0,0), (-1,-1), 1),
        ("RIGHTPADDING",  (0,0), (-1,-1), 2),
    ]))

    # col widths: No, Scene, Durasi, Narasi, Visual
    CW = [CONTENT_W * r for r in [0.05, 0.12, 0.08, 0.375, 0.375]]

    GRAY = colors.HexColor("#f0f0f0")
    header = [
        Paragraph("No",     S["center_sm"]),
        Paragraph("Scene",  S["center_sm"]),
        Paragraph("Durasi", S["center_sm"]),
        Paragraph("Narasi", S["center_sm"]),
        Paragraph("Visual", S["center_sm"]),
    ]
    data_row  = [Paragraph(no, S["cell_sm"]), "", "", "", ""]
    sub_hdr   = [
        "",
        Paragraph("Interaksi",          S["center_sm"]),
        "",
        Paragraph("Keterangan/Catatan", S["center_sm"]),
        "",
    ]
    sub_data  = ["", "", "", "", ""]

    rows = [header, data_row, sub_hdr, sub_data]
    row_heights = [6*mm, MAIN_ROW_H, 6*mm, SUB_ROW_H]

    t = Table(rows, colWidths=CW, rowHeights=row_heights)
    t.setStyle(TableStyle([
        ("BOX",       (0,0), (-1,-1), 0.5, BLACK),
        ("INNERGRID", (0,0), (-1,-1), 0.5, BLACK),
        ("BACKGROUND",(0,0), (-1,0),  GRAY),
        ("BACKGROUND",(0,2), (-1,2),  GRAY),
        # No spans rows 0-3 (all)
        ("SPAN", (0,0), (0,3)),
        # Narasi spans header+data rows
        ("SPAN", (3,0), (3,1)),
        # Visual spans header+data rows
        ("SPAN", (4,0), (4,1)),
        # Scene spans header+data rows
        ("SPAN", (1,0), (1,1)),
        # Durasi spans header+data rows
        ("SPAN", (2,0), (2,1)),
        # sub header: Interaksi col 1-2
        ("SPAN", (1,2), (2,2)),
        # sub header: Keterangan col 3-4
        ("SPAN", (3,2), (4,2)),
        # sub data spans
        ("SPAN", (1,3), (2,3)),
        ("SPAN", (3,3), (4,3)),
        # alignment
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("ALIGN",  (0,0), (0,-1),  "CENTER"),
        ("ALIGN",  (0,0), (-1,0),  "CENTER"),
        ("ALIGN",  (0,2), (-1,2),  "CENTER"),
        ("TOPPADDING",    (0,0), (-1,-1), 2),
        ("BOTTOMPADDING", (0,0), (-1,-1), 2),
        ("LEFTPADDING",   (0,0), (-1,-1), 3),
        ("RIGHTPADDING",  (0,0), (-1,-1), 3),
    ]))
    return KeepTogether([stage_t, t, Spacer(1, 3*mm)])

PHASES = [
    {
        "title": "TAHAP PEMBUKA",
        "scenes": [
            ("1.", "Tahap 1: Menarik Perhatian Peserta"),
            ("2.", "Tahap 2: Menyampaikan Tujuan Pembelajaran"),
            ("3.", "Tahap 3: Menggali Pengetahuan Awal Peserta"),
        ]
    },
    {
        "title": "TAHAP INTI",
        "scenes": [
            ("1.", "Tahap 4: Menyajikan Konten Pembelajaran"),
            ("2.", "Tahap 5: Latihan Interaktif"),
            ("3.", "Tahap 6: Pembelajaran Mandiri"),
        ]
    },
    {
        "title": "TAHAP PENUTUP",
        "scenes": [
            ("1.", "Tahap 7: Feedback"),
            ("2.", "Tahap 8: Refleksi"),
            ("3.", "Tahap 9: Penguatan dan Aplikasi"),
        ]
    },
]

def generate(output_path: str,
             meta: dict = None,
             dibuat: dict = None,
             diperiksa: dict = None,
             disetujui: dict = None,
             logo_path: str = None):
    """
    Generate the storyboard template PDF.

    Parameters
    ----------
    output_path  : str  – destination file path (.pdf)
    meta         : dict – keys: judul, fase, tujuan, capaian,
                          no_dokumen, tanggal_rilis, total_durasi, ahli_materi
    dibuat       : dict – keys: nama, nip
    diperiksa    : dict – keys: nama, nip
    disetujui    : dict – keys: nama, nip
    logo_path    : str  – optional path to institution logo image
    """
    doc = SimpleDocTemplate(
        output_path, pagesize=A4,
        leftMargin=MARGIN_L, rightMargin=MARGIN_R,
        topMargin=MARGIN_T,  bottomMargin=MARGIN_B,
    )
    S = make_styles()
    story = []

    story.append(build_header(S, logo_path))
    story.append(HRFlowable(width=CONTENT_W, thickness=1, color=BLACK,
                             spaceAfter=2*mm, spaceBefore=2*mm))
    story.append(build_meta_table(S, meta))
    story.append(Spacer(1, 3*mm))
    story.append(build_approval_table(S, dibuat, diperiksa, disetujui))
    story.append(Spacer(1, 4*mm))
    story.append(build_storyboard_title(S))
    story.append(Spacer(1, 4*mm))

    for phase in PHASES:
        story.append(build_phase_header(S, phase["title"]))
        story.append(Spacer(1, 2*mm))
        for (no, step_label) in phase["scenes"]:
            story.append(build_scene_block(S, no, step_label))

    doc.build(story)
    print(f"✅  Saved: {output_path}")


if __name__ == "__main__":
    import sys
    out = sys.argv[1] if len(sys.argv) > 1 else "/home/claude/storyboard_output.pdf"
    generate(output_path=out)
