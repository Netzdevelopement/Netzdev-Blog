from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.image("logo.jpg", x=10, y=8, w=100)
pdf.set_font("helvetica", size=12)
pdf.output("image.pdf")