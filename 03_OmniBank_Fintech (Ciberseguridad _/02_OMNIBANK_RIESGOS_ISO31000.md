# Expediente 02: OmniBank - Sector Financiero
## Fase 2: Evaluación de Riesgos bajo Norma ISO 31000:2018

### 1. Marco de Gestión de Riesgos (ISO 31000)
Para este expediente, la gestión de riesgos no se limita al cumplimiento legal, sino que se integra en el corazón de la gobernanza de OmniBank. Como **Operador de Importancia Vital (OIV)**,  responsabilidad sobre la estabilidad financiera y la infraestructura crítica nacional (Ley 21.663).

### 2. Identificación de Riesgos (Contexto OIV y Ley 21.719)
Hemos identificado los eventos de riesgo que pueden impedir que OmniBank cumpla con sus objetivos de seguridad y privacidad:

| ID | Riesgo Identificado | Factor de Riesgo (Causa) | Activo Afectado |
| :--- | :--- | :--- | :--- |
| **R.01** | **Vulneración de Reserva Bancaria** | Interconexión lógica sin segmentación con filiales de Retail. | `omnibank_clientes.csv` |
| **R.02** | **Sanción Gravísima APDP** | Tratamiento de datos económicos sin base de licitud válida (finalidad contaminada). | Reputación y Patrimonio (hasta 20.000 UTM). |
| **R.03** | **Interrupción de Servicio Esencial** | Movimiento lateral de una amenaza desde el Holding hacia el Core Bancario. | Disponibilidad del Servicio OIV. |
| **R.04** | **Decisiones Automatizadas Sesgadas** | Uso de algoritmos de perfilamiento sobre datos de solvencia no actualizados. | Derechos ARCO del Titular. |

### 3. Análisis y Evaluación de Riesgos (Matriz 5x5)
Bajo los criterios de la ISO 31000, evaluamos el **Riesgo Inherente** (antes de controles):

* **Probabilidad (P):** **5 (Casi Seguro)** - La interconexión técnica actual es un puente permanente de datos entre filiales.
* **Impacto (I):** **5 (Catastrófico)** - La calificación de OIV implica que una brecha escala a nivel de seguridad nacional y pérdida de licencia bancaria.
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
from matplotlib.lines import Line2D

# Configuración de la Matriz 5x5
n = 5
cmap = ListedColormap(['#99ff99', '#ffff99', '#ffcc99', '#ff9999', '#ff3333'])

## Definición lógica de niveles de riesgo (Probabilidad x Impacto)
risk_colors = np.zeros((n, n))
for p in range(n):
    for i in range(n):
        score = (p + 1) * (i + 1)
        if score <= 4: risk_colors[p, i] = 1   # Bajo
        elif score <= 9: risk_colors[p, i] = 2 # Medio
        elif score <= 15: risk_colors[p, i] = 3 # Alto
        else: risk_colors[p, i] = 4             # Extremo (OIV)

fig, ax = plt.subplots(figsize=(8, 6))
ax.imshow(risk_colors, origin='lower', cmap=cmap, extent=[0.5, 5.5, 0.5, 5.5])

# Marcado del Riesgo Inherente detectado para OmniBank (P=5, I=5)
ax.scatter(5, 5, color='black', s=200, marker='X', label='OmniBank OIV')
ax.annotate(' RIESGO OIV\n EXTREMO (25)', (5, 5), xytext=(3.5, 4.5),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, fontweight='bold', bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black"))

# Etiquetas y Título
ax.set_xticks(range(1, 6))
ax.set_yticks(range(1, 6))
ax.set_xlabel('Impacto (Consecuencia)', fontweight='bold')
ax.set_ylabel('Probabilidad (Frecuencia)', fontweight='bold')
ax.set_title('Matriz de Riesgo ISO 31000 - OmniBank (OIV)', fontsize=14, fontweight='bold')
ax.grid(which='minor', color='black', linestyle='-', linewidth=1)

plt.tight_layout()
plt.savefig('matriz_riesgo_omnibank.png')

**Nivel de Riesgo Inherente: 25 (Extremo - Crítico)**

### 4. Estrategia de Tratamiento de Riesgos
Siguiendo la ISO 31000, la dirección debe optar por **Mitigar** o **Evitar**. La aceptación no es una opción para un OIV.

1.  **Mitigación Técnica:**
    * Implementación inmediata de **Aislamiento Lógico (Air Gapping)** entre el Banco y el Holding.
    * Cifrado de extremo a extremo de la base `omnibank_clientes.csv`.
2.  **Mitigación Jurídica (Compliance):**
    * Redacción de cláusulas de **Secreto Bancario Reforzado** para todo personal con acceso a infraestructura crítica.
    * Auditoría de los contratos de consentimiento para asegurar la especificidad requerida por la Ley 21.719.
3.  **Monitoreo y Revisión:**
    * Establecimiento de un canal de reporte inmediato a la **ANCI** (Agencia Nacional de Ciberseguridad) para cumplir con los plazos de la Ley 21.663.

### 5. Conclusión de la Fase 2
El análisis bajo ISO 31000 confirma que la estructura actual del Holding es **incompatible** con la seguridad que se exige a un Operador de Importancia Vital. El riesgo de "contagio" desde la filial de Retail hacia el Banco es la mayor amenaza para la continuidad operativa de la institución.

---
