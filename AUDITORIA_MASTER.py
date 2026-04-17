import pandas as pd
import os

def consolidar_evidencia_holding():
    print("🕵️‍♂️ Iniciando Consolidación Forense de Datos - OmniGroup...")
    
    # Rutas detectadas en el peritaje
    archivos = {
        "Salud": "omnisalud_clientes.csv",
        "Banco": "omnibank_clientes.csv",
        "Robots": "04_OmniRobotics_IA (Gestión IA ISO 42001)/omnirobotics_activos.csv",
        "Retail": "05_OmniRetail_Seguros (Contaminación de Datos Riesgo Reputacional)/omniretail_clientes.csv"
    }

    try:
        # 1. Cargar bases de datos
        df_salud = pd.read_csv(archivos["Salud"])
        df_banco = pd.read_csv(archivos["Banco"])
        df_robots = pd.read_csv(archivos["Robots"])
        df_retail = pd.read_csv(archivos["Retail"])

        # 2. Unión de Datos (Merging)
        # Unimos Salud con Banco
        master = pd.merge(df_salud, df_banco, left_on="ID_Interno", right_on="ID_Asociado")
        # Unimos con Robots
        master = pd.merge(master, df_robots, left_on="ID_Interno", right_on="ID_Asociado")
        # Unimos con Retail (usando la columna ID)
        master = pd.merge(master, df_retail, left_on="ID_Interno", right_on="ID")

        # 3. Identificar columna de seguro (evita el error de nombre)
        # Buscamos cualquier columna que contenga la palabra 'Seguro'
        col_seguro = [c for c in df_retail.columns if 'Seguro' in c][0]

        # 4. Selección de Columnas para el Reporte Final
        reporte_dpo = master[[
            "Nombre_Completo", 
            "ID_Interno", 
            "Patologia_Cronica", 
            "Score_DICOM_Simulado", 
            "Modelo_Robot", 
            col_seguro  # Usamos la columna detectada automáticamente
        ]]

        # 5. Generar la "Prueba Reina"
        reporte_dpo.to_csv("REPORTE_CRITICO_AUDITORIA_OMNIGROUP.csv", index=False, encoding='utf-8-sig')
        
        print(f"🔥 ¡OPERACIÓN EXITOSA!")
        print(f"Se ha generado el REPORTE_CRITICO_AUDITORIA_OMNIGROUP.csv")
        print(f"Total de ciudadanos vulnerados: {len(reporte_dpo)}")

    except Exception as e:
        print(f"❌ Error en la consolidación: {e}")

if __name__ == "__main__":
    consolidar_evidencia_holding()