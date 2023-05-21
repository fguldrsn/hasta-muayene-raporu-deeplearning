from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def form(path):
    my_canvas = canvas.Canvas(path, pagesize=letter)
    my_canvas.setLineWidth(.3)
    my_canvas.setFont('Helvetica', 12)
    my_canvas.drawString(30, 750, 'PATIENT EXAMINATION REPORT')
    my_canvas.drawString(30, 735, 'XX HOSPITAL')
    my_canvas.drawString(500, 750, "22 / 09 / 2022")
    my_canvas.line(480, 747, 580, 747)
    my_canvas.drawString(30, 650, 'PATIENT NAME:')
    my_canvas.drawString(123, 650, "JOHN DOE")
    my_canvas.line(120, 645, 580, 645)
    my_canvas.drawString(30, 597, 'PATIENT AGE:')
    my_canvas.drawString(123, 597, '32')
    my_canvas.line(115, 593, 300, 593)
    my_canvas.drawString(30, 544, 'PATIENT SYMPTOMS:')
    my_canvas.drawString(160, 544, 'HEADACHE')
    my_canvas.line(157, 540, 500, 540)
    my_canvas.drawString(30, 491, 'DIAGNOSIS:')
    my_canvas.drawString(103, 491, 'COMMON COLD')
    my_canvas.line(101, 486, 500, 486)
    my_canvas.drawString(30, 438, 'MEDICINE:')
    my_canvas.drawString(95, 438, 'PAROL')
    my_canvas.line(95, 433, 500, 433)

    my_canvas.drawString(450, 200, 'DOKTOR NAME')
    my_canvas.line(545, 180, 445, 180)
    my_canvas.drawString(460, 150, 'SIGNATURE')
    my_canvas.line(545, 130, 445, 130)

 
    

    my_canvas.save()
if __name__ == '__main__':
    form('hasta_muayene.pdf')
    
