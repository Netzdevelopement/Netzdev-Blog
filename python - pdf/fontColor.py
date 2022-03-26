from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_text_color(137,70,70) 
pdf.set_font("helvetica", "B", 16)
pdf.cell(40, 10, "Netzdev")
pdf.output("fontColor.pdf")