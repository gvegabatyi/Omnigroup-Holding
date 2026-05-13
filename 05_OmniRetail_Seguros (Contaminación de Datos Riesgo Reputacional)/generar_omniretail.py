import pandas as pd
import random
import os

def generar_dataset_omniretail():
    # El peritaje anterior mostró que los archivos están en la raíz (..)
    ruta_salud = "../omnisalud_clientes.csv"
    ruta_banco = "../omnibank_clientes.csv"
    
    if os.path.exists(ruta_salud) and os.path.exists(ruta_banco):
        df_salud = pd.read_csv(ruta_salud)
        df_banco = pd.read_csv(ruta_banco)
        
        nombres = df_salud["Nombre_Completo"].tolist()
        ids = df_salud["ID_Interno"].tolist()
        patologias = df_salud["Patologia_Cronica"].tolist()
        morosidad = df_banco["Score_DICOM_Simulado"].tolist()
        
        print(f"🔗 Conexión exitosa. Cruzando datos de Salud y Finanzas.")
    else:
        print("⚠️ ERROR: No se encuentran las bases en la raíz. Revisa la ubicación de los CSV.")
        return

    datos_retail = []
    for i in range(len(nombres)):
        gasto = random.randint(15000, 900000)
        # Lógica de discriminación: Si tiene patología y score bajo (<450), seguro RECHAZADO
        if patologias[i] != "Alergia Alimentaria" and morosidad[i] < 450:
            seguro = "RECHAZADO (Riesgo Salud/Financiero)"
        else:
            seguro = "APROBADO"
            
        datos_retail.append([nombres[i], ids[i], gasto, seguro])
    
    df_retail = pd.DataFrame(datos_retail, columns=["Cliente", "ID", "Gasto_Mensual", "Estado_Seguro"])
    df_retail.to_csv("omniretail_clientes.csv", index=False, encoding='utf-8-sig')
    print(f"✅ Hito 05: Archivo 'omniretail_clientes.csv' generado con éxito.")

if __name__ == "__main__":
    generar_dataset_omniretail()