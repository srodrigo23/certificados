
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape, A4
from reportlab.lib import colors
import os

def create_pdf():
    c = canvas.Canvas("content2_pdf.pdf", pagesize=letter)
    # canvas.Canvas.setPageSize(c, (landscape(A4)))
    c.setFillColor(colors.grey)
    c.setFont("Helvetica-Bold", 24)
    c.drawString(100, 700, "Creating PDFs with Python")

    c.setFillColor(colors.black)
    c.setFont("Helvetica", 14)
    c.drawString(50, 660, "In this tutorial, we will demonstrate how to create PDF files using Python.")
    c.drawString(50, 640, "Python is a versatile programming language that can be used to create different types of files, including PDFs.")
    c.drawString(50, 620, "By the end of this tutorial, you will be able to generate PDF files using Python and the ReportLab library.")

    image_path = os.path.join(os.getcwd(), "code.png")
    c.drawImage(image_path, 50, 400, width=150, height=150)

    c.save()

if __name__ == "__main__":
    create_pdf()
