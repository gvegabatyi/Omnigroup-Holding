import matplotlib.pyplot as plt
import matplotlib.patches as patches

def crear_diagrama_gobernanza():
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Estilos de cajas
    estilo_directorio = dict(boxstyle='round,pad=0.5', facecolor='#2c3e50', edgecolor='black', alpha=1)
    estilo_comite = dict(boxstyle='round,pad=0.5', facecolor='#34495e', edgecolor='black', alpha=0.9)
    estilo_liderazgo = dict(boxstyle='round,pad=0.5', facecolor='#e67e22', edgecolor='black', alpha=0.8)
    estilo_operativo = dict(boxstyle='round,pad=0.5', facecolor='#ecf0f1', edgecolor='black', alpha=1)

    # Nivel 1: Alta Dirección
    ax.text(5, 9.2, "ALTA DIRECCIÓN / DIRECTORIO\n(Responsabilidad Legal Final)", 
            ha='center', va='center', color='white', weight='bold', bbox=estilo_directorio)

    # Nivel 2: Comité de Riesgos OIV
    ax.text(5, 7.8, "COMITÉ DE RIESGOS Y CIBERSEGURIDAD\n(Gobernanza ISO 31000 / Ley 21.663)", 
            ha='center', va='center', color='white', weight='bold', bbox=estilo_comite)

    # Nivel 3: Liderazgo Técnico-Jurídico
    ax.text(3, 6.2, "DPO (Delegado Protección Datos)\nGestión de Privacidad ISO 27701", 
            ha='center', va='center', color='white', weight='bold', bbox=estilo_liderazgo)
    ax.text(7, 6.2, "CISO (Chief Information Security Officer)\nSeguridad de Información ISO 27001", 
            ha='center', va='center', color='white', weight='bold', bbox=estilo_liderazgo)

    # Nivel 4: Controles de Tratamiento
    ax.text(5, 4.5, "SISTEMA DE GESTIÓN DE INFORMACIÓN DE PRIVACIDAD (PIMS)\nTokenización | Air Gapping | Control de Acceso JIT", 
            ha='center', va='center', color='black', weight='bold', bbox=estilo_operativo)

    # Nivel 5: Reporte Externo
    ax.text(5, 2.8, "CANAL DE REPORTE OBLIGATORIO\nANCI (Ciberseguridad) | APDP (Privacidad) | CMF (Bancario)", 
            ha='center', va='center', color='black', style='italic', bbox=estilo_operativo)

    # Conectores (Flechas)
    arrow_props = dict(arrowstyle='->', lw=1.5, color='black')
    ax.annotate('', xy=(5, 8.8), xytext=(5, 8.2), arrowprops=arrow_props)
    ax.annotate('', xy=(5, 7.4), xytext=(5, 6.8), arrowprops=arrow_props)
    ax.annotate('', xy=(3, 6.8), xytext=(5, 7.4), arrowprops=arrow_props)
    ax.annotate('', xy=(7, 6.8), xytext=(5, 7.4), arrowprops=arrow_props)
    ax.annotate('', xy=(5, 5.8), xytext=(3, 5.8), arrowprops=arrow_props)
    ax.annotate('', xy=(5, 5.8), xytext=(7, 5.8), arrowprops=arrow_props)
    ax.annotate('', xy=(5, 3.2), xytext=(5, 4.0), arrowprops=arrow_props)

    plt.title("Estructura de Gobernanza de Privacidad y Ciberseguridad - OmniBank OIV", 
              fontsize=14, fontweight='bold', pad=20)
    
    plt.tight_layout()
    nombre_archivo = 'diagrama_gobernanza_omnibank.png'
    plt.savefig(nombre_archivo, dpi=300)
    plt.show()

if __name__ == "__main__":
    crear_diagrama_gobernanza()