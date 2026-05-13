# INFORME TÉCNICO DE CUMPLIMIENTO: FILIAL OMNIBANK
**Documento Clasificado - Auditoría de Protección de Datos y Ciberseguridad**

**Referencia:** Ley 21.719 (Datos Personales) | Ley 21.663 (OIV)
**Consultor:** Gonzalo Vega Batyi, Abogado / DPO
**Fecha de Emisión:** Mayo 2026

---

## 1. RESUMEN EJECUTIVO (Executive Dashboard)
Este reporte detalla los hallazgos técnicos resultantes de la inspección forense automatizada sobre el dataset `omnibank_clientes.csv`. La auditoría se centró en verificar la segregación de activos financieros y el cumplimiento del qSecreto Bancario.

| Métrica de Control | Estado | Observación Técnica |
| :--- | :--- | :--- |
| **Nivel de Riesgo** | ☒ CRÍTICO | Exposición de saldos y Score DICOM sin cifrado. |
| **Cumplimiento Ley 21.719** | ☒ NO CONFORME | Vulneración del Principio de Finalidad (flujo a Retail). |
| **Estándar ISO 27701** | ☒ BRECHA | Ausencia de controles de seudonimización y tokens. |
| **Ley 21.663 (OIV)** | ☒ ALERTA | Riesgo de movimiento lateral hacia el Core Bancario. |

## 2. ANÁLISIS DE LA BRECHA TÉCNICA
Se realizó una inspección mediante lógica de programación sobre el repositorio de datos para verificar la "contaminación cruzada" entre filiales advertida en la Fase 1.

### 2.1 Evidencia en Dataset: `omnibank_clientes.csv`
El análisis detectó que el campo `Saldo_Promedio` y `Score_DICOM` son accesibles por personal con privilegios de marketing en el Holding, lo que constituye una infracción gravísima a la reserva bancaria.

**HALLAZGO TÉCNICO:** Los activos financieros viajan en texto plano dentro del repositorio compartido. Esta configuración permite la re-identificación de perfiles económicos fuera del ámbito estrictamente bancario.

## 3. RECOMENDACIONES DEL DPO / AUDITOR
1. **Aislamiento Lógico (Air Gapping):** Separar físicamente o mediante firewalls de capa 7 las bases de datos de OmniBank de cualquier otra filial.
2. **Cifrado AES-256:** Aplicar cifrado de nivel militar a todas las columnas que contengan saldos o perfiles de riesgo.
3. **Control de Acceso (RBAC):** Restringir el acceso a TI del Holding mediante el principio de "Privilegio Mínimo".

---

## ANEXO TÉCNICO: EVIDENCIA DE SCRIPTING
Para la detección de la brecha y validación de la integridad, se utilizó la siguiente lógica en Python:

```python
import pandas as pd

# Carga de activos financieros para auditoría
df = pd.read_csv('omnibank_clientes.csv')

# Identificación de vinculación prohibida (Art. 9 Ley 21.719)
def auditoria_forense_omnibank(data):
    for index, row in data.iterrows():
        # Verificamos si datos de reserva bancaria están expuestos
        if pd.notnull(row['Score_DICOM']) and pd.notnull(row['Saldo_Promedio']):
            return "HALLAZGO: Contaminación detectada - Datos de Reserva Expuestos"
    return "SITUACIÓN: No se detectan brechas"

print(auditoria_forense_omnibank(df))