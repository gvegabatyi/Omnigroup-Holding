import os
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from pypdf import PdfReader, PdfWriter
import io

def crear_marca_agua():
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    can.setFillAlpha(0.15)  # Opacidad baja (15%)
    can.setFont("Helvetica-Bold", 45)
    can.setFillColorRGB(0.7, 0.7, 0.7)  # Gris claro
    
    # Crear el mosaico diagonal
    for x in range(-3, 12, 4):
        for y in range(-2, 16, 2):
            can.saveState()
            can.translate(x*inch, y*inch)
            can.rotate(45)
            can.drawCentredString(0, 0, "GVB ABOGADO GRC")
            can.restoreState()
    can.save()
    packet.seek(0)
    return PdfReader(packet).pages[0]

def proteger_carpeta():
    marca_agua = crear_marca_agua()
    # Buscar solo los PDFs originales (que no sean ya protegidos)
    archivos = [f for f in os.listdir('.') if f.endswith('.pdf') and '_PROTECTED' not in f]
    
    for nombre_archivo in archivos:
        print(f"Protegiendo: {nombre_archivo}...")
        reader = PdfReader(nombre_archivo)
        writer = PdfWriter()
        
        for pagina in reader.pages:
            pagina.merge_page(marca_agua)
            writer.add_page(pagina)
        
        nombre_salida = nombre_archivo.replace(".pdf", "_PROTECTED.pdf")
        with open(nombre_salida, "wb") as f:
            writer.write(f)
    print("¡Proceso completado! Revisa tus archivos con el sufijo _PROTECTED.")

if __name__ == "__main__":
    proteger_carpeta()