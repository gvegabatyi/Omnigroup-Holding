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
