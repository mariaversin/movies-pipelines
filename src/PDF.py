import plott
from fpdf import FPDF

def creaPDF(pelis):
    '''
    Create a pdf with the winning films of an Oscar, given one year and one genre.
    '''
    
    path_image=plott.image_movies(pelis)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(70, 15, txt="??????????????????????????????????????")
    pdf.set_font("Arial", size=8)
    pdf.image(path_image, x=110, y=60, w=100)
    #pdf.cell(200, 100, txt="Average Price", ln=1)
    #pdf.ln(85)  # move 85 down

    pdf.output("../output/result.pdf")

    return

    