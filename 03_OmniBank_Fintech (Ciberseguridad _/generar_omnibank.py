import pandas as pd
import random
import os

def generar_dataset_omnibank():
    # 1. Intentar leer los datos de la clínica para simular la filtración
    ruta_clinica = "../02_OmniSalud_Clinica_(Datos Sensibles__Ley 21.719)/omnisalud_clientes.csv"
    
    if os.path.exists(ruta_clinica):
        df_clinica = pd.read_csv(ruta_clinica)
        nombres = df_clinica["Nombre_Completo"].tolist()
        ids = df_clinica["ID_Interno"].tolist()
        morosidad_clinica = df_clinica["Estado_Moroso"].tolist()
    else:
        print("⚠️ No se encontró el archivo de la clínica. Generando nombres genéricos...")
        nombres = [f"Usuario {i}" for i in range(20000)]
        ids = [f"{random.randint(1000, 9999)}X" for _ in range(20000)]
        morosidad_clinica = ["No"] * 20000

    datos_banco = []
    
    for i in range(len(nombres)):
        saldo = random.randint(50000, 15000000)
        score = random.randint(300, 900)
        
        # Lógica de infracción: Si era moroso en la clínica, el banco lo marca
        if morosidad_clinica[i] == "Si":
            producto = "Crédito Recuperación Salud (Interés 35%)"
        else:
            producto = "Cuenta Corriente Premium"
            
        dias_clave = random.randint(1, 400) # Más de 90 días es riesgo en Ley 21.663
        
        datos_banco.append([
            nombres[i], ids[i], saldo, score, producto, dias_clave
        ])
    
    columnas = [
        "Nombre_Cliente", "ID_Asociado", "Saldo_Cuenta", 
        "Score_DICOM_Simulado", "Oferta_Comercial_Asignada", "Dias_Desde_Ultima_Clave"
    ]
    
    df_banco = pd.DataFrame(datos_banco, columns=columnas)
    df_banco.to_csv("omnibank_clientes.csv", index=False, encoding='utf-8-sig')
    print(f"✅ Dataset de OmniBank generado. Se detectaron {len(nombres)} clientes compartidos ilegalmente.")

if __name__ == "__main__":
    generar_dataset_omnibank()