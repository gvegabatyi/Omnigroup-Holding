import os

print("--- INICIO DE PERITAJE ---")
print(f"📍 Estás parado en: {os.getcwd()}")
print("\n📂 Carpetas que veo un nivel más arriba (..):")

try:
    contenido = os.listdir("..")
    for item in contenido:
        if os.path.isdir(f"../{item}"):
            print(f"  - [CARPETA] {item}")
        else:
            print(f"  - [ARCHIVO] {item}")
except Exception as e:
    print(f"❌ Error al mirar arriba: {e}")

print("\n--- FIN DE PERITAJE ---")