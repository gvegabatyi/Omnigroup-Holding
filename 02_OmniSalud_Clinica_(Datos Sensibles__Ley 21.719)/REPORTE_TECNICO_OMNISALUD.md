# 🛡️ INFORME TÉCNICO DE CUMPLIMIENTO: FILIAL OMNISALUD
**Documento Clasificado - Auditoría de Protección de Datos (Ley 21.719)**

---

## 1. RESUMEN EJECUTIVO (Executive Dashboard)
Este reporte detalla el hallazgo técnico resultante de la auditoría automatizada sobre el dataset de la filial **OmniSalud**, parte del Holding OmniGroup.

| Métrica de Control | Estado | Observación Técnica |
| :--- | :--- | :--- |
| **Nivel de Riesgo** | 🔴 CRÍTICO | Exposición de datos de salud sensibles |
| **Cumplimiento Ley 21.719** | ❌ NO CONFORME | Infracción al principio de finalidad |
| **Estándar ISO 27701** | ⚠️ BRECHA | Ausencia de controles de seudonimización |

---

## 2. ANÁLISIS DE LA BRECHA TÉCNICA
Se realizó una inspección forense mediante scripts de Python sobre el repositorio de datos para verificar la segregación de la privacidad entre filiales.

### 2.1 Evidencia en Dataset: `omnisalud_clientes.csv`
El análisis detectó la presencia de datos de salud vinculados a la identidad del sujeto de forma directa, sin capas de abstracción.

**HALLAZGO TÉCNICO:** El campo **Patologia_Cronica** está expuesto en texto plano y vinculado al **ID_Interno**. Esta configuración permite la re-identificación inmediata del paciente fuera del ámbito clínico, facilitando la "contaminación cruzada" con la base de datos de la filial de seguros (OmniRetail).

### 2.2 Validación de Lógica de Auditoría
Se ejecutó un control técnico de validación para detectar el riesgo de infracción ante la futura **Agencia de Protección de Datos (APDP)**.

**Lógica de detección aplicada:**
* Si el origen de los datos es **OmniSalud** y existen campos de salud vinculados a IDs persistentes, se activa una alerta de riesgo gravísimo.
* La recomendación técnica inmediata es la implementación de **Tokenización Dinámica** para romper el vínculo identificatorio.

---

## 3. DICTAMEN JURÍDICO - ESTRATÉGICO
Bajo el nuevo marco regulatorio chileno, este hallazgo representa un riesgo financiero de hasta **20.000 UTM** por cada infracción detectada, sumado a una pérdida reputacional crítica para el Directorio del Holding.

**Recomendaciones del DPO:**
1. **Cifrado en Reposo:** Aplicar estándares AES-256 a la base de datos de patologías.
2. **Segregación de Funciones:** Implementar un modelo de acceso basado en roles (RBAC) que impida a las áreas comerciales acceder a registros médicos.
3. **Accountability:** Registrar esta brecha en el Libro de Incidentes y aplicar medidas de remediación antes de la plena entrada en vigencia de la Ley 21.719.

---
---
## ANEXO TÉCNICO: EVIDENCIA DE SCRIPTING
Para la detección de la brecha se utilizó la siguiente lógica en Python:

```python
import pandas as pd

# Carga de activos de salud
df = pd.read_csv('omnisalud_clientes.csv')

# Identificación de vinculación prohibida (Art. 9 Ley 21.719)
def auditoria_privacidad(data):
    for index, row in data.iterrows():
        if pd.notnull(row['Patologia_Cronica']) and pd.notnull(row['ID_Interno']):
            return "HALLAZGO: Contaminación de datos identificables detectada"

print(auditoria_privacidad(df))

**Gonzalo Vega Batyi** *Abogado Experto en Ciberseguridad y Protección de Datos* *Certificado ISO 27001 / ISO 42001*