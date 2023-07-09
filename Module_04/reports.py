#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(Attachment, Title, Para):
    report = SimpleDocTemplate(Attachment)
    styles = getSampleStyleSheet()
    report_title = Paragraph(Title , styles["h1"])
    report_para = Paragraph(Para, styles["BodyText"])
    empty_space = Spacer(1,20)
    report.build([report_title, empty_space, report_para])