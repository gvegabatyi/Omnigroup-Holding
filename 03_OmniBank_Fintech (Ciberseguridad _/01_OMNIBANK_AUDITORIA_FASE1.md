# Expediente 02: OmniBank - Sector Financiero
##  Fase 1: Contexto, Licitud y Descripción Sistemática

### 1. Introducción y Alcance
Este expediente aborda la auditoría de cumplimiento y gestión de riesgos del activo de información de **OmniBank**, filial financiera del Holding. A diferencia del caso clínico, aquí el foco se desplaza hacia la **protección de activos financieros**, la **reserva bancaria** y la **seguridad de la infraestructura crítica**.

* **Entidad:** OmniBank.
* **Activo Crítico:** `omnibank_clientes.csv`.
* **Naturaleza del Dato:** Datos económicos, perfiles de riesgo crediticio y saldos transaccionales.

### 2. Marco Normativo Aplicable
El tratamiento de datos en este expediente se rige bajo un estándar de "Especialidad Normativa":
1.  **Ley 21.719:** Regula el tratamiento de datos personales y la protección de la vida privada (enfoque en datos económicos).

### 3. Clasificación bajo la Ley Marco de Ciberseguridad (Ley 21.663)
OmniBank ha sido designado como **Operador de Importancia Vital (OIV)** por la Agencia Nacional de Ciberseguridad (ANCI).

* **Impacto de la Calificación:** Esta categoría implica que la base de datos `omnibank_clientes.csv` es parte de la **Infraestructura Crítica de la Información (ICI)** de la nación.
* **Deberes Especiales:** Se activan los protocolos de gestión de riesgos de seguridad de nivel superior y la obligación de reporte inmediato ante incidentes que afecten la integridad o disponibilidad del activo financiero.

3.  **Ley General de Bancos (Art. 154):** Establece el deber de secreto y reserva bancaria.
4.  **ISO 27001 / ISO 27701:** Estándares técnicos para el sistema de gestión de seguridad y privacidad.

### 3. Identificación del Activo de Información
| Variable | Descripción Técnica | Sensibilidad Jurídica |
| :--- | :--- | :--- |
| `ID_Cliente` | Identificador único del sujeto. | Dato Personal. |
| `Saldo_Promedio` | Patrimonio y liquidez del titular. | **Dato Sensible (Económico).** |
| `Score_DICOM` | Perfilamiento de riesgo crediticio. | **Dato Sensible / Perfilamiento.** |
| `Historial_Pagos` | Comportamiento financiero. | Protegido por Reserva Bancaria. |

### 4. Hallazgos de Auditoría (Gap Analysis)
Tras el análisis sistemático del flujo de datos en el Holding, se detectan las siguientes vulneraciones:

* **Vulneración del Principio de Finalidad (Art. 9 Ley 21.719):** Los datos financieros captados por el Banco para la evaluación de créditos están siendo compartidos con la filial de Retail para campañas de marketing sin el consentimiento expreso, específico e informado del titular.
* **Riesgo de Infraestructura Crítica (Ley 21.663):** La interconexión física y lógica entre el Banco y el Retail no presenta "Air Gapping" ni segmentación de red suficiente. Un incidente de ciberseguridad en el Retail podría escalar al Core Bancario, afectando la continuidad del servicio esencial.
* **Debilidad en la Cadena de Custodia:** Se observa que el personal de TI del Holding tiene privilegios de lectura sobre el dataset `omnibank_clientes.csv`, contraviniendo el deber de reserva bancaria estricta.

### 5. Conclusión inicial 
El estado actual de tratamiento de datos en OmniBank es de **Riesgo Crítico**. La base de licitud de "Ejecución de Contrato" solo cubre las operaciones bancarias, pero no autoriza el flujo de datos hacia otras filiales del Holding. 

---
