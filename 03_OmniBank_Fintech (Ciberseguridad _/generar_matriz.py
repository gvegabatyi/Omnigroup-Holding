import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

def generar_matriz_riesgo():
    n = 5
    # Colores para los niveles de riesgo
    cmap = ListedColormap(['#99ff99', '#ffff99', '#ffcc99', '#ff9999', '#ff3333'])

    risk_colors = np.zeros((n, n))
    for p in range(n):
        for i in range(n):
            score = (p + 1) * (i + 1)
            if score <= 4:
                risk_colors[p, i] = 0
            elif score <= 9:
                risk_colors[p, i] = 1
            elif score <= 15:
                risk_colors[p, i] = 2
            elif score <= 20:
                risk_colors[p, i] = 3
            else:
                risk_colors[p, i] = 4

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.imshow(risk_colors, origin='lower', cmap=cmap, extent=[0.5, 5.5, 0.5, 5.5])

    # Marcado del Riesgo Inherente OmniBank (P=5, I=5)
    ax.scatter(5, 5, color='black', s=200, marker='X', edgecolors='white', zorder=5)
    ax.annotate(' RIESGO OIV\n EXTREMO (25)', (5, 5), xytext=(3.0, 4.5),
                 arrowprops=dict(facecolor='black', shrink=0.05, width=1),
                 fontsize=10, fontweight='bold', 
                 bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black", alpha=0.9))

    ax.set_xticks(range(1, 6))
    ax.set_yticks(range(1, 6))
    ax.set_xlabel('Impacto / Consecuencia (ISO 31000)', fontweight='bold')
    ax.set_ylabel('Probabilidad / Frecuencia', fontweight='bold')
    ax.set_title('Matriz de Riesgo: OmniBank (OIV)', fontsize=13, fontweight='bold', pad=20)
    
    ax.set_xticks(np.arange(0.5, 6.5, 1), minor=True)
    ax.set_yticks(np.arange(0.5, 6.5, 1), minor=True)
    ax.grid(which='minor', color='black', linestyle='-', linewidth=0.5)

    plt.tight_layout()
    plt.savefig('matriz_riesgo_omnibank.png', dpi=300)
    plt.show()

if __name__ == "__main__":
    generar_matriz_riesgo()