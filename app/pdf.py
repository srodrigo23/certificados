
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape, A4
from reportlab.lib import colors
import os

from numero_letras import leer_miles

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

    # image_path = os.path.join(os.getcwd(), "code.png")
    # c.drawImage(image_path, 50, 400, width=150, height=150)

    c.save()

    c = canvas.Canvas("content3_pdf.pdf", pagesize=letter)
    # canvas.Canvas.setPageSize(c, (landscape(A4)))
    c.setFillColor(colors.grey)
    c.setFont("Helvetica-Bold", 24)
    c.drawString(100, 700, "Creating PDFs with Python")

    c.setFillColor(colors.black)
    c.setFont("Helvetica", 14)
    c.drawString(50, 660, "In this tutorial, we will demonstrate how to create PDF files using Python.")
    c.drawString(50, 640, "Python is a versatile programming language that can be used to create different types of files, including PDFs.")
    c.drawString(50, 620, "By the end of this tutorial, you will be able to generate PDF files using Python and the ReportLab library.")

    # image_path = os.path.join(os.getcwd(), "code.png")
    # c.drawImage(image_path, 50, 400, width=150, height=150)

    c.save()

def create_another_pdf():

    # c = canvas.Canvas("hojas(20001-21000).pdf", pagesize=letter)
    # c.setFillColor(colors.black)
    # c.setFont("Helvetica", 12)
    
    # Set the page size and margins
    width, height = letter
    
    # Text to align to the center
    initial = 1
    final = 22000
    
    # Calculate the position for center alignment
    x_position_number = width / 2
    y_position_number = height - 50  # Adjust the y-coordinate as needed

    margin = 40
    # Calculate the position for right alignment
    x_position_text = width - margin
    y_position_text = height - 70  # Adjust the y-coordinate as needed

    saltos = 1000
    for k in range(initial, final, saltos):

        c = canvas.Canvas(f"hojas({k}-{(k+saltos)-1}).pdf", pagesize=letter)
        c.setFillColor(colors.black)
        c.setFont("Helvetica", 12)

        for number_page in range(k, k+saltos, 1):
            # Text to align to the right
            text = convert_number_to_literal_string(num=number_page)
            c.drawCentredString(x_position_number, y_position_number, text)
            c.drawRightString(x_position_text, y_position_text, f"{number_page}")
            c.showPage()
        # Save the PDF file
        c.save()

def cant_dig(num:int)->int:
    if num > 0 and num <=9:
        return 1
    else:
        return 1 + cant_dig(num//10)

base = {
    1:"uno", 2:"dos", 3:"tres", 4:"cuatro", 5:"cinco", 6:"seis", 7:"siete", 8:"ocho", 9:"nueve", 10:"diez",
    11: "once", 12: "doce", 13: "trece", 14: "catorce", 15: "quince", 100: "cien", 
}
decenas = [
    "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"
]

centenas = ["", "ciento", "doscientos", "trescientos", "cuatrocientos", "quinientos", 
            "seiscientos", "setecientos", "ochocientos", "novecientos"]

def convert_number_to_literal_string(num:int)->str:
    # 1 - 99999
    cantDig = cant_dig(num=num)
    if cantDig <=2:
        return unidades_decenas_tostr(num)
    elif cantDig ==3:
        return centenas_tostr(num)
    elif cantDig == 4 or cantDig == 5:
        return miles_tostr(num)
    
def miles_tostr(num:int)->str:
    # 10 345
    miles = num // 1000
    centenas = num % 1000
    return f"{unidades_decenas_tostr(miles) if miles != 1 else ''} mil {centenas_tostr(centenas)}".strip()

def centenas_tostr(num:int)->str:
    # 123
    if num !=0:
        centena = num // 100
        unidad_decena = num % 100
        return f"{centenas[centena] if unidad_decena!= 0 else base[100]} {unidades_decenas_tostr(unidad_decena)}".strip()
    return ''

def unidades_decenas_tostr(num:int)->str:
    if num>=1 and num<=15:
        return base[num]
    elif num>=16 and num<=99:
        if num%10==0: #ultimo dig
            if num == 10:
                return base[num]
            else:   
                return decenas[(num//10)-2]
        else:
            return f'{base[10] if num//10==1 else decenas[(num//10)-2]} y {base[(num%10)]}'        
    return ""

if __name__ == "__main__":
    
    create_another_pdf()
    # create_pdf()