from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_report(data, filename):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph("Sentinel AI Threat Report",
                  styles["Title"])
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            f"Threat Level: {data.get('threat_level')}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Attack Type: {data.get('attack_type')}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Confidence: {data.get('confidence')}",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            data.get("llm_explanation", ""),
            styles["Normal"]
        )
    )

    doc.build(content)