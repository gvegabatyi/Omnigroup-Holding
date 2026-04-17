import pandas as pd
import random

# Listas para construir los nombres de fantasía
nombres_base = ["Pepe", "Francisco", "Maria", "Juan", "Coty", "Lucho", "Sacha", "Matias", "Pancha"]
animales = ["Nutria", "Leon", "Puma", "Zorro", "Condor", "Ballena", "Gato", "Perro", "Huemul"]
adjetivos = ["Salvage", "Rojo", "Veloz", "Austral", "Gigante", "Noble", "Audaz", "Sigiloso"]
patologias = ["Hipertension", "Diabetes T2", "Asma", "Hipotiroidismo", "Arritmia", "Alergia Alimentaria"]
vivienda_opciones = ["Casa Propia", "Arrienda", "Vivienda Familiar"]

def generar_dataset_omnisalud(n_registros=20000):
    datos = []
    
    for i in range(1, n_registros + 1):
        # 1. Nombre Fantasía (Ej: Pepe Nutria Salvage)
        nombre = f"{random.choice(nombres_base)} {random.choice(animales)} {random.choice(adjetivos)}"
        
        # 2. Identificador Aleatorio (Ej: 154X)
        identificador = f"{random.randint(1000, 999999)}X"
        
        # 3. Datos Sensibles y Financieros
        dia_nacimiento = f"{random.randint(1, 28)}/{random.randint(1, 12)}/{random.randint(1950, 2010)}"
        patologia = random.choice(patologias)
        cuenta_corriente = random.choice(["Si", "No"])
        moroso = random.choice(["Si", "No"])
        vivienda = random.choice(vivienda_opciones)
        
        # DATO EXTRA ESTRATÉGICO: Consentimiento (Infracción de Ley 21.719)
        consentimiento = random.choices(["Si", "No"], weights=[20, 80])[0] # 80% no tiene consentimiento
        
        datos.append([
            nombre, identificador, dia_nacimiento, patologia, 
            cuenta_corriente, moroso, vivienda, consentimiento
        ])
    
    # Crear el DataFrame
    columnas = [
        "Nombre_Completo", "ID_Interno", "Fecha_Nacimiento", "Patologia_Cronica", 
        "Tiene_Cuenta_Corriente", "Estado_Moroso", "Situacion_Habitacional", "Consentimiento_Firmado"
    ]
    
    df = pd.DataFrame(datos, columns=columnas)
    
    # Guardar en la carpeta actual
    df.to_csv("omnisalud_clientes.csv", index=False, encoding='utf-8-sig')
    print(f"✅ Dataset de OmniSalud generado exitosamente con {n_registros} registros.")

if __name__ == "__main__":
    generar_dataset_omnisalud()
    