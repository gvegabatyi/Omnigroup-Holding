import pandas as pd
import random
import os

def generar_dataset_omnirobotics():
    # --- LÓGICA DE BÚSQUEDA AUTOMÁTICA ---
    ruta_clinica =ruta_clinica = "../omnisalud_clientes.csv"
    # Buscamos cualquier carpeta que contenga "OmniSalud" en el nivel superior
    for nombre_carpeta in os.listdir(".."):
        if "OmniSalud" in nombre_carpeta:
            posible_ruta = f"../{nombre_carpeta}/omnisalud_clientes.csv"
            if os.path.exists(posible_ruta):
                ruta_clinica = posible_ruta
                break
    
    if ruta_clinica:
        print(f"🔗 Conexión exitosa. Leyendo datos desde: {ruta_clinica}")
        df_base = pd.read_csv(ruta_clinica)
        nombres = df_base["Nombre_Completo"].tolist()
        ids = df_base["ID_Interno"].tolist()
    else:
        print("⚠️ FALLA DE SEGURIDAD: No se encontró la base de la clínica. Usando genéricos.")
        nombres = [f"Usuario {i}" for i in range(20000)]
        ids = [f"{random.randint(1000, 9999)}X" for _ in range(20000)]
    # --- FIN DE LA LÓGICA DE BÚSQUEDA ---
    datos_robots = []
    modelos = ["DomestiBot-V3 (Asistente)", "Guardian-Eye (Seguridad)", "EduPlay-Nano (Niños)"]
    
    for i in range(len(nombres)):
        modelo = random.choice(modelos)
        
        # Riesgos ISO 42001 y Protección de Datos
        recoleccion_biometrica = "Facial y Voz"
        streaming_audio_video = random.choice(["Activado", "Desactivado"])
        # Infracción de Ciberseguridad: 70% NO cifrada (Ley 21.663)
        telemetria_cifrada = random.choices(["Si", "No"], weights=[30, 70])[0] 
        sesgo_ia_detectado = random.choice(["Si", "No"])
        
        # El "Dato Fatal": Integración con el perfil de salud del holding
        acceso_perfil_salud = "Vinculado-OmniSalud" 

        datos_robots.append([
            nombres[i], ids[i], modelo, recoleccion_biometrica, 
            streaming_audio_video, telemetria_cifrada, sesgo_ia_detectado, acceso_perfil_salud
        ])
    
    columnas = [
        "Propietario", "ID_Asociado", "Modelo_Robot", "Datos_Biometricos", 
        "Grabacion_Activa", "Cifrado_Punto_a_Punto", "Alerta_Sesgo_Algoritmico", "Integracion_Holding"
    ]
    
    df_robots = pd.DataFrame(datos_robots, columns=columnas)
    df_robots.to_csv("omnirobotics_activos.csv", index=False, encoding='utf-8-sig')
    print(f"✅ Hito 04: Dataset de OmniRobotics generado. 20.000 dispositivos en riesgo.")

if __name__ == "__main__":
    generar_dataset_omnirobotics()