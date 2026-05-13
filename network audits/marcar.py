import os, io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from pypdf import PdfReader, PdfWriter

def crear_sello():
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    can.setFillAlpha(0.12) 
    can.setFont("Helvetica-Bold", 42)
    can.setFillColorRGB(0.7, 0.7, 0.7) 
    for x in range(-2, 12, 4):
        for y in range(-1, 14, 2):
            can.saveState()
            can.translate(x*inch, y*inch)
            can.rotate(45)
            can.drawCentredString(0, 0, "GVB ABOGADO GRC")
            can.restoreState()
    can.save()
    packet.seek(0)
    return PdfReader(packet).pages[0]

def procesar():
    marca = crear_sello()
    output_dir = "PORTAFOLIO_FINAL"
    if not os.path.exists(output_dir): os.makedirs(output_dir)
    archivos = [f for f in os.listdir('.') if f.lower().endswith('.pdf') and 'PROTECTED' not in f]
    for f in archivos:
        print(f"Aplicando sello profesional a: {f}...")
        reader = PdfReader(f); writer = PdfWriter()
        for pagina in reader.pages:
            pagina.merge_page(marca); writer.add_page(pagina)
        with open(os.path.join(output_dir, f"PROTECTED_{f}"), "wb") as salida:
            writer.write(salida)
    print(f"\n✅ Archivos listos en la carpeta '{output_dir}'")

if __name__ == "__main__":
    procesar()