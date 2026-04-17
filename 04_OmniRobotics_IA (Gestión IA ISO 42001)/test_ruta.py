import os

# Mirar qué hay en la carpeta de "arriba"
print("🔍 Buscando carpetas en el nivel superior...")
carpetas = os.listdir("..")
for c in carpetas:
    if "OmniSalud" in c:
        print(f"✅ CARPETA ENCONTRADA: '{c}'")
        # Mirar si el archivo está adentro
        archivo = f"../{c}/omnisalud_clientes.csv"
        if os.path.exists(archivo):
            print(f"🚀 EL ARCHIVO EXISTE EN: {archivo}")
        else:
            print(f"❌ EL ARCHIVO NO ESTÁ DENTRO DE ESA CARPETA")