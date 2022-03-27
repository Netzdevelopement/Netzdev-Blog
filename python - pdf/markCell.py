from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_fill_color(137,70,70)
pdf.set_font("helvetica", "B", 16)
pdf.cell(40, 10, "Netzdev", fill = True)
pdf.output("markCell.pdf")